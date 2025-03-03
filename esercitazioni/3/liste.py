'''
Esercizio 1
Creare una lista vuota e assegnarla a una variabile.
'''
print("-----------------------ESERCIZIO 1------------------------")
list = []
print(list)

'''
Esercizio 2
Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.
'''
print("-----------------------ESERCIZIO 2------------------------")
list2 = [1,2,3,4,5]
for i in list2:
    list = list2
print(list)

'''
Esercizio 3
Accedere all'elemento con indice 2 della lista precedente.
'''
print("-----------------------ESERCIZIO 3------------------------")
print(list[2]) 

'''
Esercizio 4
Aggiungere un nuovo elemento "6" alla lista precedente.
'''
print("-----------------------ESERCIZIO 4------------------------")
list.append(6)
for num in list:
    print(num)

'''
Esercizio 5
Rimuovere l'elemento con indice 3 dalla lista precedente.
'''
print("-----------------------ESERCIZIO 5------------------------")
list.pop(3)
print(list)

'''
Esercizio 6
Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.
'''
print("-----------------------ESERCIZIO 6------------------------")
for i in list[:3]:
    list6 = list[i]
    print(i)

'''
Esercizio 7
Ordinare la lista precedente in ordine decrescente. Per svolgere l’esercizio, informarsi sul metodo sorted()
'''
print("-----------------------ESERCIZIO 7------------------------")
list7 = sorted(list, reverse=True)
for i in list7:
    print(i)