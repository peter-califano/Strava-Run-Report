#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sql
import pandas as pd


# In[2]:


# Map pandas dtypes to SQLite types
dtype_mapping = {
    "int64": "INTEGER",
    "float64": "REAL",
    "object": "TEXT",
    "datetime64[ns]": "TEXT"  # Store datetime as TEXT in SQLite
}


def upsert_data(db_name: str, table_name: str, new_data: pd.DataFrame, unique_key: str = 'id'):
    """
    Initialize a table with the correct schema and upsert data into it.

    :param db_name: Name of the SQLite database file.
    :param table_name: Name of the table to create or update.
    :param new_data: DataFrame containing the data to upsert.
    :param unique_key: Column name to enforce uniqueness (e.g., primary key).
    """
    # Connect to the SQLite database
    conn = sql.connect(db_name)
    cursor = conn.cursor()

    # Construct CREATE TABLE query with schema
    sql_columns = []
    for column, dtype in new_data.dtypes.items():
        sql_type = dtype_mapping.get(str(dtype), "TEXT")  # Default to TEXT if type is unknown
        sql_columns.append(f"{column} {sql_type}")
    
    # Add UNIQUE constraint
    sql_columns.append(f"UNIQUE({unique_key})")
    columns_str_with_types = ",\n    ".join(sql_columns)
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (\n    {columns_str_with_types}\n);"
    cursor.execute(create_table_query)

    # Prepare column names and values for upserting
    columns_str = ", ".join(new_data.columns)  # Only column names
    values_str = ", ".join(["?" for _ in new_data.columns])  # Placeholder for values
    
    # Iterate through rows of new_data to insert or replace into the table
    for _, row in new_data.iterrows():
        upsert_query = f"""
        INSERT OR REPLACE INTO {table_name} ({columns_str})
        VALUES ({values_str});
        """
        cursor.execute(upsert_query, tuple(row))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


# In[3]:


strava_data = pd.read_csv('strava_data_processed.csv', index_col = 0)
upsert_data(db_name = 'strava_data.db', table_name =  "activities", new_data = strava_data, unique_key = 'id')


# In[4]:


conn = sql.connect("strava_data.db")
df = pd.read_sql_query("SELECT * FROM activities", conn)
print(df)
df.to_csv('database_read.csv')
conn.commit()
conn.close()

