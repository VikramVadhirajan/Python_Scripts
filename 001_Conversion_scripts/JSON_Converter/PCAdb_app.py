import streamlit as st
import pandas as pd
import zipfile
import json
from io import BytesIO
import os

st.set_page_config(page_title="AutoCare PCA Converter", layout="wide")

st.title("AutoCare PCA Database → Excel Converter")

st.write("Upload the **AutoCare PCA ZIP file** to extract Attribute Details and Valid Values.")

uploaded_zip = st.file_uploader("Upload PCA ZIP File", type=["zip"])


def load_json_from_zip(zip_file):

    dataframes = {}

    with zipfile.ZipFile(zip_file, 'r') as z:
        for file_name in z.namelist():
            if file_name.endswith(".json"):

                with z.open(file_name) as f:
                    data = json.load(f)

                df = pd.json_normalize(data)
                key = os.path.splitext(os.path.basename(file_name))[0]
                dataframes[key] = df

    return dataframes


if uploaded_zip:

    with st.spinner("Processing PCA Database..."):

        dataframes = load_json_from_zip(uploaded_zip)

        df_PA = dataframes["PartAttributes"]
        df_PAA = dataframes["PartAttributeAssignment"]
        df_P = dataframes["Parts"]
        df_MUOM = dataframes["MetaUOMCodes"]
        df_MUOMA = dataframes["MetaUomCodeAssignment"]
        df_CM = dataframes["CodeMaster"]
        df_Cat = dataframes["Categories"]
        df_VVA = dataframes["ValidValueAssignment"]
        df_VV = dataframes["ValidValues"]

        # Valid Values Table
        df_ValidValues = (
            df_VV.merge(df_VVA, on="ValidValueID", how="left")
            .merge(df_PAA, on="PAPTID", how="outer")
            .merge(df_PA, on="PAID", how="outer")
            .merge(df_P, on="PartTerminologyID", how="outer")
        )

        df_ValidValues = df_ValidValues[df_ValidValues["ValidValue"].notna()]

        df_ValidValues = df_ValidValues[
            ["PartTerminologyName", "PAName", "ValidValue"]
        ]

        # Attribute Table
        df = (
            df_PAA.merge(df_P, on="PartTerminologyID", how="outer")
            .merge(df_PA, on="PAID", how="outer")
            .merge(df_MUOMA, on="PAPTID", how="outer")
            .merge(df_MUOM, left_on="MetaUomID", right_on="MetaUOMID", how="outer")
            .merge(df_CM, on="PartTerminologyID", how="outer")
            .merge(df_Cat, on="CategoryID", how="outer")
        )

        df_cleaned = df[
            [
                "CategoryID",
                "CategoryName",
                "PartTerminologyID",
                "PartTerminologyName",
                "PAID",
                "PAName",
            ]
        ].drop_duplicates()

        df_cleaned = df_cleaned[df_cleaned["CategoryName"].notna()]
        df_cleaned = df_cleaned[df_cleaned["PAName"].notna()]

    st.success("Processing Complete")

    st.subheader("Attribute Details Preview")
    st.dataframe(df_cleaned, use_container_width=True)

    st.subheader("Valid Values Preview")
    st.dataframe(df_ValidValues, use_container_width=True)

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df_cleaned.to_excel(writer, index=False, sheet_name="Attribute_Details")
        df_ValidValues.to_excel(writer, index=False, sheet_name="Valid_Values")

    st.download_button(
        label="Download Excel",
        data=output.getvalue(),
        file_name="Autocare_PCA_Output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )