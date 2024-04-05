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

# Function to check and update vl_bal for each staff member
def update_vl_bal():
    try:
        # Fetch all staff members' details including their join dates
        cursor.execute("SELECT staff_id, join_date FROM staff_staff_details")
        staff_details = cursor.fetchall()
        
        # Get the current date
        current_date = datetime.datetime.now()
        
        # Iterate through each staff member's details
        for staff_id, join_date in staff_details:
            # Calculate the difference in days between the current date and the join date
            days_difference = (current_date - join_date).days
            
            # If the difference is 365 days or more, update vl_bal to 6 for this staff member
            if days_difference >= 365:
                cursor.execute("UPDATE staff SET vl_bal = 6 WHERE staff_id = %s", (staff_id,))
                conn.commit()
                print(f"vl_bal updated to 6 for staff_id {staff_id}")
    except mysql.connector.Error as e:
        print("Error updating vl_bal:", e)

# Main loop
while True:
    # Call the function to update vl_bal for eligible staff members
    update_vl_bal()
    
    # Wait for 24 hours before checking again
    time.sleep(86400)  # 24 hours in seconds

# Close cursor and connection
cursor.close()
conn.close()
