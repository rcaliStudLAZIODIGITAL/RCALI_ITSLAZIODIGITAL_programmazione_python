--Esercitazione 1 Linguaggio SQL

/*1.1 Istruzione Select.
Accedendo alla Tabella DIPENDENTI, elencare il codice dipendente, il cognome, la data di nascita, IL BONUS e lo stipendio per tutti i 
dipendenti che guadagnano più di € 500 di bonus. Ordina i dati in base alla colonna STIPENDIO in modalità decrescente.*/
SELECT COD_DIP, COGNOME DT_NASCITA, BONUS, STIPENDIO FROM DIPENDENTI
WHERE BONUS > 500
ORDER BY STIPENDIO DESC;

/*1.2 Istruzione Select
Accedendo alla Tabella DIPENDENTI, elencare il COGNOME, il NOME ed il COD_UFF per tutti i dipendenti che nel proprio nome hanno il 
carattere "i" minuscolo come lettera finale ordinando i dati in base al COD_UFF in modalità discendente e all'interno dello stesso 
ufficio per i cognomi in modalità decrescente.*/
SELECT COGNOME, NOME, COD_UFF, STIPENDIO FROM DIPENDENTI
WHERE TRIM(NOME) LIKE '%i'
ORDER BY COGNOME DESC, COD_UFF DESC;

/*1.3 Istruzione Select.
Accedendo alla Tabella DIPENDENTI, visualizzare la colonna LIVELLO_ISTRUZIONE eliminando dal risultato i valori duplicati; il risultato dovrà essere ordinato 
in modo discendente per la colonna selezionata.*/
SELECT DISTINCT LIVELLO_ISTRUZIONE FROM DIPENDENTI
ORDER BY LIVELLO_ISTRUZIONE DESC;

/*1.4 Istruzione Select.
Accedendo alla Tabella TASK_DIPENDENTI che contiene le attività, elencare i dipendenti indicando il proprio codice identificativo ( COD_DIP ) ed i progetti a loro 
assegnati visualizzando però solo quelli con COD_DIP maggiore o uguale a 100 e che sono assegnati ai progetti compresi tra quelli nel range letterale tra I ed N.
Prestare attenzione in quanto la colonna COD_DIP è definite come CHAR anche se all’interno contiene valori numerici.
Il risultato della Query dovrà essere ordinato in modo ascendente per la colonna COD_PROG; per l’ordinamento utilizzare i numeri di posizione della colonna della 
Query e non il nome della colonna.*/
SELECT COD_DIP, COD_PROG FROM TASK_DIPENDENTI
WHERE COD_DIP >=100 AND COD_PROG BETWEEN 'I' AND 'N'
ORDER BY COD_DIP;

/*1.5 Istruzione Select.
Accedendo alla Tabella DIPENDENTI, elencare il COGNOME, lo STIPENDIO ed il BONUS dei soli dipendenti uomini assunti tra il 1° agosto del 2023 ed il 31 dicembre 2024.
I dati dovranno essere ordinati per COGNOME in modalità ascendente*/
SELECT COGNOME, STIPENDIO, BONUS, DT_ASSUNZ FROM DIPENDENTI
WHERE SESSO = 'U' 
  AND DT_ASSUNZ BETWEEN TO_DATE('2023-08-01', 'YYYY-MM-DD') AND TO_DATE('2024-12-31', 'YYYY-MM-DD')
ORDER BY COGNOME ASC;

/*1.6 Istruzione Select con operatori logici.
Accedendo alla Tabella DIPENDENTI, elencare il COGNOME, lo STIPENDIO, il BONUS e le provvigioni ( colonna COMMISSIONI ) per tutti i 
dipendenti con uno stipendio superiore a € 3000 ed un bonus di € 400 oppure per tutti i dipendenti con un bonus maggiore di € 500 e 
una provvigione inferiore a € 300. 
Il Result Set dovrà essere ordinato per cognome in modalità discendente e si richiede inoltre di prestare molta attenzione 
all’utilizzo di eventuali parentesi nella WHERE CONDITION.*/
SELECT COGNOME, STIPENDIO, BONUS, COMMISSIONI FROM DIPENDENTI
WHERE (STIPENDIO > 3000 AND BONUS = 400)
	OR (BONUS > 500 AND COMMISSIONI < 300)
ORDER BY COGNOME DESC;

/*1.7 Istruzione Select con operatori logici.
Accedendo alla Tabella DIPENDENTI, elencare il COGNOME, lo STIPENDIO, il BONUS e le provvigioni ( colonna COMMISSIONI ) per tutti i 
dipendenti con uno stipendio superiore a € 2500, un bonus minore di € 400 o maggiore di € 500 e una provvigione superiore a € 300; 
il risultato dovrà essere ordinato in modo discendente per la colonna COGNOME.
Anche per questa Query si richiede inoltre di prestare molta attenzione all’utilizzo di eventuali parentesi nella WHERE CONDITION.*/
SELECT COGNOME, STIPENDIO, BONUS, COMMISSIONI FROM DIPENDENTI
WHERE STIPENDIO > 2500 AND COMMISSIONI < 300;

/*1.8 Istruzione Select con ricerca parziale e lista valori.
Accedendo alla Tabella TASK  Dipendenti, si richiede di visualizzare i dati per tutti i progetti che hanno un COD_PROG che inizia con 
A ed i TASK con id 10, 80 o 180 associati ad essi.
Le colonne dovranno essere la COD_PROG, la NUM_TASK, la DT_INI_TASK e la DT_FIN_TASK. 
Ordinare il risultato per numero di attività in modalità ascendente.*/
SELECT COD_PROG, NUM_TASK, DT_INI_TASK, DT_FIN_TASK FROM TASK_DIPENDENTI
WHERE COD_PROG LIKE 'A%' AND NUM_TASK IN (10, 80, 180)
ORDER BY NUM_TASK ASC;

/*1.9 Istruzione Select.
Accedendo alla Tabella UFFICI, elencare il codice del responsabile dell’ufficio ed il codice dell’ufficio per tutti gli uffici a cui 
è stato assegnato un dipendente in qualità di responsabile., l'elenco risultante dovrà essere ordinato per la colonna del responsabile 
in modalità ascendente.*/
SELECT RESP_UFF, COD_UFF FROM UFFICI
WHERE RESP_UFF IS NOT NULL
ORDER BY RESP_UFF ASC;

/*1.10 Istruzione Select con gestione della data.
Accedendo alla Tabella DIPENDENTI, si richiede di elencare il cognome, lo stipendio e la provvigione per tutti i dipendenti con uno 
stipendio superiore a € 2500 ed assunti dopo il 2022. Ordinare i dati per la colonna COGNOME in modalità ascendente.
Per questa Query utilizzare la funzione EXTRACT.*/
SELECT COGNOME, STIPENDIO, COMMISSIONI FROM DIPENDENTI
WHERE STIPENDIO > 2500 AND EXTRACT(YEAR FROM DT_ASSUNZ) > 2022
ORDER BY COGNOME ASC;

/*1.11 Istruzione Select con ricerca ad intervalli.
Accedendo alla Tabella DIPENDENTI, visualizzare il COD_DIP, il COGNOME, lo STIPENDIO ed il BONUS per tutti i dipendenti che hanno un 
bonus compreso tra € 800 e € 900; ordinare i dati per BONUS in modalità ascendente e per codice dipendente sempre in modo ascendente.*/
SELECT COD_DIP, COGNOME, STIPENDIO, BONUS FROM DIPENDENTI
WHERE BONUS BETWEEN 800 AND 900
ORDER BY BONUS ASC, COD_DIP ASC;

/*1.12 Istruzione Select con ricerca ad intervalli.
Accedendo alla Tabella DIPENDENTI, visualizzare il COD_DIP, il COGNOME, lo STIPENDIO ed il COD_UFF di tutti i dipendenti negli uffici 
compresi tra A00 e C01; ordinare i dati in ordine alfabetico per cognome e per codice dipendente in modo discendente.*/
SELECT COD_DIP, COGNOME, STIPENDIO, COD_UFF FROM DIPENDENTI
WHERE COD_UFF BETWEEN 'A00' AND 'C01'
ORDER BY COGNOME ASC, COD_DIP DESC;

/*1.13 Istruzione Select con ricerca parziale.
Accedendo alla Tabella PROGETTI, elencare tutti i codici progetto ed il loro relativo nome ordinando i dati per codice progetto in modalità ascendente; tra i criteri di selezione vi è quello di filtrare le righe che hanno all’interno del nome del progetto la parola “Sviluppo”.*/
SELECT COD_PROG, NOME_PROG FROM PROGETTI
WHERE NOME_PROG LIKE '%Sviluppo%'
ORDER BY COD_PROG ASC;

/*1.14 Istruzione Select con ricerca parziale.
Accedendo alla Tabella UFFICI, visualizzare il COD_UFF ed il NOME_UFFICIO relativo per i soli uffici che hanno il valore uno come carattere centrale considerando che la colonna COD_UFF è un CHAR(3); i dati dovranno essere ordinati per codice ufficio in modo discendente.*/
SELECT COD_UFF, NOME_UFFICIO FROM UFFICI
WHERE SUBSTR(COD_UFF, 2, 1) = '1'
ORDER BY COD_UFF DESC;

/*1.15 Istruzione Select con doppia negazione.
Accedendo alla Tabella DIPENDENTI, visualizzare COGNOME, NOME, INIZIALI e STIPENDIO per tutti i dipendenti che non ricoprono il ruolo di Amministratore e Manager, per tutti quelli che non hanno nella colonna iniziale i valori FL e TC e che hanno uno stipendio compreso tra i € 2500 ed i € 2630. Ordinare i dati per stipendio partendo dal più alto.*/
SELECT COGNOME, NOME, INIZIALI, STIPENDIO FROM DIPENDENTI
WHERE RUOLO NOT IN ('Amministratore', 'Manager') 
	AND INIZIALI NOT IN ('FL', 'TC') 
	AND STIPENDIO BETWEEN 2500 AND 2630
ORDER BY STIPENDIO DESC;

/*1.16 Istruzione Select.
Elencare il NOME_SALA di tutte le sale cinematografiche presenti nella Tabella SALE, che hanno nel proprio nome la lettera A nella terza e nella sesta posizione.
I dati dovranno essere ordinati in modo ascendente.*/
SELECT NOME_SALA FROM SALE
WHERE SUBSTR(NOME_SALA, 3, 1) = 'A' AND SUBSTR(NOME_SALA, 6, 1) = 'A'
ORDER BY NOME_SALA ASC;

/*1.17 Istruzione Select con AND ed OR e ricerca per intervalli.
Accedendo alla Tabella FILM, elencare TITOLO e DATA_PROD per quei film del genere Drammatico e di nazionalità americana o spagnola prodotti tra il primo gennaio del 2000 ed il 31 dicembre del 2007; la lista dovrà essere ordinata per la DATA_PROD in modalità decrescente partendo quindi dal più recente.*/
SELECT TITOLO, DATA_PROD FROM FILM
WHERE GENERE = 'Drammatico'
  AND NAZIONALITA IN ('USA', 'Spagna')
  AND DATA_PROD BETWEEN TO_DATE('2000-01-01','YYYY-MM-DD') AND TO_DATE('2007-12-31','YYYY-MM-DD')
ORDER BY DATA_PROD DESC;

/*1.18 Istruzione Select con ricerca mirata di valori.
Accedendo alla Tabella FILM, elencare il TITOLO, la DATA_PROD ed il REGISTA per quei film che sono stati prodotti tra il 1997 ed il 2001 ma solo nei mesi compresi tra Aprile e Settembre. 
Dal risultato dovranno essere estromessi tutti quelli dei generi Drammatico e Romantico. 
Il risultato finale dovrà essere ordinato per il TITOLO in modo ascendente.*/
SELECT TITOLO, DATA_PROD, REGISTA FROM FILM
WHERE DATA_PROD BETWEEN TO_DATE('1997-01-01','YYYY-MM-DD') AND TO_DATE('2001-12-31','YYYY-MM-DD')
  AND EXTRACT(MONTH FROM DATA_PROD) BETWEEN 4 AND 9
  AND GENERE NOT IN ('Drammatico', 'Romantico')
ORDER BY TITOLO ASC;

/*1.19 Istruzione Select.
Accedendo alla Tabella VOLI, trovare le città da cui partono voli diretti a Roma ordinate alfabeticamente in modo ascendente.*/
SELECT DISTINCT CITTA_PARTENZA FROM VOLI
WHERE CITTA_ARRIVO = 'Roma'
ORDER BY CITTA_PARTENZA ASC;

/*1.20 Istruzione Select e controllo di valori sconosciuti.
Accedendo alla Tabella AEROPORTI, trovare le città con aeroporti di cui non è noto il numero di piste ordinando i dati per CITTA in modalità ascendente.*/
SELECT CITTA FROM AEROPORTI
WHERE NUM_PISTE IS NULL
ORDER BY CITTA ASC;
/*1.21 Istruzione Select con ricerca mirata e operatori logici.
Accedendo alla Tabella VOLI, elencare le colonne ID_VOLO, CITTA_PARTENZA, CITTA_ARRIVO e TIPO_AEREO degli aerei E49I3, AZ94P e CK13L che sono partiti da Milano e che sono atterrati in tutti gli aeroporti esclusi quelli di Las Vegas, Vienna e Barcellona. Ordinare i dati per la colonna TIPO_AEREO in modalità ascendente.*/
SELECT ID_VOLO, CITTA_PARTENZA, CITTA_ARRIVO, TIPO_AEREO FROM VOLI
WHERE TIPO_AEREO IN ('E49I3', 'AZ94P', 'CK13L')
  AND CITTA_PARTENZA = 'Milano' AND CITTA_ARRIVO NOT IN ('Las Vegas', 'Vienna', 'Barcellona')
ORDER BY TIPO_AEREO ASC;

/*1.22 Istruzione Select.
Accedendo alla Tabella DIPENDENTI, visualizzare il COGNOME, il NOME ed il NUM_TEL_INTERNO del proprio ufficio per quei dipendenti assunti nei mesi di marzo, giugno, settembre e dicembre che hanno uno stipendio tra € 1670 ed € 2550 mensili; i dati dovranno essere ordinati per NOME in modalità discendente.*/
SELECT COGNOME, NOME, NUM_TEL_INTERNO FROM DIPENDENTI
WHERE STIPENDIO BETWEEN 1670 AND 2550
  AND EXTRACT(MONTH FROM DT_ASSUNZ) IN (3, 6, 9, 12)
ORDER BY NOME DESC;

/*1.23 Istruzione Select con estrazione per intervalli e domini.
Accedendo alla Tabella DIPENDENTI, estrarre il COGNOME, il NOME e la DT_ASSUNZ di tutti i dipendenti che non si chiamano Mirko, Dario, Andrea, Daniele e Paolo e che sono stati assunti nei giorni del mese che vanno dal giorno 11 al giorno 14. Ordinare i dati in base alla colonna DT_ASSUNZ in modalità discendente.*/
SELECT COGNOME, NOME, DT_ASSUNZ FROM DIPENDENTI
WHERE NOME NOT IN ('Mirko', 'Dario', 'Andrea', 'Daniele', 'Paolo')
  AND EXTRACT(DAY FROM DT_ASSUNZ) BETWEEN 11 AND 14
ORDER BY DT_ASSUNZ DESC;

/*1.24 Istruzione Select.
Estrarre dalla Tabella HOTEL_PREN le colonne ID_CLIENTE e DT_INI_PREN per i clienti censiti con i codici 3, 5 e 6 e che hanno soggiornato in Albergo per almeno 4 giorni fino ad un massimo di 10.
I dati dovranno essere ordinati per ID_CLIENTE.*/
SELECT ID_CLIENTE, DT_INI_PREN FROM HOTEL_PREN
WHERE ID_CLIENTE IN (3, 5, 6) AND DURATA BETWEEN 4 AND 10
ORDER BY ID_CLIENTE ASC;

/*1.25 Istruzione Select.
Estrarre dalla Tabella DIPENDENTI le colonne COD_DIP, COGNOME, NOME e STIPENDIO di tutti quei dipendenti che nel ruolo di appartenenza hanno il carattere “e” in quinta posizione; ordinare i dati in base al COGNOME in modalità ascendente.*/
SELECT COD_DIP, COGNOME, NOME, STIPENDIO FROM DIPENDENTI
WHERE SUBSTR(RUOLO, 5, 1) = 'e'
ORDER BY COGNOME ASC;

/*1.26 Select con funzioni Sql che agiscono su più righe.
Si richiede di estrarre la somma totale degli stipendi di quei dipendenti che lavorano nell’ufficio B01; i dati dovranno essere estratti dalla Tabella DIPENDENTI.
Si richiede inoltre di rinominare la colonna del ResultSet con SOMMA_STIPENDI_UFF_B01.*/
SELECT SUM(STIPENDIO) AS SOMMA_STIPENDI_UFF_B01
FROM DIPENDENTI
WHERE COD_UFF = 'B01';

/*1.27 Select con funzioni Sql che agiscono su più righe.
Si richiede di estrarre il numero totale delle righe dalla Tabella DIPENDENTI per quei dipendenti che:
Ricoprono un ruolo contenente la parola Manager
Che sono stati assunti nei soli mesi di Febbraio, Agosto
Che hanno nel nome, in qualsiasi posizione, la lettera o minuscola
Le cui Commissioni sono comprese tra € 200 e € 400
Si richiede inoltre di rinominare la colonna del ResultSet con TOTALE_DIPENDENTI.*/
SELECT COUNT(*) AS TOTALE_DIPENDENTI FROM DIPENDENTI
WHERE RUOLO LIKE '%Manager%'
  AND EXTRACT(MONTH FROM DT_ASSUNZ) IN (2, 8)
  AND LOWER(NOME) LIKE '%o%'
  AND COMMISSIONI BETWEEN 200 AND 400;

/*1.28 Select con funzioni Sql che agiscono su più righe.
Si richiede di estrarre lo stipendio minimo, lo stipendio massimo e la media degli stipendi, dalla Tabella DIPENDENTI per quei dipendenti che:
Ricoprono un ruolo contenente la parola Manager
Che sono stati assunti nei soli mesi di Febbraio, Agosto, Settembre, Novembre e Dicembre
Che hanno nel nome, in qualsiasi posizione, la lettera o minuscola
Le cui Commissioni sono comprese tra € 200 e € 400
Si richiede inoltre di rinominare la colonna del ResultSet con STIPENDIO_MINIMO, STIPENDIO_MASSIMO e STIPENDIO_MEDIO.*/
SELECT MIN(STIPENDIO) AS STIPENDIO_MINIMO,
       MAX(STIPENDIO) AS STIPENDIO_MASSIMO,
       AVG(STIPENDIO) AS STIPENDIO_MEDIO
FROM DIPENDENTI
WHERE RUOLO LIKE '%Manager%'
  AND EXTRACT(MONTH FROM DT_ASSUNZ) IN (2, 8, 9, 11, 12)
  AND LOWER(NOME) LIKE '%o%'
  AND COMMISSIONI BETWEEN 200 AND 400;