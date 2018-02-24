import os
from socket import *

receive_host = ""
port = 5000
buf = 1024
receive_addr = (receive_host, port)
receive = socket(AF_INET, SOCK_DGRAM)
receive.bind(receive_addr)

send_host = "172.20.12.28" # Enter address of the receiver
send_addr = (send_host, port)
send = socket(AF_INET, SOCK_DGRAM)


print("Talk you piece of shit...")
while True:
#    print "Waiting to Receive"
    (receive_data, receive_addr) = receive.recvfrom(buf)
    print("Received message: " + receive_data)
    if receive_data == "exit":
        break
    
#    print "Your turn to Speak"    
    send_data = input("Enter message to send or type 'exit': ")
    send.sendto(send_data, send_addr)
    if send_data == "exit":
        break
	
send.close()
receive.close()
os._exit(0)

