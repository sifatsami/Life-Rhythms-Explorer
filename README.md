# Life Rhythms Explorer

**Interactive visualization of daily activity patterns across Europe**  
Built with **Streamlit** and **Altair**, using 10-minute interval time-use survey data from Eurostat.

This project was developed as the final assignment for a university Visualization course.  
It transforms complex temporal activity data into an intuitive dashboard for comparing countries, exploring cultural routines, and analyzing changes over time.

---

## 🌍 Project Overview

Daily human activity follows rhythmic patterns—sleeping, working, eating, commuting, leisure—and these rhythms differ across countries and evolve across decades.

This project is driven by four guiding questions:

1. **How do daily rhythms differ between European countries?**  
2. **How did these rhythms change from 2000 to 2010?**  
3. **Which activities dominate specific hours of the day?**  
4. **When are countries synchronized or divergent in their behavior?**

The result is an interactive, coordinated visualization system that allows users to explore Europe's daily routines.
![alt text](https://github.com/sifatsami/Life-Rhythms-Explorer/blob/main/Intro.png?raw=true)

---

## 🧠 Dataset

**Source:**  
Eurostat – Harmonised European Time Use Survey (HETUS)  
Table: `TUS_00STARTIME`

The dataset includes:

- **Participation rate (%)** for each activity  
- **Time of day** in 10-minute intervals  
- **Activity categories**, later grouped into broader categories  
- **Countries in Europe**  
- **Years:** 2000 and 2010  

The cleaned dataset used by the app:

`data/life_rhythms_clean.csv`

### Preprocessing (in `src/preprocess.py`)

- Filtered rows to `sex = Total`  
- Removed aggregate rows such as `Total`  
- Parsed textual time intervals into numerical:
  - `hour`  
  - `minutes_since_midnight`  
  - `hour_bin`  
- Grouped detailed activities into `activity_group`:
  - Work & Study  
  - Eating  
  - Personal Care & Sleep  
  - Household & Family Care  
  - Leisure  
  - TV & Video  
  - Travel / Commute  
  - Other  
- Saved the cleaned dataset for visualization

---

## 📊 Visualization System

The dashboard is implemented in **Streamlit** with **Altair** and uses a coordinated multiple-view layout.  
Users interact with filters (country, year, activity, hour) via a sidebar.

The four main views are:

---

### 1. Daily Rhythm Heatmap

Shows how activities are distributed across the 24 hours for a selected country and year.

![Daily Rhythm Heatmap](https://github.com/sifatsami/Life-Rhythms-Explorer/blob/main/Daily%20Activity%20Rhythm.png?raw=true)

---

### 2. Multi-Country Activity Comparison

Compares a selected activity across all countries in a selected year.

![Activity Comparison](https://github.com/sifatsami/Life-Rhythms-Explorer/blob/main/Country%20Comparison.png?raw=true)

---

### 3. Then vs Now (2000 vs 2010)

Shows how a specific country’s activity changed over time.

![Then vs Now](screenshots/then_vs_now.png)

---

### 4. Activity Composition at a Selected Hour

Displays which activities dominate a given hour across countries.

![Composition View](screenshots/composition.png)

---

## 🚀 Running the App

### Install dependencies:

```
pip install -r requirements.txt
```

Minimal requirements:

```
streamlit
altair
pandas
vega_datasets
```

### Run Streamlit:

```
streamlit run app.py
```

The app will open at:

```
http://localhost:8501
```
