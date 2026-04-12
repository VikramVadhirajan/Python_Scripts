import streamlit as st
import pandas as pd
import zipfile
import json
from io import BytesIO

st.set_page_config(page_title="AutoCare VCdb Converter", layout="wide")

st.title("AutoCare VCdb → Excel Converter")

st.write("Upload the **AutoCare VCdb ZIP file** to generate the vehicle dataset.")

uploaded_zip = st.file_uploader("Upload VCdb ZIP", type=["zip"])


def load_json_files(zip_file):

    dataframes = {}

    with zipfile.ZipFile(zip_file, "r") as z:

        for file_name in z.namelist():

            if file_name.endswith(".json"):

                with z.open(file_name) as f:
                    data = json.load(f)

                df = pd.json_normalize(data)

                key = file_name.split("/")[-1].replace(".json", "")

                dataframes[key] = df

    return dataframes


def build_vehicle_dataset(dataframes):

    df = (
        dataframes['BaseVehicle']
        .merge(dataframes['Vehicle'],how='outer')
        .merge(dataframes['Make'],how='outer')
        .merge(dataframes['Model'],how='outer')
        .merge(dataframes['VehicleType'],on='VehicleTypeID',how='outer')
        .merge(dataframes['VehicleToEngineConfig'],on='VehicleID',how='outer')
        .merge(dataframes['EngineConfig'],on='EngineConfigID',how='outer')
        .merge(dataframes['Valves'],on='ValvesID',how='outer')
        .merge(dataframes['Aspiration'],on='AspirationID',how='outer')
        .merge(dataframes['EngineDesignation'],on='EngineDesignationID',how='outer')
        .merge(dataframes['EngineVIN'],on='EngineVINID',how='outer')
        .merge(dataframes['VehicleToDriveType'],on='VehicleID',how='outer')
        .merge(dataframes['DriveType'],on='DriveTypeID',how='outer')
        .merge(dataframes['EngineBase'],on='EngineBaseID',how='outer')
        .merge(dataframes['FuelType'],on='FuelTypeID',how='outer')
        .merge(dataframes['VehicleToBrakeConfig'],on='VehicleID',how='outer',suffixes=('_VehicleToBrakeConfig','_VehicleToBrakeConfig2'))
        .merge(dataframes['BrakeConfig'],on='BrakeConfigID',how='outer')
        .merge(dataframes['BrakeSystem'],on='BrakeSystemID',how='outer')
        .merge(dataframes['Region'],on='RegionID',how='outer')
        .merge(dataframes['VehicleToClass'],on='VehicleID',how='outer',suffixes=('_VehicleToClass','_VehicleToClass2'))
        .merge(dataframes['Class'],on='ClassID',how='outer')
        .merge(dataframes['VehicleToWheelbase'],on='VehicleID',how='outer',suffixes=('_VehicleToWheelbase','_VehicleToWheelbase2'))
        .merge(dataframes['WheelBase'],left_on='WheelbaseID',right_on='WheelBaseID',how='outer')
        .merge(dataframes['VehicleToBodyStyleConfig'],on='VehicleID',how='outer',suffixes=('VehicleToBodyStyleConfig','VehicleToBodyStyleConfig2'))
        .merge(dataframes['BodyStyleConfig'],on='BodyStyleConfigID',how='outer')
        .merge(dataframes['BodyType'],on='BodyTypeID',how='outer')
        .merge(dataframes['EngineVersion'],on='EngineVersionID',how='outer')
    )

    df_all = df[
        ['BaseVehicleID',"VehicleTypeName", 'YearID','MakeName','ModelName','BlockType', 'Cylinders','Liter','ValvesPerEngine','CC','CID','FuelTypeName','AspirationName','EngineDesignationName','EngineVINName','DriveTypeName','RegionAbbr','BodyTypeName','WheelbaseID','WheelBase','WheelBaseMetric','EngineVersion','BrakeSystemName']
    ]

    df_all = df_all.drop_duplicates().reset_index(drop=True)

    return df_all

@st.cache_data
def build_dataset(uploaded_zip):
    dataframes = load_json_files(uploaded_zip)
    df_result = build_vehicle_dataset(dataframes)
    return df_result

@st.cache_data
def convert_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")


@st.cache_data
def convert_to_excel(df):
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer

if uploaded_zip:

    with st.spinner("Processing VCdb..."):

        df_result = build_dataset(uploaded_zip)

    st.success("Processing Complete")

    st.subheader("Vehicle Dataset Preview")

    st.dataframe(df_result, use_container_width=True)

    st.write("Total Records:", len(df_result))

    st.subheader("Download Data")

    file_type = st.radio(
            "Download format",
            ["CSV (recommended ⚡)", "Excel"]
            )

    if file_type.startswith("CSV"):
        data = convert_to_csv(df_result)
        file_name = "VCdb_output.csv"

    else:
        data = convert_to_excel(df_result)
        file_name = "VCdb_output.xlsx"

    downloaded = st.download_button(
        "Download file",
        data=data,
        file_name=file_name
    )

    if downloaded:
        st.success("✅ File Downloadeed successfully.")
    

else:
    st.info("Upload the VCdb ZIP file to begin.")