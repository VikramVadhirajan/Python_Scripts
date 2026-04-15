# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: 08-python-scripts (3.11.15)
#     language: python
#     name: python3
# ---

# %%
from pathlib import Path
from time import sleep
from IPython.display import clear_output
import os
from tqdm import tqdm
import shutil

# %% [markdown]
# ### Targeting list of folders

# %%
Sources=[
r"C:\01_LogicJunior",
r"C:\02_Personal_Documents",
r"C:\03_FBG_Work",
r"C:\04_Udemy",
r"C:\05_Simplilearn",
r"C:\06_Freelancing",
r"C:\07_Python_Projects",
r"C:\08_Python_Scripts",
r"C:\09_Power BI files",
r"C:\10_SQL_Files",
r"C:\11_Excel_Files",
r"C:\12_Portfolio_Website",
r"C:\13_Tableau",
r"C:\14_Langchain"]


# %%
# paths=r"C:\01_LogicJunior,C:\02_Personal_Documents,C:\03_FBG_Work,C:\04_Udemy,C:\05_Simplilearn,C:\06_Freelancing,C:\07_Python_Projects,C:\08_Python_Scripts,C:\09_Power BI files,C:\10_SQL_Files,C:\11_Excel_Files,C:\12_Portfolio_Website,C:\13_Tableau,C:\14_Langchain"
# paths = input("Enter folder paths separated by comma:\n")
# Sources = [p.strip() for p in paths.split(",")]

# %%
dest= Path(r"C:\99_CopyHDD")

# %% [markdown]
# ### Ignoring List of folders

# %%
ignore_folders = ['.venv', '__pycache__', '.git', 'node_modules',"images_from_videos"]
ignore = shutil.ignore_patterns(ignore_folders)
ignore_keywords=["Frames"]

# %% [markdown]
# ### Ignoring large files such as videos

# %%
ignore_extensions = [".mov"]

# %%
last_folder = None


# %%
def directory_Size(directory):
    totalsize=0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                totalsize+=size
            except Exception:
                pass
    for unit in ["B","KB","MB","GB","TB"]:
        if totalsize < 1024:
            return f"{totalsize:.2f} {unit}"
        totalsize /= 1024
    return totalsize


# %%
source=Path(Sources[5])
items = list(source.rglob("*"))
list(items[5].parts) 

# %%
for source in Sources:
    source=Path(source)
    items = list(source.rglob("*"))
    Parent_Project=str(source).split("\\")[-1]
    for item in tqdm(items, desc=f"Backing up files from {Parent_Project} total of \t \t : {directory_Size(source)}", unit="item", colour='green'):
        # sleep(0.01)
        
        if any(folder in item.parts for folder in ignore_folders):
            continue
        if item.suffix in ignore_extensions:
            continue    
        if any(keyword in part for part in item.parts for keyword in ignore_keywords):
            continue
        relative_path = item.relative_to(source)
        first_folder = relative_path.parts[0]

        target = dest/Parent_Project / item.relative_to(source)


        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)

        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
            # print("Copied:", item)
            # sleep(0.05)
            # clear_output(wait=True)
                
print(f"Backup completed successfully! copied \t \t :{directory_Size(dest)} of Data")


# %% [markdown]
# ### Copy specific Items from the folder

# %%
destination=Path(r"C:\99_CopyHDD\Ipynb_files")

# %%
neededfileextension=".ipynb"

# %%
for source in Sources:
    source=Path(source)
    items = list(source.rglob("*"))
    Parent_Project=str(source).split("\\")[-1]
    for item in tqdm(items, desc=f"Backing up files from {Parent_Project} total of \t \t : {directory_Size(source)}", unit="item", colour='green'):
        # sleep(0.01)
        
        if any(folder in item.parts for folder in ignore_folders):
            continue
        if item.suffix == neededfileextension:
            relative_path = item.relative_to(source)
            first_folder = relative_path.parts[0]

            target = destination/Parent_Project/ item.relative_to(source)


            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)

            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target)
                # print("Copied:", item)
                # sleep(0.05)
                # clear_output(wait=True)
            
print(f"Backup completed successfully! copied \t \t :{directory_Size(dest)} of Data")
# %%
print("Jupytext sync test")
