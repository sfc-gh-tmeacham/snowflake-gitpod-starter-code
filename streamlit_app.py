import os
import streamlit as st
import snowflake.connector  #upm package(snowflake-connector-python==2.7.0)
 
 
# Initialize connection, using st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    con = snowflake.connector.connect(
        user=os.getenv("SFUSER"),
        password=os.getenv("PASSWORD"),
        account=os.getenv("ACCOUNT"),
        role=os.getenv("ROLE"),
        warehouse=os.getenv("WAREHOUSE"),
    )
    return con
 
 
# Perform query, using st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
 
 
# rows = run_query("SHOW TABLES;")
conn = init_connection()
 
query = "CREATE OR REPLACE DATABASE EMPLOYEES;"
rows = run_query(query)
 
# Print results.
for row in rows:
    st.write(row)
