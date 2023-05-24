import os
import snowflake.connector
import streamlit as st

conn = st.experimental_connection('snowpark')


df = conn.query('SELECT * FROM "UEFA_PROD_DATAIKU"."MKT"."RFM_ANALYSIS_202303_OPTINS" LIMIT 5', ttl=600)
# Perform query

cursor.execute(query)

    
for row in df.itertuples():
    st.write(f"{row[0]} has a :{row[1]}:")

