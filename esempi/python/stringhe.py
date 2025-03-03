# per dichiare una stringa possiamo utilizzare doppi o songoli apici

x= "ciao"
y= 'ciao'
frase= "il mio soprannome è 'ciccio'"

# si possono dichiarare stringhe miltiriga:

z= """questa è
una stringa multiriga"""

# possiamo accedere ad ogni carattere della stringa
print("il primo carattere della stringa in x è: ", x[0])

# possiamo contare da quanti caratteri è composta la stringa
# si utilizza la funzione len()
print("la stringa x è composta da ", len(x) , " caratteri")

# possiamo utilizzare intervalli per prendere porzioni di stringa:

animale= "cavallo"

print(animale[:3]) # da 0 a 3 ( 3 escluso!)

print(animale[2:5]) # 5 escluso!!

print(animale [2:]) # da indice 2 a fine stringa

# posso utilizzare anche indici negativi
print(animale[-4:])

#ALCUNE FUNZIONI DI BASE PER MODIFICARE LE STRINGHE:

str= " Casa "

# upper() --> trasforma la stringa in MAIUSCOLO
print(str.upper())

#lower() --> trasforma la stringa in Minuscolo
print(str.lower())

#strip() --> toglie spazi ad inizio e fine stringa
print(str.strip())

#replace() --> serve a sostituire i caratteri in una stringa 
print(str.replace("a", "o"))

#posso indicare anche più di un carattere da sostituire
print(str.replace("asa", "oro"))

#posso utilizzare più funzioni in una sola istruzione:
print(str.strip().replace("asa", "oro").upper())

stringa3= "ciao"


