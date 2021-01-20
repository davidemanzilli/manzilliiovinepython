from random import randint


f = open("dati.txt", 'w')


dati = ""

# il primo ciclo serve a creare le singole righe
for riga in range(100):

    # il secondo ciclo serve a compulare la singola riga
    for elemento in range(1):

        # aggiungo il numero casuale e inserisco uno spazio in coda
        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
        
    # aggiungo un terminatore di riga, così il secondo rigo va a capo
    dati = dati + "\n"


print(dati)

# scrivo la stringa nel file
f.write(dati)

# chdiuamo sempre il file
f.close()