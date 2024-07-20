import pandas as pd
import os

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def clean_data(data):
    # Example cleaning steps
    data['transaction_timestamp'] = pd.to_datetime(data['transaction_timestamp'])
    data = data.dropna(subset=['before_location_lat', 'before_location_lng'])
    return data

if __name__ == "__main__":
    raw_data_path = 'data/raw/store_location_data.csv'
    data = load_data(raw_data_path)
    cleaned_data = clean_data(data)
    processed_data_path = 'data/processed/clean_store_location_data.csv'
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
    cleaned_data.to_csv(processed_data_path, index=False)
    print(f'Cleaned data saved to {processed_data_path}')
