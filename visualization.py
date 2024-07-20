import pandas as pd
import folium
import os

def visualize_locations(data):
    map = folium.Map(location=[data['before_location_lat'].mean(), data['before_location_lng'].mean()], zoom_start=12)
    for _, row in data.iterrows():
        folium.Marker(location=[row['before_location_lat'], row['before_location_lng']], popup='Before').add_to(map)
        folium.Marker(location=[row['after_location_lat'], row['after_location_lng']], popup='After').add_to(map)
    return map

if __name__ == "__main__":
    processed_data_path = 'data/processed/clean_store_location_data.csv'
    data = pd.read_csv(processed_data_path)
    location_map = visualize_locations(data)
    
    os.makedirs('visualizations', exist_ok=True)
    location_map.save('visualizations/location_map.html')
    print("Location map saved to 'visualizations/location_map.html'")
