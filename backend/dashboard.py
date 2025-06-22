import streamlit as st
import pandas as pd
import sqlite3
import time

st.set_page_config(page_title="SafeWalk Dashboard", layout="wide")

st.title("🚨 SafeWalk SOS Dashboard")

conn = sqlite3.connect("instance/alerts.db")
query = "SELECT * FROM Alert ORDER BY timestamp DESC"
df = pd.read_sql_query(query, conn)
conn.close()

if df.empty:
    st.warning("No alerts found.")
else:
    st.subheader("📍 SOS Alert Map")
    st.map(df[["lat", "lon"]])

    st.subheader("🗂️ Alert Details")
    df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d %H:%M:%S")
    st.dataframe(df[["id", "name", "contact", "status", "timestamp", "notes"]])

    if st.button("🔄 Refresh"):
        st.experimental_rerun()
