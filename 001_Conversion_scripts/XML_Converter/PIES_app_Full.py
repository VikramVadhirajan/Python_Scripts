import streamlit as st
import xml.etree.ElementTree as ET
import pandas as pd
from io import BytesIO

st.title("PIES XML → Excel Converter")
st.write("Upload a PIES XML file and select which sheets to export.")

uploaded_file = st.file_uploader("Upload PIES XML", type=["xml"])


def parse_pies(xml_file):

    items = []
    descriptions = []
    attributes = []
    extended = []
    packages = []
    interchanges = []

    for event, elem in ET.iterparse(xml_file, events=("end",)):

        tag = elem.tag.split("}")[-1]

        if tag == "Item":

            item_row = {}

            for k, v in elem.attrib.items():
                item_row[k] = v

            for child in elem:

                ctag = child.tag.split("}")[-1]

                if ctag not in [
                    "Descriptions",
                    "ExtendedInformation",
                    "ProductAttributes",
                    "Packages",
                    "PartInterchangeInfo"
                ]:

                    if child.text and child.text.strip():
                        item_row[ctag] = child.text.strip()

                    for a, v in child.attrib.items():
                        item_row[f"{ctag}_{a}"] = v

            items.append(item_row)

            part = item_row.get("PartNumber")
            part_terminology = item_row.get("PartTerminologyID")

            # Descriptions
            desc = elem.find(".//{*}Descriptions")
            if desc is not None:
                for d in desc:
                    descriptions.append({
                        "PartNumber": part,
                        "DescriptionCode": d.attrib.get("DescriptionCode"),
                        "Text": d.text
                    })

            # Attributes
            attrs = elem.find(".//{*}ProductAttributes")
            if attrs is not None:
                for a in attrs:
                    attributes.append({
                        "PartNumber": part,
                        "PartTerminologyID": part_terminology,
                        "AttributeID": a.attrib.get("AttributeID"),
                        "UOM": a.attrib.get("AttributeUOM"),
                        "Value": a.text
                    })

            # Extended Info
            ext = elem.find(".//{*}ExtendedInformation")
            if ext is not None:
                for e in ext:
                    extended.append({
                        "PartNumber": part,
                        "Code": e.attrib.get("EXPICode"),
                        "Value": e.text
                    })

            # Packages
            pkg = elem.find(".//{*}Packages")
            if pkg is not None:
                for p in pkg:
                    packages.append({
                        "PartNumber": part,
                        "PackageUOM": p.findtext(".//{*}PackageUOM"),
                        "Quantity": p.findtext(".//{*}QuantityofEaches")
                    })

            # Interchange
            inter = elem.find(".//{*}PartInterchangeInfo")
            if inter is not None:
                for i in inter:
                    interchanges.append({
                        "PartNumber": part,
                        "BrandAAIAID": i.attrib.get("BrandAAIAID"),
                        "PartNumber_Interchange": i.findtext(".//{*}PartNumber")
                    })

            elem.clear()

    dfs = {
        "Items": pd.DataFrame(items),
        "Descriptions": pd.DataFrame(descriptions),
        "Attributes": pd.DataFrame(attributes),
        "ExtendedInfo": pd.DataFrame(extended),
        "Packages": pd.DataFrame(packages),
        "Interchange": pd.DataFrame(interchanges)
    }

    return dfs


def create_excel(selected_sheets):

    output = BytesIO()

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:

        for name, df in selected_sheets.items():
            df.to_excel(writer, sheet_name=name, index=False)

    output.seek(0)
    return output


if uploaded_file:

    with st.spinner("Parsing XML..."):
        dfs = parse_pies(uploaded_file)

    st.success("XML parsed successfully")

    # Preview data
    for name, df in dfs.items():
        st.subheader(name)
        st.dataframe(df.head(50))

    st.divider()

    st.subheader("Select Sheets to Export")

    selected = st.multiselect(
        "Choose sheets",
        list(dfs.keys()),
        default=["Items"]
    )

    if selected:

        selected_data = {name: dfs[name] for name in selected}

        excel_file = create_excel(selected_data)

        st.download_button(
            "Download Excel",
            excel_file,
            file_name="pies_selected_output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )