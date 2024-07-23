import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('taxi_data.db')
cursor = conn.cursor()

# Create trips table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS taxi_trips (
         VendorID               INTEGER,
         tpep_pickup_datetime   DATETIME,
         tpep_dropoff_datetime  DATETIME,
         passenger_count        REAL       ,
         trip_distance          REAL       ,
         RatecodeID             REAL       ,
         store_and_fwd_flag     string        ,
         PULocationID           INTEGER         ,
         DOLocationID           INTEGER         ,
         payment_type           INTEGER         ,
         fare_amount            REAL       ,
         extra                  REAL       ,
         mta_tax                REAL       ,
         tip_amount             REAL       ,
         tolls_amount           REAL       ,
         improvement_surcharge  REAL       ,
         total_amount           REAL       ,
         congestion_surcharge   REAL       ,
         airport_fee            REAL       ,
         trip_duration          REAL       ,
         average_speed          REAL       ,
         pickup_date            string  

    )
''')

# Create trip metrics table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS trip_metrics (
        pickup_date DATE PRIMARY KEY,
        total_trips INTEGER,
        average_fare REAL
    )
''')

# Insert data into the trips table
taxi_data.to_sql('taxi_trips', conn, if_exists='replace', index=False)

# Close the SQLite connection
conn.close()
