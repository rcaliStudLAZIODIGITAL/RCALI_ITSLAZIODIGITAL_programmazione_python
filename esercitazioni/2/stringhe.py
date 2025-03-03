print("-----------------------ESERCIZIO 1------------------------")
stringa = "ciao mondo"
stringa_upper = stringa.upper()
print(stringa_upper)

print("-----------------------ESERCIZIO 2------------------------")
stringa = "Benvenuti a Roma"
stringa_lower = stringa.lower()
print(stringa_lower)

print("-----------------------ESERCIZIO 3------------------------")
stringa = "Il meglio deve ancora venire"
lista_parole = stringa.split()
print(lista_parole)

print("-----------------------ESERCIZIO 4------------------------")
stringa = "Hello World"
stringa_replace = stringa.replace("World", "Python")
print(stringa_replace)

print("-----------------------ESERCIZIO 5------------------------")
stringa = " Ciao "
stringa_strip = stringa.strip()
print(stringa_strip)

print("-----------------------ESERCIZIO 6------------------------")
stringa = "abcdefg"
primi_tre = stringa[:3]
print(primi_tre)

print("-----------------------ESERCIZIO 7------------------------")
stringa = "Python"
inizia_con_py = stringa.startswith("Py")
print(inizia_con_py)

print("-----------------------ESERCIZIO 8------------------------")
stringa = "Ciao mondo"
conteggio_o = stringa.count("o")
print(conteggio_o)

print("-----------------------ESERCIZIO 9------------------------")
stringa = "Ciao mondo"
ultimi_cinque = stringa[-5:].upper().replace("O", "K")
print(ultimi_cinque)