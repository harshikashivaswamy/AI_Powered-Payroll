model = IsolationForest(
    n_estimators=100,
    contamination=0.15,
    random_state=42
)

data['Anomaly'] = model.fit_predict(scaled_features)
