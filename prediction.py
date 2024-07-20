import pandas as pd
import joblib

def predict_store_location(before_lat, before_lng):
    model = joblib.load('models/store_location_predictor.pkl')
    prediction = model.predict([[before_lat, before_lng]])
    return prediction

if __name__ == "__main__":
    test_lat = 37.7749
    test_lng = -122.4194
    predicted_location = predict_store_location(test_lat, test_lng)
    print(f'Predicted store location: {predicted_location}')
