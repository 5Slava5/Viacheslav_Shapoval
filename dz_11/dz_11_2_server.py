# Сервер для відповіді на повідомлення
import socket

m1 = "Hello!"
m2 = "How are you?"
m3 = "What is your name?"
a1 = "H!"
a2 = "Thanks,I am fine!"
a3 = "Intel."
a4 = "Sorry, I do not understand you."
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
    if data_str == m1:
        conn.send(bytes(a1, encoding='UTF-8'))
    elif data_str == m2:
        conn.send(bytes(a2, encoding='UTF-8'))
    elif data_str == m3:
        conn.send(bytes(a3, encoding='UTF-8'))
    else:
        conn.send(bytes(a4, encoding='UTF-8'))
conn.close()