"""Програма додавання даних до таблиць student і employee бази даних my_first_db"""
import mysql.connector  # type: ignore


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p6e9r3e5s4m9oTr",
    database="my_first_db"
)
my_cursor = my_db.cursor()
sql_1 = "INSERT INTO student (PRIMARY_KEY, NAME) VALUES (%s, %s)"
val_1 = (1, "John")
my_cursor.execute(sql_1, val_1)
sql_2 = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
val_2 = (1, "John", 10000)
my_cursor.execute(sql_2, val_2)
my_db.commit()
