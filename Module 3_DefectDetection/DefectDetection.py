import pandas as pd

# Load preprocessed data
df = pd.read_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 2_Preprocessing/preprocessed_aircraft_data.csv')

# Example rule-based defect detection (adjust thresholds if needed for your normalization)
def detect_defects(row):
    if row['engine_temp'] > 0.85:
        return "engine_overheat"
    elif row['hydraulic_pressure'] < 0.30:
        return "hydraulic_leak"
    elif row['vibration'] > 0.75:
        return "vibration_high"
    else:
        return "normal"

df['defect_detected'] = df.apply(detect_defects, axis=1)

# Save results
df[['timestamp', 'engine_temp', 'hydraulic_pressure', 'vibration', 'defect_detected']].to_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 3_DefectDetection/defect_detection_results.csv', index=False)
print("Defect detection complete. Results saved to 'defect_detection_results.csv'")
