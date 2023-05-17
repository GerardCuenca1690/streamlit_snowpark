import os
import snowflake.connector
import streamlit as st

# Retrieve Snowflake connection details from environment variables
account = os.getenv("SNOWFLAKE_ACCOUNT")
user = os.getenv("SNOWFLAKE_USER")
password = os.getenv("SNOWFLAKE_PASSWORD")
database = os.getenv("SNOWFLAKE_DATABASE")
warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")

# Establish connection
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database
)

# Create a cursor to execute queries
cursor = conn.cursor()

# Perform query
query = 'SELECT * FROM "UEFA_PROD_DATAIKU"."MKT"."RFM_ANALYSIS_202303_OPTINS" WHERE "MACRO_THRESHOLD_MS" = \'Active\' LIMIT 5'
cursor.execute(query)

# Fetch and print results
for row in cursor:
    st.write(f"{row[0]} has a :{row[1]}:")

# Close the cursor and connection
cursor.close()
