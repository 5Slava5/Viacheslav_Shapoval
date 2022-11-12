# Клієнт для обміну повідомленнями
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
message = input("Enter > 'Hello!', 'How are you?' or 'What is your name?': ")
sock.send(bytes(message, encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data)
