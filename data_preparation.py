import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Parameters
num_records = 1000
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
time_diff_mean = 7200  # Mean time difference in seconds (2 hours)
time_diff_std = 3600   # Standard deviation of time difference (1 hour)
lat_range = (35.0, 45.0)
lng_range = (-120.0, -70.0)

# Helper functions
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def random_coordinates(lat_range, lng_range):
    return round(random.uniform(*lat_range), 6), round(random.uniform(*lng_range), 6)

# Generate data
data = []
for i in range(num_records):
    transaction_id = i + 1
    store_id = f'S{random.randint(1, 100):03d}'
    user_id = random.randint(1, 500)
    transaction_timestamp = random_date(start_date, end_date)
    before_location_lat, before_location_lng = random_coordinates(lat_range, lng_range)
    after_location_lat, after_location_lng = random_coordinates(lat_range, lng_range)
    before_timestamp = transaction_timestamp - timedelta(seconds=abs(int(np.random.normal(time_diff_mean, time_diff_std))))
    after_timestamp = transaction_timestamp + timedelta(seconds=abs(int(np.random.normal(time_diff_mean, time_diff_std))))
    time_diff = (after_timestamp - before_timestamp).total_seconds()
    distance_diff = np.sqrt((after_location_lat - before_location_lat) ** 2 + (after_location_lng - before_location_lng) ** 2) * 111  # Approx conversion to km

    data.append([
        transaction_id, store_id, user_id, transaction_timestamp, before_location_lat, before_location_lng,
        before_timestamp, after_location_lat, after_location_lng, after_timestamp, time_diff, distance_diff
    ])

# Create DataFrame
columns = [
    'transaction_id', 'store_id', 'user_id', 'transaction_timestamp', 'before_location_lat', 'before_location_lng',
    'before_timestamp', 'after_location_lat', 'after_location_lng', 'after_timestamp', 'time_diff', 'distance_diff'
]
data_df = pd.DataFrame(data, columns=columns)

# Create data directory if it doesn't exist
os.makedirs('data/raw', exist_ok=True)

# Save to CSV
data_df.to_csv('data/raw/store_location_data.csv', index=False)

print("Dataset created and saved as 'data/raw/store_location_data.csv'.")
