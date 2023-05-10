"""
setup.py
Zayn Anderson Severance
05/09/2023
Imports all the data to the SQLite database.
"""

import pandas as pd
import numpy as np
import sqlite3

# Import csv
data = pd.read_csv('example_batch_records.csv', header=None, delimiter=',', na_filter='NULL')
# Format csv for SQL's NULL formatting
data = data.replace(np.nan, 'NULL')
# Format data for easier insertion
data = data[[0, 1, 2]]

try:
    with sqlite3.connect('batch_records') as con:
        cur = con.cursor
        con.execute("DROP TABLE IF EXISTS BatchRecords;")
        con.execute("""CREATE TABLE BatchRecords(
        batch_number INTEGER PRIMARY KEY,
        submitted_at DATETIME,
        nodes_used INTEGER)""")
        for index, d in data.iterrows():
            com = f"""INSERT INTO BatchRecords VALUES ({d[0]}, {f"'{d[1]}'" if d[1] != 'NULL' else d[1]}, {d[2]})"""
            print(com)
            con.execute(com)
except Exception as e:
    print(e)