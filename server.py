#!/usr/bin/env python3
import socket #importiamo il pacchetto socket



SERVER_ADDRESS = '127.0.0.1' #indirizzo server

SERVER_PORT = 22224 #porta server

sock_listen = socket.socket()

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5)

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT))) #Il server in ascolto, è in grado richieste di connessione


while True: #se il server in ascolto esegue i comandi sottostanti
    sock_service, addr_client = sock_listen.accept() #accetta la connessione dal client, e rimane in ascolto per ricevere i dati
    print("\nConnessione ricevuta da " + str(addr_client))
    print("\nAspetto di ricevere i dati ")
    contConn=0 #inizializza il contatore
    while True: #se la connessione è attiva esegue i comandi sottostanti
        dati = sock_service.recv(2048) #aspetta la richiesta del client
        contConn+=1 #il contatore incrementa di 1
        if not dati: #controlla che i dati abbiano un valore 
            print("Fine dati dal client. Reset")
            break #se dati non ha valore chiudo la connessione 
        
        dati = dati.decode()#se dati ha valore lo decodifica
        print("Ricevuto: '%s'" % dati)
        if dati=='0': 
            print("Chiudo la connessione con " + str(addr_client))
            break #se dati ha valore 0 chiudo la connessione

        operazione, primo, secondo = dati.split(";")#split
        #Vari if per selezionare l'operazione che il client ha inserito
        if operazione == "piu":
            risultato = int(primo) + int(secondo)
        if operazione == "meno":
            risultato = int(primo) - int(secondo)
        if operazione == "per":
            risultato = int(primo) * int(secondo)
        if operazione == "diviso":
            risultato = int(primo) / int(secondo)

        dati = "Il risultato dell'operazione: "+operazione +" tra "+primo+" e "+secondo+" è: "+str(risultato)#output
        
        dati = dati.encode() #codifica la risposta da inviare

        sock_service.send(dati) #invia i dati codificati

    sock_service.close() #chiusura della connessione

