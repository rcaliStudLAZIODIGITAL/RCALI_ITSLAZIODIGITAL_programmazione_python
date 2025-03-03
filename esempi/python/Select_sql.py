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

# variabile con istruzione select:

select_sql= "SELECT * FROM anagrafica"

# eseguo la select:

cursor.execute(select_sql)

risultato= cursor.fetchall() # restuisce una lista

for riga in risultato:
    print(riga)
    

# allo stesso modo di sql, anche qui posso eseguire query più complesse:

select_sql2= """SELECT nome, cognome 
                FROM anagrafica
                WHERE eta <30"""
# eseguo la select:

cursor.execute(select_sql2)

risultato2= cursor.fetchall() # restuisce una lista

for riga in risultato2:
    print(riga)

