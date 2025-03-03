# importare il modulo:
import oracledb

# connessione al db on localhost:
conn= oracledb.connect(
    user= "SYS",
    password= "",
    dsn= "localhost:1521/xe",
    mode= oracledb.SYSDBA
)
print(conn)

cursor= conn.cursor()

# MODIFICA DEI RECORD:
#esempio --> voglio modificare l'età di chi ha 30 

update_query= "UPDATE anagrafica SET eta=31 WHERE eta=30"
cursor.execute(update_query)
conn.commit()

# controllo il risultato della modifica:

select_sql= "SELECT * FROM anagrafica"

# eseguo la select:

cursor.execute(select_sql)

risultato= cursor.fetchall() # restuisce una lista

for riga in risultato:
    print(riga)
    
# voglio aggiungere una nuova colonna alla tabella anagrafica:
# voglio aggiungere la colonna citta:

alter_query= "ALTER TABLE angarafica ADD citta VARCHAR2(15)"

cursor.execute(alter_query)
conn.commit()

# aggiungo dati nella colonna città (aggiorno i record già esistenti):
insert_citta= "UPDATE anagrafica SET citta=:1 WHERE cognome=:2"

valori= [("Roma", "Rossi"),("Milano", "Gialli"), ("Napoli", "Blu"), ("Bari", "Verdi")]

cursor.executemany(insert_citta, valori )
conn.commit()

# controllo il risultato della modifica:

select_sql2= "SELECT * FROM anagrafica"

# eseguo la select:

cursor.execute(select_sql2)

risultato2= cursor.fetchall() # restuisce una lista

for riga in risultato2:
    print(riga)
    