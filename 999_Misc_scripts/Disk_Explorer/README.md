# Disk Explorer 📂💾

A Python utility that analyzes directory structures and visualizes **disk usage across folders and files**.

This tool helps identify **large directories, storage-heavy files, and space consumption patterns** within a file system.

It is especially useful for developers and data professionals who want to **clean up disk space or understand folder size distribution**.

---

# 📌 Project Overview

The **Disk Explorer** script scans a directory recursively and calculates the size of folders and files.

It then prepares the data so that it can be visualized to better understand **which directories are consuming the most storage**.

This project demonstrates how Python can be used for:

* File system exploration
* Disk usage analysis
* Directory size computation
* Data visualization of folder hierarchies

---

# 🚀 Features

* Scan directories recursively
* Calculate file and folder sizes
* Identify large folders
* Visualize disk usage hierarchy
* Help clean up unused storage

---

# ⚙️ Technologies Used

Python
Pandas
Plotly (for visualization)
OS module (filesystem operations)

---

# 🧱 How It Works

The script follows these steps:

1. Traverse the selected directory
2. Collect file and folder paths
3. Compute sizes for each file
4. Aggregate sizes for parent directories
5. Store results in a DataFrame
6. Visualize folder hierarchy using a treemap chart

---

# 📂 Repository Structure

```id="hw7hq6"
Disk_Explorer/
│
├── Disk_Folder_Explorer.ipynb
├── disk_explorer.py
├── requirements.txt
└── README.md
```

---

# 🚀 How to Run

### Clone the repository

```id="3wb6db"
git clone https://github.com/VikramVadhirajan/Python_Scripts.git
```

Navigate to the script directory

```id="wjpajb"
cd Python_Scripts/999_Misc_scripts/Disk_Explorer
```

Install dependencies

```id="i9b0ti"
pip install -r requirements.txt
```

Run the script

```id="pzw5ss"
python disk_explorer.py
```

---

# 📊 Output

The tool generates a **visual representation of disk usage**, helping you quickly identify:

* Large directories
* Storage-heavy files
* Space distribution across folders

---

# 💡 Use Cases

* Cleaning up storage
* Understanding project folder sizes
* Managing large datasets
* Disk usage analysis for development environments

---

# 🔮 Future Improvements

* Add GUI interface
* Allow filtering by file type
* Export disk usage reports
* Integrate with Streamlit dashboard

---

# 👨‍💻 Author

**Vikram Vadhirajan**

Data Analyst | Python | Machine Learning | Power BI

GitHub
https://github.com/VikramVadhirajan

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐
