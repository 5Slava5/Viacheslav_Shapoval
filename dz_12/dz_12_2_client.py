"""Клієнт відправлення двох чисел на сервер для проведення з ними арифметичних
дій з використанням asincio"""
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
num_1 = input("Enter the first number : ")
sock.send(bytes(num_1, encoding='UTF-8'))
data1 = sock.recv(1024)
print(data1)
num_2 = input("Enter the second number : ")
sock.send(bytes(num_2, encoding='UTF-8'))
data2 = sock.recv(1024)
print(data2)
sock.close()
