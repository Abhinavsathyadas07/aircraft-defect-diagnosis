import pandas as pd

# Load predictive maintenance results
df = pd.read_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 4_PredictiveMaintenance/predictive_maintenance_results.csv')

# Recommendation logic based on predicted risk
def recommend_action(risk):
    if risk == 'engine_overheat_risk':
        return 'Schedule engine temperature inspection and coolant check'
    elif risk == 'hydraulic_leak_risk':
        return 'Inspect hydraulic system for leaks and replace fluid'
    elif risk == 'vibration_high_risk':
        return 'Check engine mounts and vibration dampers'
    else:
        return 'No immediate maintenance required'

df['maintenance_recommendation'] = df['predicted_fault_risk'].apply(recommend_action)

# Filter for actionable recommendations only (no "no immediate maintenance required" entries)
recommendations = df[df['maintenance_recommendation'] != 'No immediate maintenance required']

# Save all recommendations and filtered actionable ones
df.to_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 5_Recommendations/maintenance_recommendations_full.csv', index=False)
recommendations[['timestamp', 'predicted_fault_risk', 'maintenance_recommendation']].to_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 5_Recommendations/maintenance_actions.csv', index=False)

print("Maintenance recommendations generated.\nFull results in 'maintenance_recommendations_full.csv' and actionable actions in 'maintenance_actions.csv'.")
