#Esempio: provo a stampare una variabile non definita
# try:
#     print(x)
# except NameError:
#     print("non hai dichiarato nessuna variabile!")
    
# si possono inserire più blocchi except per gestire più errori:
try:
    x= 100
    y= "1"
    somma= x+y

    print(x)
    print(somma)
except NameError:
    print("variabile non dichiarata!")
except TypeError:
    print("non puoi sommare numeri con stringhe")
    
# possiamo utilizzare anche un blocco else:

try:
    divisione= 50/0
except ZeroDivisionError:
    print("non si può dividere per zero")
else:
    print(divisione)

# esiste anche il blocco finally --> viene eseguito in ogni caso (se si presenta l'errore o se non si presenta )

#esempio: provo a scrivere in un file aperto in modalità lettura
try:
    f= open("prova.txt", "r")
    f.write("testo da scrivere")
except:
    print("non puoi scrivere nel file se sei in modalità lettura")
finally:
    f.close()
    print("file chiuso")

# lanciare eccezioni personalizzate:

def accesso_maggiorenni(eta):
    if eta < 18:
        raise ValueError
    else:
        print("accesso consentito")
        
try:
    accesso_maggiorenni(18)
except ValueError:
    print("non sei maggiorenne, accesso negato!")
    