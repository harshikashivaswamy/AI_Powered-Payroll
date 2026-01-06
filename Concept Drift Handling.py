def retrain_model(new_data):
    new_features = new_data[['Base_Salary', 'Overtime_Hours',
                             'Overtime_Pay', 'Total_Salary']]
    scaled = scaler.fit_transform(new_features)
    model.fit(scaled)
