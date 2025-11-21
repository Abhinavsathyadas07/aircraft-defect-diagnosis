# Aircraft Defect Diagnosis System

A modular Python project to simulate, preprocess, analyze, and visualize aircraft sensor data for defect detection, predictive maintenance, and actionable recommendations—featuring both batch analytics and an interactive Streamlit dashboard.

---

## **Project Overview**

This project enables realistic simulation and analysis of aircraft sensor data, offering automated defect detection, predictive maintenance analytics, and clear maintenance recommendations. A built-in Streamlit dashboard allows users to interactively filter, visualize, and export results.

---

## **Key Features**

- **Sensor Data Simulation** – Generate realistic time-series aircraft sensor data with customizable parameters and faults.
- **Data Preprocessing** – Clean, normalize, and feature-engineer raw sensor readings.
- **Defect Detection** – Identify abnormal events (engine overheat, hydraulic leaks, vibration risks) using rule-based or ML analytics.
- **Predictive Maintenance** – Anticipate future faults via trend analysis and predictive algorithms.
- **Maintenance Recommendations** – Generate actionable guidance for technicians/operators.
- **Interactive Dashboard** – Explore, filter, upload/download data, visualize sensor trends, export charts/data to CSV/PDF.

---

## **Project Structure**

aircraft-defect-diagnosis/
├── DataSimulation/
├── Preprocessing/
├── Module 3_DefectDetection/
├── Module 4_PredictiveMaintenance/
├── Module 5_Recommendations/
├── Module 6_Visualization/
├── requirements.txt
├── README.md


Output results (CSV, PNG, etc.) are stored in each respective module folder.

---

## **Installation**

1. **Clone the repository**  

2. **Set up Python environment**  

---

## **Usage**

**Run modules in order:**
1. Data Simulation:  
`python DataSimulation/simulate_data.py`
2. Preprocessing:  
`python Preprocessing/Preprocessing.py`
3. Defect Detection:  
`python Module\ 3_DefectDetection/DefectDetection.py`
4. Predictive Maintenance:  
`python Module\ 4_PredictiveMaintenance/PredictiveMaintenance.py`
5. Maintenance Recommendations:  
`python Module\ 5_Recommendations/MaintenanceRecommendation.py`
6. Interactive Dashboard:  
`streamlit run Module\ 6_Visualization/InteractiveDashboard.py`

Upload your own data or use generated datasets. Filter, download, and export results via the dashboard.

---

## **Screenshots**

Include dashboard and results images for clarity:
---

## **Contact**

Author: Abhinav Thundiyil Sathyadas  
GitHub: Abhinavsathyadas07 (https://github.com/Abhinavsathyadas07)
Email: asathya2404@gmail.com

---

## **Acknowledgments**

- Streamlit, Pandas, Matplotlib documentation
- Inspired by aviation safety analytics coursework

---


