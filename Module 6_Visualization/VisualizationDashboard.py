import pandas as pd
import matplotlib.pyplot as plt

# Load final maintenance recommendations and results
df = pd.read_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 5_Recommendations/maintenance_recommendations_full.csv')

# Plot engine temperature, vibration, and hydraulic pressure over time, color-coded by detected/predicted risk
plt.figure(figsize=(15,8))

plt.subplot(3,1,1)
plt.plot(df['timestamp'], df['engine_temp'], label='Engine Temp')
plt.scatter(df[df['predicted_fault_risk']=='engine_overheat_risk']['timestamp'], 
            df[df['predicted_fault_risk']=='engine_overheat_risk']['engine_temp'], color='red', label='Overheat Risk')
plt.title('Engine Temperature with Overheat Risks')
plt.ylabel('Normalized Temp')
plt.legend()

plt.subplot(3,1,2)
plt.plot(df['timestamp'], df['hydraulic_pressure'], label='Hydraulic Pressure')
plt.scatter(df[df['predicted_fault_risk']=='hydraulic_leak_risk']['timestamp'],
            df[df['predicted_fault_risk']=='hydraulic_leak_risk']['hydraulic_pressure'], color='orange', label='Leak Risk')
plt.title('Hydraulic Pressure with Leak Risks')
plt.ylabel('Normalized Pressure')
plt.legend()

plt.subplot(3,1,3)
plt.plot(df['timestamp'], df['vibration'], label='Vibration')
plt.scatter(df[df['predicted_fault_risk']=='vibration_high_risk']['timestamp'],
            df[df['predicted_fault_risk']=='vibration_high_risk']['vibration'], color='purple', label='High Vibration Risk')
plt.title('Vibration with High Risk Events')
plt.xlabel('Timestamp')
plt.ylabel('Normalized Vibration')
plt.legend()

plt.tight_layout()
plt.savefig('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 6_Visualization/dashboard.png')
plt.show()

# Show summary of actionable maintenance recommendations
actions = df[df['maintenance_recommendation'] != 'No immediate maintenance required']
print("\nMaintenance Actions Needed (Summary):")
print(actions[['timestamp', 'predicted_fault_risk', 'maintenance_recommendation']].to_string(index=False))
