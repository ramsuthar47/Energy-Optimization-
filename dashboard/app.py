import streamlit as st
import pandas as pd
import plotly.express as px

DATA_PATH = "data/processed/energy_hourly.csv"

st.title("AI Energy Optimization System")

st.write("Household Energy Consumption Analysis")

df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
df = df.set_index("timestamp")

st.subheader("Energy Consumption Over Time")

fig = px.line(df, y="Global_active_power")
st.plotly_chart(fig)

df["hour"] = df.index.hour
hourly_usage = df.groupby("hour")["Global_active_power"].mean()

st.subheader("Average Energy Usage by Hour")

fig2 = px.bar(hourly_usage)
st.plotly_chart(fig2)

peak_hour = hourly_usage.idxmax()

st.subheader("Peak Usage Hour")

st.write(f"Highest energy usage occurs at **{peak_hour}:00**")

off_peak_hour = hourly_usage.idxmin()

st.subheader("Optimization Recommendation")

st.write(
    f"Run high energy appliances after **{off_peak_hour}:00** instead of **{peak_hour}:00**"
)