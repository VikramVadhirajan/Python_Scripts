import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Load CSV file into DataFrame
<<<<<<< HEAD
csv_file_path = r"C:\06_Freelancing\Discussion\Chatbot\automotive_sku_data.csv"  # Replace with your CSV file path
=======
csv_file_path = r"D:\06_Freelancing\Discussion\Chatbot\automotive_sku_data.csv" # Replace with your CSV file path
>>>>>>> 40e1debd3d909a506705d4d22eaa4e7a1fa70643
df = pd.read_csv(csv_file_path)

# Connect to MySQL database
engine = create_engine('mysql+mysqlconnector://root:DViPa_2408@localhost:3306/Demonstration')  # Replace with your credentials

# Load DataFrame into MySQL
<<<<<<< HEAD
df.to_sql(name='autodata', con=engine, if_exists='replace', index=False)  # Replace with your table name
=======
df.to_sql(name='automotivedata', con=engine, if_exists='replace', index=False)  # Replace with your table name
>>>>>>> 40e1debd3d909a506705d4d22eaa4e7a1fa70643

print('Data loaded into MySQL database successfully.')