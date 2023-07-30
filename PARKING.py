import sqlite3
connection = sqlite3.connect("Parking.db")
cursor = connection.cursor()
command = "CREATE TABLE IF NOT EXISTS add_vehicle(vehicle_owner VARCHAR2(20), vehicle_name VARCHAR2(20), vehicle_type VARCHAR2(15), vehicle_number INTEGER, mobile_number INTEGER, date VARCHAR2(12), in_time VARCHAR2(10), out_time VARCHAR2(10))"
cursor.execute(command)
connection.commit()
connection.close()