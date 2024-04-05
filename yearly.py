import mysql.connector
import datetime
import time

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="first"
)

# Create a cursor object
cursor = conn.cursor()

# Function to increment data in every row of the table
def increment_data():
    try:
        # Increment data in every row of the table
        cursor.execute("UPDATE staff_staff_details SET dl_bal = dl_bal + 1")
        conn.commit()
        print("Data incremented successfully")
    except mysql.connector.Error as e:
        print("Error incrementing data:", e)

# Schedule the incrementation every 10 seconds
while True:
    current_datetime = datetime.datetime.now()
    
    # Check if it's 12:00 AM on January 1st
    if current_datetime.month == 1 and current_datetime.day == 1 and current_datetime.hour == 0 and current_datetime.minute == 0:
        increment_balances()
    
    time.sleep(60)  

# Close cursor and connection
cursor.close()
conn.close()
