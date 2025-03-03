# INSTALLARE IL PACCHETTO: pip install oracledb

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

# creare un cursore per porter eseguire dei comandi nel db:

cursor= conn.cursor()

#creo una tabella:

cursor.execute("""
               CREATE TABLE anagrafica(
                   nome VARCHAR2(20),
                   cognome VARCHAR2(20),
                   eta INT 
               )
               """)
#esito della creazione:
print("tabella creata!")

# chiudo cursore e connessione al db:

cursor.close()
conn.close()
