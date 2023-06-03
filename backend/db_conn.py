import pymysql as sqlcnt
import os

# Connect to the database
conn = sqlcnt.connect(host="localhost", user="root", passwd="sanjeev123", database="ignitiahack")
cursor = conn.cursor()

os.chdir("D:\IgnitiaHack\\backend")

# Run the detection script
for i in os.listdir("D:\IgnitiaHack\\backend\data\images"):
    command = "python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/"+i+" --plate"
    output = os.popen(command).read()

    # Extract the necessary information from the output
    plate_number = output[18:]  # Replace with the actual plate number extracted from the output

    # Insert or update the data in the table
    insert_query = "INSERT INTO license_plate (License_plate_No, timestamp) VALUES (%s, NOW()) ON DUPLICATE KEY UPDATE License_plate_No = VALUES(License_plate_No), timestamp = VALUES(timestamp)"
    values = (plate_number,)
    cursor.execute(insert_query, values)
    cursor.execute("Delete from license_plate where License_plate_No = ''")
    conn.commit()

# Close the database connection
conn.close()
