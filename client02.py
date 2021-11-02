import socket

HOST = '127.0.0.1'
PORT = 50000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

while True:

    mensagem_envio = input("digite a mensagem: ")
    cliente.sendall(str.encode(mensagem_envio))
    data = cliente.recv(1024)

    print('Mensagem ecoada: ', data.decode())

    '''cliente.sendto(mensagem_envio.encode(), ("",12000))
    mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)
    print(mensagem_bytes.decode())'''