#!/usr/bin/env python3


input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket #importare il pacchetto socket 

SERVER_ADDRESS = '127.0.0.1' #indirizzo del server
SERVER_PORT = 22224          #porta del server
sock_service = socket.socket() #socket che crea la richiesta del servizio

sock_service.connect((SERVER_ADDRESS, SERVER_PORT)) #socket che invia la richiesta del servizio

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT))) #commento per verificare che il collegamento sia in atto
while True:
    try:
        dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ") #l'utente inserisce la richiesta da inviare al server
    except EOFError: #se trova un errore sulla rete si chiude la connessione
        print("\nOkay. Exit")
        break
    if not dati:
        print("Non puoi inviare una stringa vuota!") #controllo perchè la stringa non sia vuota
        continue
    if dati == '0':
        print("Chiudo la connessione con il server!") #quando l'utente inserisce 0 in input la connessione si interrompe
    
    dati = dati.encode() #vengono decodificati i dati

    sock_service.send(dati) #I dati vengono inviati

    dati = sock_service.recv(2048) #aspetta la risposta dal server

    if not dati: #controllo che il server risponda
        print("Server non risponde. Exit") #se non risponde
        break #altrimenti
    
    dati = dati.decode()#decodifico la risposta 

    print("Ricevuto dal server:") #stampo a schemro i dati contenuti nell risposta
    print(dati + '\n')

sock_service.close() #se l'utente inserisce 0 o se il server non risponde si chiude la connessione
