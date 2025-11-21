import pandas as pd
import os
from datetime import timedelta
import matplotlib.pyplot as plt

# ---- CONFIG ----
original_log_path = '/Users/abhi/Downloads/aircraft-defect-diagnosis/output/fault_log_with_compliance.csv'
output_dir = '/Users/abhi/Downloads/aircraft-defect-diagnosis/output'
augmented_log_path = os.path.join(output_dir, 'fault_log_with_compliance_with_date.csv')

os.makedirs(output_dir, exist_ok=True)

# ---- LOAD DATA ----
if not os.path.exists(original_log_path):
    raise FileNotFoundError(f"Input file not found: {original_log_path}")

log_df = pd.read_csv(original_log_path)

# ---- ENSURE DATE COLUMN EXISTS ----
possible_date_cols = [col for col in log_df.columns if 'date' in col.lower() or 'time' in col.lower()]
if 'date' in log_df.columns:
    date_col = 'date'
    log_df.to_csv(augmented_log_path, index=False)
    print(f"Using existing date column. File saved to: {augmented_log_path}")

elif possible_date_cols:
    date_col = possible_date_cols[0]
    print(f"Using detected date column: '{date_col}'")
    log_df.to_csv(augmented_log_path, index=False)
    print(f"File with date saved to: {augmented_log_path}")

else:
    print("No date column found. Adding sequential 'date' column for forecasting.")
    start_date = pd.to_datetime('2025-11-01')
    log_df['date'] = [start_date + pd.Timedelta(days=i) for i in range(len(log_df))]
    date_col = 'date'
    log_df.to_csv(augmented_log_path, index=False)
    print(f"Saved expanded log with date to: {augmented_log_path}")
# ---- PREPROCESS DATE COLUMN ----
log_df[date_col] = pd.to_datetime(log_df[date_col], errors='coerce')

num_missing = log_df[date_col].isnull().sum()
if num_missing > 0:
    print(f"Warning: {num_missing} rows dropped due to invalid dates.")
    log_df = log_df.dropna(subset=[date_col])

# ---- GROUP AND SUMMARIZE BY DATE ----
faults_per_day = log_df.groupby(date_col).size()
faults_per_day = faults_per_day.asfreq('D', fill_value=0)  # Ensure daily frequency

print("Faults per day (last 7):")
print(faults_per_day.tail(7))

# ---- FORECAST: MEAN OF LAST 7 DAYS ----
recent_days = faults_per_day[-7:]
mean_daily = recent_days.mean()
print(f"Mean daily faults (last 7 days): {mean_daily:.2f}")

future_days = 7
forecast_dates = [faults_per_day.index[-1] + timedelta(days=i) for i in range(1, future_days+1)]
forecast_values = [mean_daily] * future_days

forecast_df = pd.DataFrame({
    date_col: forecast_dates,
    'forecasted_faults': forecast_values
})

output_forecast_csv = os.path.join(output_dir, 'maintenance_forecast.csv')
forecast_df.to_csv(output_forecast_csv, index=False)
print(f"Forecast saved to {output_forecast_csv}")

# ---- PLOT ----
plt.figure(figsize=(10, 6))
plt.plot(faults_per_day.index, faults_per_day.values, label='Observed Faults')
plt.plot(forecast_dates, forecast_values, 'r--', label='Forecasted Faults (Next 7 Days)')
plt.xlabel('Date')
plt.ylabel('Faults')
plt.title('Fault Log: Maintenance Forecast')
plt.legend()
plt.tight_layout()
plot_path = os.path.join(output_dir, 'maintenance_forecast_plot.png')
plt.savefig(plot_path)
plt.close()
print(f"Forecast plot image saved to {plot_path}")

print("\n--- Maintenance Forecast Summary ---")
print(forecast_df)
print(f"\n(See '{output_forecast_csv}' and '{plot_path}' for saved files.)")
