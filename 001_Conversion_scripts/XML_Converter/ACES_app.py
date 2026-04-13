import streamlit as st
import xml.etree.ElementTree as ET
import pandas as pd
from io import BytesIO


st.title("ACES XML → Excel Converter")

st.write("Upload an ACES XML file to convert it into Excel.")


uploaded_file = st.file_uploader("Upload XML file", type=["xml"])


def parse_xml(xml_file):
    rows = []

    for event, elem in ET.iterparse(xml_file, events=("end",)):

        if elem.tag == "App":

            row = {}

            # App attributes
            for k, v in elem.attrib.items():
                row[f"App_{k}"] = v

            # Child elements
            for child in elem:

                # attributes
                if child.attrib:
                    for attr, val in child.attrib.items():
                        row[f"{child.tag}_{attr}"] = val

                # text values
                if child.text and child.text.strip():
                    row[child.tag] = child.text.strip()

                # nested elements
                for sub in child:
                    if sub.text and sub.text.strip():
                        row[f"{child.tag}_{sub.tag}"] = sub.text.strip()

            rows.append(row)

            elem.clear()

    df = pd.DataFrame(rows)

    return df


def convert_to_excel(df):
    output = BytesIO()

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="ACES_Data")

    output.seek(0)
    return output


@st.cache_data
def convert_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")


@st.cache_data
def convert_to_excel(df):
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer

if uploaded_file:

    with st.spinner("Parsing XML..."):
        df = parse_xml(uploaded_file)

    st.success("XML Parsed Successfully!")

    st.subheader("Preview Data")
    st.dataframe(df.head(100))

    st.write(f"Total Rows: {len(df)}")

    st.subheader("Download Data")

    file_type = st.radio(
            "Download format",
            ["CSV (recommended ⚡)", "Excel"]
            )

    if file_type.startswith("CSV"):
        data = convert_to_csv(df)
        file_name = "VCdb_output.csv"

    else:
        data = convert_to_excel(df)
        file_name = "VCdb_output.xlsx"

    downloaded = st.download_button(
        "Download file",
        data=data,
        file_name=file_name
    )

    if downloaded:
        st.success("✅ File Downloadeed successfully.")
    
else:
    st.info("Upload an ACES XML file to convert it into Excel.")