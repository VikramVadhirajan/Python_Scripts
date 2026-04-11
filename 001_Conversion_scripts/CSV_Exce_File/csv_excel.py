import streamlit as st
import pandas as pd
from io import BytesIO
import time

st.title("CSV → Excel Chunk Converter")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

chunk_size = st.number_input(
    "Chunk size per sheet (Max 1,000,000)",
    min_value=1,
    max_value=1_000_000,
    value=200_000
)

sheet_prefix = st.text_input(
    "Sheet name prefix",
    value="Sheet"
)


def count_rows(file):
    total = sum(1 for _ in file) - 1
    file.seek(0)
    return total


if uploaded_file:

    if st.button("Start Conversion"):

        st.write("Counting rows...")
        total_rows = count_rows(uploaded_file)

        st.success(f"Total rows: {total_rows:,}")

        progress_bar = st.progress(0)

        status_text = st.empty()
        timer_text = st.empty()

        start_time = time.time()

        rows_processed = 0
        sheet_num = 1

        output = BytesIO()

        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:

            for chunk in pd.read_csv(uploaded_file, chunksize=chunk_size):

                sheet_name = f"{sheet_prefix}_{sheet_num}"

                chunk.to_excel(
                    writer,
                    sheet_name=sheet_name,
                    index=False
                )

                rows_processed += len(chunk)
                sheet_num += 1

                progress = rows_processed / total_rows
                progress_bar.progress(progress)

                elapsed = time.time() - start_time

                rows_per_sec = rows_processed / elapsed if elapsed > 0 else 0

                remaining_rows = total_rows - rows_processed

                eta_seconds = remaining_rows / rows_per_sec if rows_per_sec > 0 else 0

                eta_minutes = int(eta_seconds // 60)
                eta_sec = int(eta_seconds % 60)

                status_text.markdown(
                    f"**Processed:** {rows_processed:,} / {total_rows:,}"
                )

                timer_text.markdown(
                    f"⏳ **Estimated Time Remaining:** {eta_minutes}m {eta_sec}s"
                )

        st.success("Conversion Completed!")

        st.download_button(
            "Download Excel",
            data=output.getvalue(),
            file_name="converted.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )