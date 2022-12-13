"""Програма створення нової таблиці у базі даних my_first_db"""
import mysql.connector  # type: ignore


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p6e9r3e5s4m9oTr",
    database="my_first_db"
)
my_cursor = my_db.cursor()
my_cursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")
