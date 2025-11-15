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

---

## 📦 Repository Structure

```text
.
├── app.py                     # Main Streamlit dashboard
├── README.md                  # Project description (this file)
├── requirements.txt           # Dependencies
├── data/
│   └── life_rhythms_clean.csv
├── src/
│   └── preprocess.py          # Cleaning and transformation script
├── screenshots/
│   ├── heatmap.png
│   ├── line_comparison.png
│   ├── then_vs_now.png
│   └── composition.png
├── .streamlit/
│   └── config.toml            # Custom sage-green theme
└── report/
    └── report.pdf             # Final 3-page course report
