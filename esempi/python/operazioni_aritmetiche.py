# possiamo utilizzare operatori arimetici per fare calcoli:

x= 9
y= 3

# + --> somma
print("somma ",x+y)

# - --> sottrazione
print("sottrazione ",x-y)

# / --> divisione 
print("divisione ", x/y)

# * --> moltiplicazione
print("moltiplicazione" ,x*y)

# % --> modulo --> resto della divisione
print("modulo ", x%y) 

# ** --> potenza
print("potenza ", x**y) 

 # // --> floor Division --> arrotonda per difetto il risultato della divisione
x= 15 
y= 7

print("floor Division" , x//y)

# possiamo fare delle espressioni:

espressione=(x+y)*2
print(espressione)

# OPERATORI DI ASSEGNAMENTO:

# se voglio fare: 
x= 5 
x= x+2
print(x)

#posso utilizzare += per avere lo stesso risultato:
x= 5
x+= 2 # x = se stesso +2
print(x)

# per ogni operatore aritmetico abbiamo l'operatore di assegnamento:
# -= , *=, /= ...

# ALCUNI METODI PER OPERAZIONI SEMPLICI

x= 5
y= 10
z= 15

# min()---> estrapola il minore da un elenco di numeri
num_minore= min(x,y,z)
print(num_minore)
 
# max() --> estrapola il maggiore da un elenco di numeri
num_maggiore= max(x,y,z)
print(num_maggiore)

# abs() ---> restituisce il valore assoluto di un numero:
k = -10 
numero_assoluto = abs(k)

print(numero_assoluto)

# pow() --> potenza
potenza= pow(x, 2)
print(potenza)

