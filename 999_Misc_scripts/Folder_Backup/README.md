# Folder Content Backup Utility 📂💾

A Python automation tool that scans multiple directories, analyzes their contents, and backs up selected files to a target location.

This project is useful for developers and data professionals who maintain **multiple project folders** and want an automated way to **collect and back up important files such as Jupyter notebooks or scripts**.

---

# 📌 Project Overview

Managing many development folders across different learning platforms, projects, and tools can quickly become difficult.

This notebook provides a solution to:

* Scan multiple directories
* Identify files recursively
* Ignore unnecessary folders
* Track folder sizes
* Backup selected files to a central location

The tool is particularly useful for **backing up `.ipynb` files or other project assets** across several directories.

---

# 🚀 Key Features

✔ Scan multiple folders automatically
✔ Recursive directory traversal
✔ Backup selected file types
✔ Ignore unnecessary system folders
✔ Progress tracking using `tqdm`
✔ Folder size analysis

---

# 🧠 Workflow

The notebook performs the following steps.

---

## 1️⃣ Define Source Directories

Multiple directories are provided as sources to scan.

Example:

```python id="src_dirs"
Sources = [
"C:\\07_Python_Projects",
"C:\\08_Python_Scripts",
"C:\\09_Power BI files",
"C:\\10_SQL_Files",
"C:\\11_Excel_Files",
"C:\\12_Portfolio_Website"
]
```

These directories are recursively scanned.

---

# 2️⃣ Define Backup Destination

The destination folder stores the backup copies.

```python id="dest_dir"
dest = Path("destination path")
```

---

# 3️⃣ Ignore Unnecessary Folders and Files

Certain folders are skipped during scanning to avoid copying unnecessary files.

Examples include:

* `.venv`
* `__pycache__`
* `.git`
* `node_modules`

Example configuration:

```python id="ignore"
ignore_folders = ['.venv', '__pycache__', '.git']
```

```Skip specific large files like videos 
ignore_extensions = [".mov"]
```

---

# 4️⃣ Calculate Folder Size

Before copying files, the script calculates directory size to understand storage usage.

This helps track how much data is being processed.

---

# 5️⃣ Recursive Folder Scanning

The notebook scans folders using:

```python id="scan"
Path.rglob("*")
```

This allows discovery of **all nested files and directories**.

---

# 6️⃣ Progress Monitoring

The script uses **tqdm** to display progress bars during scanning and copying.

This helps monitor long-running operations.

---

# 7️⃣ File Filtering

The tool allows filtering specific file extensions.

Example:

```python id="ext_filter"
neededfileextension = ".ipynb"
```

This allows users to backup **only Jupyter notebooks or specific file types**.

---

# 📂 Project Structure

```
FolderContent_Backup/
│
├── backup.py
├── FolderContent_Backup.ipynb
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies Used

Python
Pathlib
OS module
Shutil
TQDM
Jupyter Notebook

---

# 🚀 How to Run

### Install dependencies

```
pip install -r requirements.txt
```

---

### Launch Jupyter Notebook

```
jupyter notebook
```

Open:

```
FolderContent_Backup.ipynb
```

Run the cells sequentially.

---

# 💡 Use Cases

This tool is useful for:

* Backing up development projects
* Collecting Jupyter notebooks across folders
* Managing large learning repositories
* Migrating projects to external storage
* Organizing datasets and scripts

---

# 🔮 Future Improvements

* Convert the notebook into a **Python CLI tool**
* Add **logging and backup reports**
* Support **cloud backups (Azure / Google Drive)**
* Add **file size filtering**
* Build a **Streamlit interface for visualization**

---

# 👨‍💻 Author

**Vikram Vadhirajan**

Data Analyst | Python | Machine Learning | Automation

GitHub
https://github.com/VikramVadhirajan

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐
