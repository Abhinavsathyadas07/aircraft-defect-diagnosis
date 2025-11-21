import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from matplotlib.backends.backend_pdf import PdfPages
import io

today = datetime.datetime.now()
current_year = today.year


st.set_page_config(layout="wide")
st.title("Aircraft Defect Diagnosis Interactive Dashboard")

# 1. File Upload
uploaded_file = st.sidebar.file_uploader("Upload CSV file for analysis", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded and loaded!")
else:
    df = pd.read_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 5_Recommendations/maintenance_recommendations_full.csv')

# 2. Date Range Filter
df['timestamp'] = pd.to_datetime(df['timestamp'])
min_date = df['timestamp'].min()
max_date = today  # instead of df['timestamp'].max(), use current date
date_range = st.sidebar.date_input(
    "Select date range",
    [min_date.date(), max_date.date()]
)
if len(date_range) == 2:
    filtered_df = df[
        (df['timestamp'] >= pd.to_datetime(date_range[0])) &
        (df['timestamp'] <= pd.to_datetime(date_range[1]))
    ]

# 3. Risk Filter
risk_types = df['predicted_fault_risk'].unique()
selected_risks = st.sidebar.multiselect("Risk types to display", risk_types, default=list(risk_types))
filtered_df = filtered_df[filtered_df['predicted_fault_risk'].isin(selected_risks)]

st.subheader("Sensor Trends with Risk Events")

# 4. Charts
figs = []
def plot_sensor(sensor, risk, color, ylabel):
    fig, ax = plt.subplots()
    ax.plot(filtered_df['timestamp'], filtered_df[sensor], label=sensor)
    event_mask = filtered_df['predicted_fault_risk'] == risk
    ax.scatter(filtered_df[event_mask]['timestamp'], filtered_df[event_mask][sensor], color=color, label=f"{risk} Event")
    ax.set_xlabel('Timestamp')
    ax.set_ylabel(ylabel)
    ax.set_title(f"{sensor.capitalize()} with {risk.replace('_', ' ').title()}")
    ax.legend()
    st.pyplot(fig)
    figs.append(fig)

if 'engine_overheat_risk' in selected_risks:
    plot_sensor('engine_temp', 'engine_overheat_risk', 'red', 'Normalized Temp')
if 'hydraulic_leak_risk' in selected_risks:
    plot_sensor('hydraulic_pressure', 'hydraulic_leak_risk', 'orange', 'Normalized Pressure')
if 'vibration_high_risk' in selected_risks:
    plot_sensor('vibration', 'vibration_high_risk', 'purple', 'Normalized Vibration')

# Extra Charts
st.subheader("Histogram & Boxplot")
col1, col2 = st.columns(2)
with col1:
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(filtered_df['engine_temp'], bins=30, color='skyblue')
    ax_hist.set_title("Engine Temp Histogram")
    st.pyplot(fig_hist)
    figs.append(fig_hist)
with col2:
    fig_box, ax_box = plt.subplots()
    ax_box.boxplot(filtered_df['vibration'])
    ax_box.set_title("Vibration Boxplot")
    st.pyplot(fig_box)
    figs.append(fig_box)

# 5. Maintenance Actions Table
st.subheader("Maintenance Recommendations")
show_actions = st.checkbox("Show actionable recommendations only", value=True)
if show_actions:
    actions = filtered_df[filtered_df['maintenance_recommendation'] != 'No immediate maintenance required']
else:
    actions = filtered_df
st.dataframe(actions[['timestamp', 'predicted_fault_risk', 'maintenance_recommendation']])

# 6. Download Filtered Data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download filtered data as CSV", data=csv, file_name="filtered_maintenance_data.csv", mime="text/csv")

# 7. Export Charts to PDF
if st.button("Export all charts to PDF"):
    pdf_bytes = io.BytesIO()
    with PdfPages(pdf_bytes) as pdf:
        for fig in figs: pdf.savefig(fig)
    pdf_bytes.seek(0)
    st.download_button(label="Download PDF of Charts", data=pdf_bytes, file_name="dashboard_charts.pdf", mime="application/pdf")
    st.success("Charts PDF ready for download!")

