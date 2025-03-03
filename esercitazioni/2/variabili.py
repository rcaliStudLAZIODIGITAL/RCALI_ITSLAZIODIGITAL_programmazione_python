print("-----------------------ESERCIZIO 1------------------------")
nome = "Nome"
print(nome)

print("-----------------------ESERCIZIO 2------------------------")
eta = 50
print(eta)

print("-----------------------ESERCIZIO 3------------------------")
PI = 3,14159
print(PI)

print("-----------------------ESERCIZIO 4------------------------")
lenght = 9
print(lenght)
lenght = 15
print(lenght)

print("-----------------------ESERCIZIO 5------------------------")
cognome="Cognome"
nome_completo = nome, cognome
print(nome_completo)

print("-----------------------ESERCIZIO 6------------------------")
eta_fut = eta+10
print(eta_fut)

print("-----------------------ESERCIZIO 7------------------------")
anno_di_nascita = 1900
print(nome,cognome,"anno",anno_di_nascita)
nome = "nome"
cognome="cognome"
anno_di_nascita = 1600
print(nome,cognome,"anno",anno_di_nascita)

print("-----------------------ESERCIZIO 8------------------------")
from datetime import datetime
anno_attuale = datetime.now().year
eta_attuale = anno_attuale - anno_di_nascita
print("Età attuale:",eta_attuale)