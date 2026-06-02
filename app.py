from flask import Flask
from db import db, cursor

app = Flask(__name__)
@app.route('/')
def home():
    return "students Management System"
@app.route('/add')
def add_student():
    query = """
    INSERT INTO students(name, department, fees)
    VALUES(%s, %s, %s)
    """	`
    values = ("Nandini", "cse", 50000)
    cursor.execute(query, values)
    db.commit()
    return "student Added"
@app.route('/view')
def view_students():
    query = "SELECT * FROM students"
    cursor.execute(query)
    data = cursor.fetchall()
    return str(data)
@app.route('/update')
def update_student():
    query = """
    UPDATE students
    SET fees  = %s
    WHERE id = %s
    """
    values = (70000, 1)
    cursor.execute(query, values)
    db.commit()
    return "student Updated"
@app.route('/delete')
def delete_student():
    query = "DELETE FROM students WHERE id = %s"
    values = (1,)
    cursor.execute(query, values)
    db.commit()
    return "student Deleted"
if __name__ == '__main__':
    app.run(debug=True)