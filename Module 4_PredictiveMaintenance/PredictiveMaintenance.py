import pandas as pd
import numpy as np

# Load defect detection results
df = pd.read_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 3_DefectDetection/defect_detection_results.csv')

# Calculate rolling averages to smooth short-term fluctuations
df['engine_temp_roll'] = df['engine_temp'].rolling(window=10, min_periods=1).mean()
df['vibration_roll'] = df['vibration'].rolling(window=10, min_periods=1).mean()
df['hydraulic_pressure_roll'] = df['hydraulic_pressure'].rolling(window=10, min_periods=1).mean()

# Predictive logic: flag if rolling average gets close to defect threshold
def predict_fault(row):
    if row['engine_temp_roll'] > 0.80:
        return 'engine_overheat_risk'
    elif row['hydraulic_pressure_roll'] < 0.35:
        return 'hydraulic_leak_risk'
    elif row['vibration_roll'] > 0.70:
        return 'vibration_high_risk'
    else:
        return 'no_immediate_risk'

df['predicted_fault_risk'] = df.apply(predict_fault, axis=1)

# Mark timestamps where transition from "no_immediate_risk" to any risk happens
df['risk_transition'] = df['predicted_fault_risk'].ne(df['predicted_fault_risk'].shift())
predicted_events = df[df['risk_transition'] & (df['predicted_fault_risk'] != 'no_immediate_risk')]

# Save predictive results
df.to_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 4_PredictiveMaintenance/predictive_maintenance_results.csv', index=False)
predicted_events[['timestamp', 'predicted_fault_risk']].to_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 4_PredictiveMaintenance/predicted_events.csv', index=False)

print("Predictive maintenance complete.\nResults saved to 'predictive_maintenance_results.csv' and high-risk event summary to 'predicted_events.csv'.")
