def detect_realtime(record):
    record_scaled = scaler.transform([record])
    prediction = model.predict(record_scaled)
    return "Anomaly" if prediction[0] == -1 else "Normal"
