"""Програма створення нової таблиці employee у базі даних my_first_db"""
import mysql.connector  # type: ignore


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p6e9r3e5s4m9oTr",
    database="my_first_db"
)
my_cursor = my_db.cursor()
my_cursor.execute("CREATE TABLE employee("
                  "id INT AUTO_INCREMENT PRIMARY KEY, "
                  "name VARCHAR(255),"
                  "salary INT(6))")
