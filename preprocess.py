import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("Payroll_Data.csv")

features = data[['Base_Salary', 'Overtime_Hours',
                 'Overtime_Pay', 'Total_Salary']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


anomalies = data[data['Anomaly'] == -1]

print("⚠ Detected Payroll Anomalies:")
print(anomalies)


plt.scatter(data['Overtime_Hours'], data['Total_Salary'],
            c=data['Anomaly'])
plt.xlabel("Overtime Hours")
plt.ylabel("Total Salary")
plt.title("Payroll Anomaly Detection")
plt.show()


def retrain_model(new_data):
    new_features = new_data[['Base_Salary', 'Overtime_Hours',
                             'Overtime_Pay', 'Total_Salary']]
    scaled = scaler.fit_transform(new_features)
    model.fit(scaled)


def detect_realtime(record):
    record_scaled = scaler.transform([record])
    prediction = model.predict(record_scaled)
    return "Anomaly" if prediction[0] == -1 else "Normal"
