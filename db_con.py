import pymysql as sqlcnt
import os

# Connect to the database
conn = sqlcnt.connect(host="localhost",user="root",password="sanjeev123",database="ignitiahack")
cursor = conn.cursor()

# Run the detection script
command = "python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/car2.jpg --plate"
output = os.popen(command).read()

# Extract the necessary information from the output
plate_number = output[18:] # Replace with the actual plate number extracted from the output

# Insert the data into the table
insert_query = "INSERT INTO license_plate (License_plate_No, timestamp) VALUES (%s, NOW())"
values = (plate_number,)
cursor.execute(insert_query, values)
conn.commit()

# Close the database connection
conn.close()
