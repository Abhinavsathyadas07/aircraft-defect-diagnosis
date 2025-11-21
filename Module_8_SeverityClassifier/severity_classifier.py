import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import os

# Load your parsed aircraft fault log data
log_df = pd.read_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module_7_FaultLogs/aircraft_fault_log.csv')

# Define features and target columns
features = ['engine_temp', 'hydraulic_pressure', 'vibration']
target = 'severity_label'

# Prepare data for ML
X = log_df[features]
y = log_df[target]

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict severity on test set
severity_pred = clf.predict(X_test)

# Assign predictions back to the DataFrame test rows
log_df.loc[X_test.index, 'predicted_severity'] = severity_pred

# Define output directory and filename
output_dir = '/Users/abhi/Downloads/aircraft-defect-diagnosis/output'
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

output_path = os.path.join(output_dir, 'fault_log_with_severity.csv')

# Save updated fault log with predictions
log_df.to_csv(output_path, index=False)
print(f"Severity predictions saved to {output_path}")


