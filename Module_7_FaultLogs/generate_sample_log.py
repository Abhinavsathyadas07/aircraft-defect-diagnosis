import pandas as pd

data = {
    'engine_temp': [0.8, 0.5, 0.95, 0.7, 0.4],
    'hydraulic_pressure': [0.6, 0.9, 0.3, 0.45, 0.8],
    'vibration': [0.15, 0.35, 0.55, 0.25, 0.10],
    'fault_code': ['engine_overheat_risk', 'normal', 'engine_overheat_risk', 'hydraulic_leak_risk', 'normal'],
    'severity_label': ['High', 'Low', 'High', 'Medium', 'Low']
}

df = pd.DataFrame(data)
df.to_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 7_FaultLogs/aircraft_fault_log.csv', index=False)
print("Sample aircraft_fault_log.csv has been created!")
