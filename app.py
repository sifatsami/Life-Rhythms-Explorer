import pandas as pd
import altair as alt
import streamlit as st

alt.data_transformers.disable_max_rows()

df = pd.read_csv("life_rhythms_clean.csv")
df["hour_bin"] = df["hour"].astype(int)

st.title("Life Rhythms in Europe")

st.write("""
This dashboard visualizes daily activity patterns across selected European countries using
10-minute interval time-use survey data from 2000 and 2010.

Use the filters in the sidebar to explore:
- How activities vary over the 24-hour day
- How countries differ for a given activity
- How patterns changed between 2000 and 2010
- What people are doing at a specific hour
""")

st.markdown("---")

st.sidebar.header("Filters")

country = st.sidebar.selectbox("Country", sorted(df["country"].unique()))
year = st.sidebar.selectbox("Year", sorted(df["year"].unique()))
activity = st.sidebar.selectbox("Activity", sorted(df["activity_group"].unique()))
hour_selected = st.sidebar.slider("Hour of day", 0, 23, 8)

st.header("Daily Activity Rhythm")

st.write(
    "This heatmap shows the percentage of people engaged in each activity across the day "
    f"for **{country}** in **{year}**."
)

heatmap_data = df[(df["country"] == country) & (df["year"] == year)]

heatmap = (
    alt.Chart(heatmap_data)
    .mark_rect()
    .encode(
        x=alt.X("hour:Q", bin=alt.Bin(maxbins=48), title="Hour of day"),
        y=alt.Y("activity_group:N", title="Activity"),
        color=alt.Color(
            "value:Q",
            title="Participation (%)",
            scale=alt.Scale(scheme="viridis")
        ),
        tooltip=[
            alt.Tooltip("activity_group:N", title="Activity"),
            alt.Tooltip("time_label:N", title="Time interval"),
            alt.Tooltip("value:Q", title="Participation (%)", format=".2f")
        ]
    )
    .properties(
        width=700,
        height=280,
        title=f"Daily Rhythm – {country} ({year})"
    )
)

st.altair_chart(heatmap, use_container_width=True)

st.markdown("---")

st.header("Country Comparison for Selected Activity")

st.write(
    f"This line chart compares how different countries engage in **{activity}** across the day "
    f"in **{year}**."
)

line_data = df[(df["activity_group"] == activity) & (df["year"] == year)]

line_chart = (
    alt.Chart(line_data)
    .mark_line()
    .encode(
        x=alt.X("hour:Q", title="Hour of day"),
        y=alt.Y("value:Q", title="Participation (%)"),
        color=alt.Color(
            "country:N",
            title="Country",
            scale=alt.Scale(scheme="tableau10")
        ),
        tooltip=[
            alt.Tooltip("country:N", title="Country"),
            alt.Tooltip("time_label:N", title="Time interval"),
            alt.Tooltip("value:Q", title="Participation (%)", format=".2f")
        ]
    )
    .properties(
        width=700,
        height=320,
        title=f"{activity} – All Countries ({year})"
    )
)

st.altair_chart(line_chart, use_container_width=True)

st.markdown("---")

st.header("Change Over Time: 2000 vs 2010")

st.write(
    f"This view compares **{activity}** in **{country}** between 2000 and 2010, "
    "showing how the daily pattern has shifted over time."
)

tn_data = df[(df["country"] == country) & (df["activity_group"] == activity)]

tn_chart = (
    alt.Chart(tn_data)
    .mark_line()
    .encode(
        x=alt.X("hour:Q", title="Hour of day"),
        y=alt.Y("value:Q", title="Participation (%)"),
        color=alt.Color(
            "year:N",
            title="Year",
            scale=alt.Scale(scheme="set1")
        ),
        tooltip=[
            alt.Tooltip("year:N", title="Year"),
            alt.Tooltip("time_label:N", title="Time interval"),
            alt.Tooltip("value:Q", title="Participation (%)", format=".2f")
        ]
    )
    .properties(
        width=700,
        height=320,
        title=f"2000 vs 2010 — {activity} in {country}"
    )
)

st.altair_chart(tn_chart, use_container_width=True)

st.markdown("---")

st.header("Activity Composition at Selected Hour")

st.write(
    f"This chart shows how activities are distributed across countries at **{hour_selected}:00** "
    f"in **{year}**. Bars are normalized to show relative shares."
)

comp_data = df[(df["year"] == year) & (df["hour_bin"] == hour_selected)]

comp_chart = (
    alt.Chart(comp_data)
    .mark_bar()
    .encode(
        x=alt.X("sum(value):Q", stack="normalize", title="Share of participation"),
        y=alt.Y("country:N", title="Country"),
        color=alt.Color(
            "activity_group:N",
            title="Activity group",
            scale=alt.Scale(scheme="category20")
        ),
        tooltip=[
            alt.Tooltip("country:N", title="Country"),
            alt.Tooltip("activity_group:N", title="Activity"),
            alt.Tooltip("sum(value):Q", title="Participation (%)", format=".2f")
        ]
    )
    .properties(
        width=700,
        height=320,
        title=f"Activity Composition at {hour_selected:02d}:00 ({year})"
    )
)

st.altair_chart(comp_chart, use_container_width=True)

st.markdown("---")

st.markdown("""
**About the data:**  
Data source: Eurostat Harmonised European Time Use Survey (`TUS_00STARTIME`).  
Values represent the *participation rate (%)* — the share of people engaged in a given activity 
during each 10-minute interval.

---
*Visualization project – Life Rhythms in Europe*
""")


## cd "/Users/admin/Desktop/Projects/Visualization final project"      eita location basically,
## streamlit run app.py
## terminal e ei 2 line paste korle open hoibo dashboard