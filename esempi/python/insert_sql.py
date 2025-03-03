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

# dichiaro una query "generica" per l'inserimento dei dati in tabella:

sql= " INSERT INTO anagrafica (nome, cognome, eta) VALUES (:1, :2, :3 )"
# :1, :2, :3 sono placeholders --> verranno sotituiti con i valori reali

#dichiaro i valori da inserire:
valori= ("Mario", "Rossi", 30)

# eseguo la query:

cursor.execute(sql,valori)

#salvo le modifiche nella tabella:
conn.commit()

#stampo l'esito dell'inserimento:
print("record inseriti con successo")

# INSERIMENTO MULTIPLO:

# dichiaro una lista di tuple:
valori2= [("Giulio", "Verdi", 18), ("Marco", "Gialli", 20),("Marta", "Blu", 25),]

# per l'inserimento multiplo dobbiamo usare la funzione executemany()

cursor.executemany(sql, valori2)
conn.commit()

#stampo l'esito dell'inserimento:
print("record inseriti con successo")

# chiudo cursore e connessione al db:

cursor.close()
conn.close()
