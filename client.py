
# import socket

# cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     mensagem_envio = input("digite a mensagem: ")
#     cliente.sendto(mensagem_envio.encode(), ("",12000))
#     mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)
#     print(mensagem_bytes.decode())

# Segundo exemplo cliente

import socket

HOST = '127.0.0.1'
PORT = 50000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

cliente.sendall(str.encode('Bom dia Flor do dia'))
data = cliente.recv(1024)


print('Mensagem ecoada: ', data.decode())