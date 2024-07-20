import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data):
    features = data[['before_location_lat', 'before_location_lng']]
    target = data[['after_location_lat', 'after_location_lng']]
    
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

if __name__ == "__main__":
    processed_data_path = 'data/processed/clean_store_location_data.csv'
    data = pd.read_csv(processed_data_path)
    model, X_test, y_test = train_model(data)
    
    # Save the model for later use
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/store_location_predictor.pkl')
    print("Model trained and saved to 'models/store_location_predictor.pkl'")
