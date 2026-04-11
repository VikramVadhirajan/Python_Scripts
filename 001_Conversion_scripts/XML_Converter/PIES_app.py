import os
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import xml.etree.ElementTree as ET
from io import BytesIO

st.set_page_config(page_title="PIES Converter From XML to Excel", layout="wide")
st.title(" PIES Converter From XML to Excel")


st.markdown("Upload a **PIES XML file** and **AutoCare PCA mapping file** to extract Product Attributes.")

# Upload files
xml_file = st.file_uploader("Upload PIES XML", type=["xml"])


def parse_pies(xml_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Namespace for AutoCare XML
    ns = {"ns": "http://www.autocare.org"}

    data = []

    items = root.findall(".//ns:Item", ns)

    extended_info_data = []
    product_attr_data = []

    # Loop through each Item element and extract the desired values.
    for item in items:
        # Get the PartNumber and PartTerminologyID
        part_number_elem = item.find("ns:PartNumber", ns)
        part_term_elem = item.find("ns:PartTerminologyID", ns)
        part_number = part_number_elem.text if part_number_elem is not None else None
        part_terminology_id = part_term_elem.text if part_term_elem is not None else None

        # Extract ExtendedInformation values
        for ext in item.findall("ns:ExtendedInformation/ns:ExtendedProductInformation", ns):
            extended_info_data.append({
                "PartNumber": part_number,
                "PartTerminologyID": part_terminology_id,
                "EXPICode": ext.attrib.get("EXPICode"),
                "Value": ext.text
            })

        # Extract ProductAttributes values
        for attr in item.findall("ns:ProductAttributes/ns:ProductAttribute", ns):
            product_attr_data.append({
                "PartNumber": part_number,
                "PartTerminologyID": part_terminology_id,
                "AttributeID": attr.attrib.get("AttributeID"),
                "AttributeUOM": attr.attrib.get("AttributeUOM", ""),
                "Value": attr.text
            })

    df = pd.DataFrame(product_attr_data)

    return df


if xml_file:

    with st.spinner("Parsing XML..."):

        df = parse_pies(xml_file)

    st.success("XML Parsed Successfully")

    st.subheader("Preview Data")

    st.dataframe(df, use_container_width=True)

    st.write(f"Total Records: {len(df)}")

    # Prepare Excel download
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="PIES_Data")

    st.download_button(
        label="Download Excel",
        data=output.getvalue(),
        file_name="PIES_Output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

else:
    st.info("Please upload a PIES XML file.")