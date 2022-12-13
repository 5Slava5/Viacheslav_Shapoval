"""Програма створення нової бази даних"""
import mysql.connector # type: ignore


my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p6e9r3e5s4m9oTr"
)
my_cursor = my_db.cursor()
my_cursor.execute("CREATE DATABASE my_first_db")
