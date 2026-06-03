# Student Management System

## Project Overview

The Student Management System is a backend application developed using Flask and MySQL. It allows users to perform CRUD operations on student records stored in a MySQL database.

## Features

* Add Student Records
* View Student Records    
* Update Student Information        
* Delete Student Records
* MySQL Database Integration

## Technologies Used

* Python
* Flask
* MySQL

## Project Structure

```text
student_management_system/
│
├── app.py
├── db.py
└── README.md
```

## Database Setup

### Create Database

```sql
CREATE DATABASE student_db;
```

### Use Database

```sql
USE student_db;
```

### Create Table

```sql
CREATE TABLE students(
    s_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    course VARCHAR(100),
    marks INT
);
```

## Database Connection

Configure the database connection in `db.py`.

```python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)

cursor = db.cursor()
```

## Running the Application

```bash
python app.py
```

Open your browser and visit:    

```text
http://127.0.0.1:5000
```

## Application Routes

| Route   | Description    |
| ------- | -------------- |
| /       | Home Page      |
| /add    | Add Student    |
| /view   | View Students  |
| /update | Update Student |
| /delete | Delete Student |

## CRUD Operations

### Create

Adds a new student record to the database.

### Read

Displays all student records.

### Update

Updates student information using Student ID.

### Delete

Deletes a student record using Student ID.

## Learning Outcomes

* Flask Routing
* MySQL Connectivity
* CRUD Operations
* SQL Queries
* Backend Development Fundamentals

## Author

Nandini

### Role

Python Backend Developer
