import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="studenst_db"
)

cursor = db.cursor()