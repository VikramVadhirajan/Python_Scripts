import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Directory Explorer", layout="wide")
st.title("📁 Directory Disk Usage Explorer")

# ── Helper functions ──────────────────────────────────────────────────────────
def format_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


def scan_directory(directory):
    records = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                records.append({"path": file_path, "size": size})
            except Exception:
                pass
    return pd.DataFrame(records)


def build_plot_df(df, directory):
    df["file_size_readable"] = df["size"].apply(format_size)

    df["file_type"] = df["path"].apply(lambda x: os.path.splitext(x)[1].lower())
    df["file_type"] = df["file_type"].replace("", "no_extension")

    df["relative_path"] = df["path"].apply(lambda x: os.path.relpath(x, directory))
    df["folder"] = df["relative_path"].apply(lambda x: os.path.dirname(x))

    folder_sizes = df.groupby("folder")["size"].sum().reset_index()
    folder_sizes["folder_size_readable"] = folder_sizes["size"].apply(format_size)
    df = df.merge(folder_sizes, on="folder", how="left", suffixes=("", "_folder"))

    df["path_parts"] = df["relative_path"].apply(lambda x: x.split(os.sep))
    max_depth = df["path_parts"].apply(len).max()
    df["path_parts_padded"] = df["path_parts"].apply(
        lambda parts: parts + [None] * (max_depth - len(parts))
    )

    path_df = pd.DataFrame(df["path_parts_padded"].tolist())
    path_df = path_df.dropna(axis=1, how="all")

    df_plot = pd.concat([df.reset_index(drop=True), path_df], axis=1)
    path_cols = list(path_df.columns)

    for col in path_cols:
        df_plot[col] = df_plot[col].replace("", None)

    path_cols = [c for c in path_cols if df_plot[c].notna().any()]
    df_plot = df_plot.drop_duplicates(subset=path_cols, keep="last").reset_index(drop=True)

    return df_plot, path_cols


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")
    directory = st.text_input(
        "Directory path",
        value=r"C:\07_Python_Projects"
    )

    st.markdown("**Exclude folders** (one per line)")
    exclude_input = st.text_area("", value="venv\n.git\n__pycache__\nnode_modules")
    exclude_patterns = [p.strip() for p in exclude_input.splitlines() if p.strip()]

    scan_btn = st.button("🔍 Scan", use_container_width=True)

# ── Default state ─────────────────────────────────────────────────────────────
if not scan_btn:
    st.info("👈 Enter a directory path in the sidebar and click **Scan** to begin.")
    st.stop()

# ── Scan ──────────────────────────────────────────────────────────────────────
if not os.path.isdir(directory):
    st.error(f"Directory not found: `{directory}`")
    st.stop()

with st.spinner("Scanning directory..."):
    df = scan_directory(directory)

if df.empty:
    st.warning("No files found in that directory.")
    st.stop()

for pattern in exclude_patterns:
    df = df[~df["path"].str.contains(pattern, na=False)].reset_index(drop=True)

if df.empty:
    st.warning("All files were excluded by your filters.")
    st.stop()

total_files = len(df)
total_size = df["size"].sum()

with st.spinner("Building treemap..."):
    try:
        df_plot, path_cols = build_plot_df(df, directory)
    except Exception as e:
        st.error(f"Error building plot: {e}")
        st.stop()

# ── Metrics ───────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Total Files", f"{total_files:,}")
col2.metric("Total Size", format_size(total_size))
col3.metric("Tree Depth", len(path_cols))

st.divider()

# ── Treemap ───────────────────────────────────────────────────────────────────
st.subheader("🗺️ Treemap")

try:
    fig = px.treemap(
        df_plot,
        path=path_cols,
        values="size",
        color="file_type",
        custom_data=["file_size_readable", "folder_size_readable"],
    )
    fig.update_traces(
        texttemplate="<b>%{label}</b><br>%{value:,.0f} B",
        hovertemplate=(
            "File Size: %{customdata[0]}<br>"
            "Folder Size: %{customdata[1]}"
            "<extra></extra>"
        ),
    )
    fig.update_layout(margin=dict(t=10, l=10, r=10, b=10), height=600)
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"Treemap error: {e}")

col1, col2 = st.columns([2,1])

with col1:

    # ── Top 10 largest files ──────────────────────────────────────────────────────
    st.subheader("🔝 Top 10 Largest Files")
    top10 = (
        df[["path", "size", "file_size_readable", "file_type"]]
        .nlargest(10, "size")
        .reset_index(drop=True)
    )
    top10.index += 1
    st.dataframe(top10, use_container_width=True)


with col2:
    # ── File type breakdown ───────────────────────────────────────────────────────
    st.subheader("📊 Size by File Type")
    type_summary = (
        df.groupby("file_type")["size"]
        .sum()
        .reset_index()
        .sort_values("size", ascending=True)
    )
    type_summary["readable"] = type_summary["size"].apply(format_size)

    bar = px.bar(
        type_summary.head(20),
        y="file_type",
        x="size",
        text="readable",
        labels={"size": "Total Size (bytes)", "file_type": "File Type"},
    )
    bar.update_traces(textposition="outside")
    bar.update_layout(margin=dict(t=20, l=10, r=10, b=40), height=400)
    st.plotly_chart(bar, use_container_width=True)

st.divider()