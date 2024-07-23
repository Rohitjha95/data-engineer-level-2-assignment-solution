import requests
import pandas as pd
import os
import time
from datetime import datetime

# Function to download a file with retry logic
def download_file(url, destination):
    retries = 3
    while retries > 0:
        try:
            response = requests.get(url)
            with open(destination, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {url} to {destination}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")
            retries -= 1
            if retries > 0:
                print(f"Retrying {retries} more times...")
                time.sleep(5)  # Wait for 5 seconds before retrying
    return False

# Function to convert a Parquet file to CSV
def parquet_to_csv(parquet_file, csv_file):
    try:
        df = pd.read_parquet(parquet_file)
        df.to_csv(csv_file, index=False)
        print(f"Converted {parquet_file} to {csv_file}")
        return True
    except Exception as e:
        print(f"Error converting {parquet_file} to CSV: {e}")
        return False

# Base URL for Parquet files (replace with actual URL)
base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_'

# List of month names
months = ['01']

# Year for which data is to be downloaded
year = '2019'

# Iterate over each month
for month in months:
    parquet_url = f"{base_url}{year}-{month}.parquet"
    parquet_file = f"{year}-{month}.parquet"
    csv_file = f"{year}-{month}.csv"

    # Download the Parquet file
    if download_file(parquet_url, parquet_file):
        # Convert the Parquet file to CSV
        if parquet_to_csv(parquet_file, csv_file):
            # Clean up the downloaded Parquet file if needed
            os.remove(parquet_file)
        else:
            print(f"Conversion failed for {parquet_file}. Keeping the Parquet file.")
    else:
        print(f"Download failed for {parquet_url}. Conversion aborted.")
    
    print()  # Print a blank line for better readability between months