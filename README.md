# Earthquake ETL Pipeline (USGS API)

End-to-end ETL pipeline built with Python that extracts real earthquake data from the USGS public API, performs data validation and transformation, and prepares an analysis-ready dataset with severity classification.

This project demonstrates a complete data analyst workflow: API extraction, data quality checks, transformation, exploratory analysis, and business-oriented categorization.

---

## 🚀 Project Overview

The goal of this project is to simulate a real-world analytics pipeline by working with live earthquake data.  
The pipeline follows standard ETL practices:

1. **Extract** data from a public API (USGS Earthquake API)
2. **Validate** data quality (nulls, duplicates, data types)
3. **Transform** raw data into a clean, analysis-ready format
4. **Analyze** patterns using exploratory data analysis (EDA)
5. **Classify** events by severity to make the data more actionable

---

## 🛠️ Tech Stack

- **Python**
- **pandas** – data manipulation and analysis
- **requests** – API data extraction
- **Jupyter Notebook** – validation, transformation, and EDA
- **Git & GitHub** – version control and portfolio hosting

(Optional / Conceptual)
- **OpenAI API** – AI-assisted analytical insights (not required to run the pipeline)

---

## 🔄 Pipeline Flow
USGS API
↓
Extract (Python script)
↓
Raw CSV (data/raw)
↓
Validation & Transformation (Jupyter)
↓
Processed CSV (analysis-ready)
↓
EDA + Severity Classification

## 📁 Project Structure

earthquake-etl-pipeline/
├── extract/
│ └── extract_earthquakes.py
├── notebooks/
│ └── test.ipynb
├── .gitignore
├── requirements.txt
└── README.md

**Note:**  
Raw and processed data files are intentionally excluded from the repository to keep it lightweight and reproducible.

---

## 📥 Data Source

- **USGS Earthquake API**
- Provides real-time and historical earthquake data in GeoJSON format
- Official source: https://earthquake.usgs.gov/

---

## ✅ Data Validation

The following quality checks were performed:

- Dataset dimensions (`shape`)
- Data types (`dtypes`)
- Missing values analysis
- Duplicate row and ID checks
- Timestamp range validation

These checks ensure the dataset is reliable before analysis and transformation.

---

## 🔧 Data Transformation

Key transformation steps include:

- Removing events with missing magnitude
- Converting timestamps to UTC datetime format
- Selecting only relevant analytical columns
- Feature engineering:
  - `event_date` – calendar date of the event
  - `event_hour` – hour of occurrence (0–23)

The result is a clean dataset ready for analysis or visualization.

---

## 📊 Exploratory Data Analysis (EDA)

Basic EDA was performed to understand:

- Distribution of earthquake magnitudes
- Frequency of events over time
- Most active geographic locations
- Count and distribution of strong earthquakes (magnitude ≥ 5)

Known seismic hotspots such as **The Geysers, CA** and regions in **Alaska** were identified, validating the realism of the data.

---

## ⚠️ Earthquake Severity Classification

To make the dataset more actionable, a rule-based severity classification was added:

| Severity | Magnitude Range |
|--------|----------------|
| Low | < 4.0 |
| Medium | 4.0 – 5.5 |
| High | ≥ 5.5 |

This classification allows non-technical stakeholders to quickly identify critical events.

---

## 🤖 AI-Assisted Insights (Optional)

An optional step demonstrates how AI can be integrated into analytics workflows by generating high-level insights from a summarized dataset.

- Only statistical summaries are sent to the model (not raw data)
- API keys are handled securely via environment variables
- This step is conceptual and not required to run the pipeline

---

## ▶️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/earthquake-etl-pipeline.git

📌 Key Takeaways

Demonstrates a complete ETL pipeline using real-world data

Applies data validation best practices

Shows how raw data becomes analysis-ready

Bridges technical analysis with business-friendly categorization

Uses clean project organization and version control
