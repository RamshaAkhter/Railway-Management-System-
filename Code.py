import pandas as pd
import sqlite3

#Providing the paths
csv_path1 = r'C:\Users\sashi\OneDrive\Documents\Sisira_Ramsha\booked.csv'
csv_path2 = r'C:\Users\sashi\OneDrive\Documents\Sisira_Ramsha\Passenger.csv'
csv_path3 = r'C:\Users\sashi\OneDrive\Documents\Sisira_Ramsha\Train.csv'
csv_path4 = r'C:\Users\sashi\OneDrive\Documents\Sisira_Ramsha\Train_status.csv'

# Read CSV Files
df1 = pd.read_csv(csv_path1)
df2 = pd.read_csv(csv_path2)
df3 = pd.read_csv(csv_path3)
df4 = pd.read_csv(csv_path4)

# Create SQLite Database Connection
conn = sqlite3.connect(r'C:\Users\sashi\OneDrive\Documents\Sisira_Ramsha\RRS.db')

df1.head()

# Write DataFrames to Database
df1.to_sql('table1', conn, index=False, if_exists='replace')
df2.to_sql('table2', conn, index=False, if_exists='replace')
df3.to_sql('table3', conn, index=False, if_exists='replace')
df4.to_sql('table4', conn, index=False, if_exists='replace')
# Commit and Close Connection
conn.commit()
conn.close()
