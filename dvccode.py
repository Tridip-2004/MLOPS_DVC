import pandas as pd
import os

# Heart failure dataset (sample)
data = {
    "age": [65, 50, 72, 45, 60],
    "sex": [1, 0, 1, 1, 0],                 # 1 = Male, 0 = Female
    "chest_pain_type": [3, 2, 4, 1, 3],
    "resting_bp": [140, 130, 150, 120, 135],
    "cholesterol": [245, 220, 280, 210, 230],
    "fasting_bs": [1, 0, 1, 0, 1],          # 1 = True, 0 = False
    "resting_ecg": [1, 0, 2, 0, 1],
    "max_heart_rate": [120, 150, 110, 165, 130],
    "exercise_angina": [1, 0, 1, 0, 1],     # 1 = Yes, 0 = No
    "oldpeak": [2.3, 1.0, 3.1, 0.5, 2.0],
    "st_slope": [2, 1, 3, 1, 2],
    "heart_failure": [1, 0, 1, 0, 1]        # Target: 1 = Disease, 0 = No Disease
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create folder
folder = "heart_failure_data"
os.makedirs(folder, exist_ok=True)

# Save CSV
file_path = os.path.join(folder, "heart_failure_dataset.csv")
df.to_csv(file_path, index=False)

print("Heart Failure dataset saved successfully!")
print("File path:", file_path)