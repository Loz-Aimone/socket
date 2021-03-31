
import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_service = socket.socket()
sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
#def socket_connect (sock_service, SERVER_ADDRESS, SERVER_PORT):
  
  
print("Client connesso a: " + str((SERVER_ADDRESS, SERVER_PORT)))
protocollo = ["SYN","SYN ACK","ACK with data","ACK for data"]
step = 0
dati = str(step)

def input_data():

    while True:
        try:
            data = input("Inserisci operatore, numero uno e numero due da mandare: ")
        except EOFError:
            print("\nOkay. Exit")
            break
        if not data:
            print("non puoi inviare una stringa vuota!")
            continue
        
        if data == 'E' or data == 'e':
            print("connessione col server conclusa!")
            break
        
        data = data.encode()
        sock_service.send(data)
        data = sock_service.recv(2048)
        if not data:
            print("Il server non risonde")
            break
        
        data = data.decode()
        print("Ricevuto dal server:")
        print(data + '\n')
   

sock_service.close()