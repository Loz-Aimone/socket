#!/usr/bin/env python3
import socket #importiamo il pacchetto socket

SERVER_ADDRESS = '127.0.0.1' #indirizzo server
SERVER_PORT = 22224 #porta server

def ricevi_comandi(sock_listen): #la funzione riceve la socket connessa al server e la utilizza per accettare le richieste di connessione e per ognuna crea una socket per i dati (sock_service) da cui ricevere le richieste e inviare le risposte
    while True: #se il server è in ascolto esegue i comandi
        sock_service, addr_client = sock_listen.accept() #acetta la connessione con il client e rimane in ascolto per ricevere i dati
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nAspetto di ricevere i dati ")
        contConn=0 #inizializza il contatore
        while True: #se la connessione è attiva esegue i comandi
            dati = sock_service.recv(2048) #aspetta la richiesta dal client
            contConn+=1 #aumenta il contatore di 1
            if not dati: #controlla che dai abbia un valore
                print("Fine dati dal client. Reset")
                break #se dati non ha valore chiude la connessione
            
            dati = dati.decode() #se dati ha valore lo decodifica
            print("Ricevuto: '%s'" % dati) 
            if dati=='0': 
                print("Chiudo la connessione con " + str(addr_client))
                break #se dati ha valore '0' chiude la connessione
            
            operazione, n1, n2 = dati.split(";") #.split divide la stringa al carattere indicato#Vari if per selezionare l'operazione che il client ha inserito
            if operazione == "piu": #controllo operazione +
                risultato = int(n1) + int(n2)
            if operazione == "meno": #controllo operazione -
                risultato = int(n1) - int(n2)
            if operazione == "per": #controllo operazione *
                risultato = int(n1) * int(n2)
            if operazione == "diviso": #controllo operazione /
                risultato = int(n1) / int(n2)

            dati = "Il risultato è: " + str(risultato) #output dell'operazione

            dati = dati.encode() #codifica la risposta

            sock_service.send(dati) #invia i dati codificati
    sock_service.close() #fine ascolto del server

def avvia_server(indirizzo,porta): #crea un endpoint di ascolto (sock_listen) dal quale accettare connessioni in entrata
    sock_listen = socket.socket() #
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #
    sock_listen.bind((indirizzo, porta)) #
    sock_listen.listen(5) #
    print("Server in ascolto su %s." % str((indirizzo, porta))) #il server è in ascolto e in grado di ricevere richieste di connessione
    ricevi_comandi(sock_listen)

if __name__=='__main__': #consente al nostro codice di capire se stia venendo eseguito come script a se stante, o se è stato richiamato come modulo da qualche programma per usare una o più delle sue varie funzioni e classi
    avvia_server(SERVER_ADDRESS,SERVER_PORT)