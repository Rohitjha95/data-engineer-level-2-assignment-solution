
# Reconnect to SQLite database
conn = sqlite3.connect('taxi_data.db')

# Example SQL queries to answer the questions

# 1. Peak hours for taxi usage
peak_hours_query = '''
    SELECT strftime('%H', tpep_pickup_datetime) AS hour_of_day, COUNT(*) AS trips_count
    FROM taxi_trips
    GROUP BY hour_of_day
    ORDER BY trips_count DESC
    LIMIT 5;
'''

# Execute the query and load results into a DataFrame
peak_hours_df = pd.read_sql_query(peak_hours_query, conn)

# Plotting peak hours
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.barplot(x='hour_of_day', y='trips_count', data=peak_hours_df)
plt.title('Peak Hours for Taxi Usage')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. How does passenger count affect trip fare?
passenger_count_query = '''
    SELECT passenger_count, AVG(fare_amount) AS avg_fare
    FROM taxi_trips
    GROUP BY passenger_count
    ORDER BY passenger_count;
'''

# Execute the query and load results into a DataFrame
passenger_count_df = pd.read_sql_query(passenger_count_query, conn)

# Plotting passenger count vs trip fare
plt.figure(figsize=(8, 6))
sns.barplot(x='passenger_count', y='avg_fare', data=passenger_count_df)
plt.title('Average Trip Fare by Passenger Count')
plt.xlabel('Number of Passengers')
plt.ylabel('Average Fare ($)')
plt.tight_layout()
plt.show()

# 3. Trends in usage over the year
usage_trends_query = '''
    SELECT strftime('%m', tpep_pickup_datetime) AS month, COUNT(*) AS trips_count
    FROM taxi_trips
    GROUP BY month
    ORDER BY month;
'''

# Execute the query and load results into a DataFrame
usage_trends_df = pd.read_sql_query(usage_trends_query, conn)

# Plotting trends in usage over the year
plt.figure(figsize=(10, 6))
sns.lineplot(x='month', y='trips_count', data=usage_trends_df, marker='o')
plt.title('Trends in Taxi Usage Over the Year')
plt.xlabel('Month')
plt.ylabel('Number of Trips')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.tight_layout()
plt.show()

# Close the SQLite connection
conn.close()
