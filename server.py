
# import socket


# servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# servidor.bind(('','12000'))

# while True: 
#     mensagem_bytes, endereco_ip_cliente = servidor.recvfrom(2048)
#     mensagem_resposta = mensagem_bytes.decode().upper()
#     servidor.sendto(mensagem_resposta.encode(), endereco_ip_cliente)
#     print(mensagem_resposta)

# Segundo exemplo server
import socket

HOST = 'localhost'
PORT = 50000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print('Aguardado conexão de um cliente')
conn, ender = servidor.accept()

print("Conectado em", ender)
while True:
    data=conn.recv(1024)
    if not data:
        print('Fechando conexão')
        conn.close()
        break
    conn.sendall(data)