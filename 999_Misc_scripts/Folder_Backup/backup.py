#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shutil
from pathlib import Path
from tqdm import tqdm
from time import sleep
from IPython.display import clear_output
import os


# ## Targeting list of folders

# In[2]:

# paths = input("Enter folder paths separated by comma:\n")
paths=r"C:\01_LogicJunior,C:\02_Personal_Documents,C:\03_FBG_Work,C:\04_Udemy,C:\05_Simplilearn,C:\06_Freelancing,C:\07_Python_Projects,C:\08_Python_Scripts,C:\09_Power BI files,C:\10_SQL_Files,C:\11_Excel_Files,C:\12_Portfolio_Website,C:\13_Tableau,C:\14_Langchain,C:\15_Obsidian_Notes,C:\16_AWS_Bedrock"
Sources = [p.strip() for p in paths.split(",")]


# In[3]:


dest= Path(r"C:\99_CopyHDD")


# In[4]:


ignore_folders = ['.venv', '__pycache__', '.git', 'node_modules','images_from_videos']
ignore = shutil.ignore_patterns(ignore_folders)
ignore_keywords=["Frames"]
ignore_extensions = [".mov"]
# In[5]:


last_folder = None


# In[6]:


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


# In[9]:


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
    


# # ## Copy specific Items from the folder

# # In[18]:


# destination=Path(r"C:\99_CopyHDD\Ipynb_files")


# # In[19]:


# neededfileextension=".ipynb"


# # In[20]:


# for source in Sources:
#     source=Path(source)
#     items = list(source.rglob("*"))
#     Parent_Project=str(source).split("\\")[-1]
#     for item in tqdm(items, desc=f"Backing up files from {Parent_Project} total of \t \t : {directory_Size(source)}", unit="item", colour='green'):
#         # sleep(0.01)
        
#         if any(folder in item.parts for folder in ignore_folders):
#             continue
#         if item.suffix == neededfileextension:
#             relative_path = item.relative_to(source)
#             first_folder = relative_path.parts[0]

#             target = destination/Parent_Project/ item.relative_to(source)


#             if item.is_dir():
#                 target.mkdir(parents=True, exist_ok=True)

#             else:
#                 target.parent.mkdir(parents=True, exist_ok=True)
#                 shutil.copy2(item, target)
#                 # print("Copied:", item)
#                 # sleep(0.05)
#                 # clear_output(wait=True)
            
# print(f"Backup completed successfully! copied \t \t :{directory_Size(dest)} of Data")


os.startfile(dest)

