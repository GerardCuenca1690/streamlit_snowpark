import streamlit as st

# Initialize connection.
conn = st.experimental_connection('snowpark')

# Perform query.
df = conn.query("SELECT * FROM "UEFA_PROD_DATAIKU"."MKT"."RFM_ANALYSIS_202303_OPTINS" WHERE "MACRO_THRESHOLD_MS" ='Active' LIMIT 5", ttl=300)

# Print results.
for row in df.itertuples():
    st.write(f"{row.ID} has a :{row.OPT_IN_MS}:")
