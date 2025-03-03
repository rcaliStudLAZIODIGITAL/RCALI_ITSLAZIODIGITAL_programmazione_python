# REGULAR EXPRESSION (RegEx) --> è un pattern , sequenza di caratteri che forma un modello di ricerca

# dobbiamo importare il modulo:
import re 

# FUNZIONI PRINCIPALI:

stringa= "la pioggia cade sulla spiaggia"

# search("pattern", stringa) --> restituisce un match object se trova la corrispondenza, altrimenti restituisce None
# possiamo fare il cast in booleano, per farci restituire true o false:

print(bool(re.search("ia",stringa)))

# findall() --> restuisce una lista contenente tutte le corrispondenze trovate:
print(re.findall("og", stringa))

# sub() --> sosttuisce le corrispondenze trovate con un altro carattere
# esempio: voglio sostituire lo spazio ( \s) con _

s= re.sub("\s", "_", stringa)
print(s)

# sub() ha anche un parametro numerico che indica quante corrispendenze voglio sostituire:

s1= re.sub("\s", "_", stringa,2)
print(s1)

# I METACARATTERI:

# [] --> definiscono un set di caratteri
# esempio: trovare tutti i caratteri minuscoli in ordine alfabetico compresi tra a-m

a= re.findall("[a-m]", stringa)
print(a)

# ^ --> rappresenta "comincia con.."
# es: controllare se la stringa comincia con "la"

if re.findall("^la", stringa):
    print("si")
else:
    print("no")

# $ --> rappresenta "finisce con.."
# es: controllare se la stringa finisce con "la"

if re.findall("$la", stringa):
    print("si")
else:
    print("no")

# | ---> oppure
# esempio --> voglio controllare se la stringa contiene sole o pioggia

c= re.findall("sole|pioggia", stringa)
print(c)

# . --> wildcard -->"maschera caratteri"
# esempio: voglio cercare una sequenza che comincia con "sp" seguito da due caratteri  e da "g" 
d= re.findall("sp..g", stringa)
print(d)


# SEQUENZE SPECIALI:

stringa2= " la pioggia cadde sulla spiaggia nel 2010!!"

# \d  --- > numeri (da 1 a 9)
e= re.findall("\d", stringa2)
print(e)

#\D --> caratteri non numerici
v= re.findall("\D", stringa2)
print(v)

#\W --> caratteri non alfabetici ( spazi, caratteri speciali, segni di punteggiatura)
w= re.findall("\W", stringa2)
print(w)

# la funzione compile(), mi permette di creare pattern riutilizzabili:

pattern= re.compile("ia")
risultato= pattern.findall(stringa2)
print(risultato)