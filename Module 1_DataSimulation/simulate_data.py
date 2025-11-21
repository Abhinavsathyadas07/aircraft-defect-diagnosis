import random
import csv

#CONFIG

NUM_SAMPLES = 2000
FAULT_INTERVAL = 150  #  EVERY 150 , INJECT A FAULTY INPUT

# Sensor simulation configuration: (mean, stddev) for normal case
SENSOR_CONFIG = {
    "engine_temp": (650, 10),            # degrees Celsius
    "vibration": (0.01, 0.005),          # g (acceleration)
    "hydraulic_pressure": (3000, 20)     # PSI
}

def simulate_sensor_data():
    data_records = []
    for t in range(NUM_SAMPLES):
        # Simulate normal
        engine_temp = random.gauss(*SENSOR_CONFIG["engine_temp"])
        vibration = random.gauss(*SENSOR_CONFIG["vibration"])
        hydraulic_pressure = random.gauss(*SENSOR_CONFIG["hydraulic_pressure"])
        fault_label = "normal"

 # Inject fault at intervals
        if t % FAULT_INTERVAL == 0 and t != 0:
            fault_type = random.choice(["engine_overheat", "hydraulic_leak", "vibration_high"])
            if fault_type == "engine_overheat":
                engine_temp += random.randint(80, 200)
            elif fault_type == "hydraulic_leak":
                hydraulic_pressure -= random.randint(500, 1500)
            elif fault_type == "vibration_high":
                vibration *= random.randint(5, 15)
            fault_label = fault_type

        data_records.append({
            'timestamp': t,
            'engine_temp': round(engine_temp, 2),
            'vibration': round(vibration, 4),
            'hydraulic_pressure': round(hydraulic_pressure, 2),
            'fault_label': fault_label
        })
    return data_records

def save_to_csv(data, filename="simulated_aircraft_data.csv"):
    keys = data[0].keys()
    with open(filename, "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

if __name__ == "__main__":
    simulated_data = simulate_sensor_data()
    save_to_csv(simulated_data)
    print(f"Simulated {NUM_SAMPLES} samples and saved to 'simulated_aircraft_data.csv'")