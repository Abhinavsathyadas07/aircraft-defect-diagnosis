import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Load data
df = pd.read_csv('/Users/abhi/Downloads/aircraft-defect-diagnosis/Module 1_DataSimulation/simulated_aircraft_data.csv')

# 2. Data Cleaning (if necessary)
# Here we drop rows with missing values (None/NaN)
df = df.dropna()

# 3. Feature Extraction
# Rolling mean for each sensor (window = 5)
df['engine_temp_rm'] = df['engine_temp'].rolling(window=5).mean()
df['vibration_rm'] = df['vibration'].rolling(window=5).mean()
df['hydraulic_pressure_rm'] = df['hydraulic_pressure'].rolling(window=5).mean()

# Rate of change features
df['engine_temp_delta'] = df['engine_temp'].diff()
df['vibration_delta'] = df['vibration'].diff()
df['hydraulic_pressure_delta'] = df['hydraulic_pressure'].diff()

# 4. Data Normalization
scaler = MinMaxScaler()
sensor_cols = ['engine_temp', 'vibration', 'hydraulic_pressure',
               'engine_temp_rm', 'vibration_rm', 'hydraulic_pressure_rm',
               'engine_temp_delta', 'vibration_delta', 'hydraulic_pressure_delta']
df[sensor_cols] = scaler.fit_transform(df[sensor_cols])

# 5. Save preprocessed data
df.to_csv('preprocessed_aircraft_data.csv', index=False)
print("Preprocessing complete. Saved as 'preprocessed_aircraft_data.csv'")
