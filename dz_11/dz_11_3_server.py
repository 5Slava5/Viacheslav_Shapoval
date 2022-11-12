# Сервер для підрахунку кількості слів
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    data_str = (data.decode())
    print(data_str)
    data_words = str(data_str.split())
    data_length = str(data_words.count(' ') + 1)
    conn.send(bytes(data_length, encoding='UTF-8'))
conn.close()
