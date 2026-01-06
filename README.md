Payroll Anomaly Detection Engine

This project is a simple but powerful tool that helps detect unusual or suspicious activities in payroll data.

It can identify things like:

Sudden salary jumps
Unusual overtime values
Possible fraud or mistakes in payroll
It works using machine learning (Isolation Forest) and supports:

Creating sample payroll data

Cleaning and preparing data

Training an AI model

Detecting anomalies

Checking data drift

Real-time anomaly simulation

What This Project Does

In simple terms:

Creates payroll data
Prepares the data
Trains an AI model
Finds suspicious salary or overtime records
Can even simulate real-time anomalies

Project Files

data_generator.py → Creates sample payroll data

preprocess.py → Cleans and scales the data

train_model.py → Trains the anomaly detection model

detect_anomalies.py → Finds unusual payroll entries

drift_detection.py → Checks if data behaviour has changed

realtime_simulation.py → Simulates real-time anomaly detection

model.pkl → Saved AI model

scaler.pkl → Saved data scaler

processed_data.csv → Cleaned data

payroll_data.csv → Raw generated data

Technology Used

Python,
Pandas,
Scikit-Learn,
Isolation Forest Model# AI_Powered-Payroll.
