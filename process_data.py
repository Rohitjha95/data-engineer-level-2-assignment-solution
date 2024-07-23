import pandas as pd
import numpy as np

# Path to your CSV file
csv_file = '2019-01.csv'

# Read the CSV file into a pandas DataFrame
try:
    taxi_data = pd.read_csv(csv_file)
    # Print the first few rows of the DataFrame to verify it was read correctly
    #print(taxi_data.head())
except FileNotFoundError:
    print(f"Error: The file '{csv_file}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{csv_file}' is empty or not properly formatted.")
except Exception as e:
    print(f"Error reading '{csv_file}': {e}")

#print(taxi_data)
# Cleaning data: Remove trips with missing or corrupt data
#taxi_data.dropna(inplace=True)
#print(taxi_data)
# Convert pickup and drop-off time to datetime objects
taxi_data['tpep_pickup_datetime'] = pd.to_datetime(taxi_data['tpep_pickup_datetime'])
taxi_data['tpep_dropoff_datetime'] = pd.to_datetime(taxi_data['tpep_dropoff_datetime'])

# Derive new columns: trip duration and average speed
taxi_data['trip_duration'] = (taxi_data['tpep_dropoff_datetime'] - taxi_data['tpep_pickup_datetime']).dt.total_seconds() / 60  # in minutes
taxi_data['average_speed'] = taxi_data['trip_distance'] / (taxi_data['trip_duration'] / 60)  # miles per hour

#print(taxi_data)
# Aggregate data: Calculate total trips and average fare per day
taxi_data['pickup_date'] = taxi_data['tpep_pickup_datetime'].dt.date
#print(taxi_data)
daily_metrics = taxi_data.groupby('pickup_date').agg(
    total_trips=('tpep_pickup_datetime', 'count'),
    average_fare=('total_amount', 'mean')
).reset_index()

print(daily_metrics)

daily_metrics.to_csv('csv_data.csv', header=True)
