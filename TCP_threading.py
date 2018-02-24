import threading
from socket import *

BUFFERSIZE  = 1024

def send_tcp(sock):
    message = ''
    while message != 'exit':
        message = input()
        if message == 'exit':
            sock.send(message.encode())
            break
        sock.send(message.encode())


def recv_tcp(conn):
    decoded_data = ''
    while decoded_data != 'exit':
        data = conn.recv(BUFFERSIZE)
        decoded_data = data.decode()
        print('Him/Her : ' + decoded_data + '\n')


if __name__ == '__main__':
    print('This is a Beta version, with full Command Line Interface. Run the server first\n.')
    x = input('Enter 1 for being server, 2 for being client\n')
    if int(x) is 1:
        print('You are the server, please be patient with the set-up process\n'
              'If you do not know to get the ip, type ifconfig in your terminal\n'
              'or ipconfig all in your windows command prompt\n\n')
        server_ip_address = input('Enter your IP address :\n')
        server_port = int(input('Enter the port you want to use for communication\n'))

        server_address = (server_ip_address, server_port)

        server = socket(AF_INET, SOCK_STREAM)
        server.bind(server_address)
        server.listen(1)

        connection, address = server.accept( )
        print('The connected address is : %s\n', address)
        send_thread = threading.Thread(target=send_tcp, args=(connection,))
        receive_thread = threading.Thread(target=recv_tcp, args=(connection,))

        send_thread.start()
        receive_thread.start()

        send_thread.join()
        receive_thread.join()

        print('That was a trial software; feel free to purchase the full product\n')


    if int(x) is 2:
        print('You are the fucking client, you need to enter the ip address and \n'
              'and the port of the server you wish to connect to.\n')
        server_ip_address = input('Enter servers IP address :\n')
        server_port = int(input('Enter the port you want to use for communication\n'))

        server_address = (server_ip_address, server_port)

        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(server_address)

        send_thread = threading.Thread(target=send_tcp, args=(client_socket,))
        receive_thread = threading.Thread(target=recv_tcp, args=(client_socket,))

        send_thread.start()
        receive_thread.start()

        send_thread.join()
        receive_thread.join()

        print('That was a trial software; feel free to purchase the full product\n')
