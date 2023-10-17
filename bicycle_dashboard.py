import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

def create_daily_sharing_df(days_df):
    daily_sharing_df = days_df.resample(rule="M", on="date").agg({
        "bicycle_total": "sum",
        "user": "sum",
        "user_registered": "sum"
    })
    daily_sharing_df.index = daily_sharing_df.index.strftime('%B %Y')
    daily_sharing_df = daily_sharing_df.reset_index()
    return daily_sharing_df

def create_season_total_df(days_df):
    season_total_df = days_df.groupby("season").bicycle_total.sum().sort_values(ascending=False).reset_index()
    return season_total_df


# Load cleaned data
days_df = pd.read_csv("days.csv")

days_df["date"] = pd.to_datetime(days_df["date"])
days_df.sort_values(by="date", inplace=True)
days_df.reset_index(inplace=True)


# # Menyiapkan berbagai dataframe
daily_sharing_df = create_daily_sharing_df(days_df)
season_total_df = create_season_total_df(days_df)

# visualisasi
st.header('Bicycle Sharing Dashboard :sparkles:')
st.subheader('Monthly Sharing')

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_sharing_df["date"],
    daily_sharing_df["bicycle_total"],
    marker='o', 
    linewidth=2,
    color="#FFA500"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', rotation = 65, labelsize=15)

st.pyplot(fig)


fig, ax = plt.subplots(figsize=(20, 10))

colors = ["#e0360b", "#f7e6e7", "#f7e6e7", "#f7e6e7"]

sns.barplot(
    x="bicycle_total", 
    y="season",
    data=season_total_df.sort_values(by="bicycle_total", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Number of Sharing by Season", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

st.caption('Copyright Muhammad Rivaldi 2023')
