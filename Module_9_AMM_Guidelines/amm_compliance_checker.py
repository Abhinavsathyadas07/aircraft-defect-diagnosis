import pandas as pd
import os

# Load AMM guideline table (semicolon-separated!)
amm_df = pd.read_csv(
    '/Users/abhi/Downloads/aircraft-defect-diagnosis/Module_9_AMM_Guidelines/amm_guidelines.csv',
    sep=';'
)
print("AMM Guideline Columns:", amm_df.columns)

# Load parsed fault log with prediction/classification
log_df = pd.read_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/output/fault_log_with_severity.csv')

def check_compliance(row):
    # Use available prediction column
    if 'predicted_fault_risk' in row:
        fault = row['predicted_fault_risk']
    elif 'predicted_severity' in row:
        fault = row['predicted_severity']
    else:
        fault = None

    result = amm_df[amm_df['fault_code'] == fault]
    if len(result) > 0:
        return result['required_action'].values[0]
    else:
        return 'No AMM guideline found'

# Apply compliance check
log_df['AMM_action'] = log_df.apply(check_compliance, axis=1)

# Save compliance results
output_dir = '/Users/abhi/Downloads/aircraft-defect-diagnosis/output'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'fault_log_with_compliance.csv')
log_df.to_csv(output_path, index=False)
print(f"AMM compliance check complete. Results saved to {output_path}")
