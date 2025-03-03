-- INNER JOIN 
-- serve a unire due o più tabelle purchè abbiano almeno una colonna in comune
--ESEMPIO: VOGLIO VISUALIZZARE NOME, COGNOME E STIPENDIO DEI DIPENDENTI:

--sintassi abbreviata:
SELECT dbetl.anagrafe_dipendenti.nome, dbetl.anagrafe_dipendenti.cognome, dbetl.stipendi_dipen.stipendio
FROM dbetl.anagrafe_dipendenti, dbetl.stipendi_dipen
WHERE dbetl.anagrafe_dipendenti.id_anag = dbetl.stipendi_dipen.id_anag
AND dbetl.anagrafe_dipendenti.sesso = 'U';

-- sintassi completa:
SELECT dbetl.anagrafe_dipendenti.nome, dbetl.anagrafe_dipendenti.cognome, dbetl.stipendi_dipen.stipendio
FROM dbetl.anagrafe_dipendenti INNER JOIN dbetl.stipendi_dipen
ON dbetl.anagrafe_dipendenti.id_anag = dbetl.stipendi_dipen.id_anag
WHERE dbetl.anagrafe_dipendenti.sesso = 'U';

--UTILIZZO DI CORRELATION NAME: alias assegnato alla tabella:

SELECT A.nome, A.cognome, S.stipendio
FROM dbetl.anagrafe_dipendenti A, dbetl.stipendi_dipen S
WHERE A.id_anag = S.id_anag
AND A.sesso = 'U';

---- correlation name con sintassi completa
SELECT A.nome, A.cognome, S.stipendio
FROM dbetl.anagrafe_dipendenti A INNER JOIN dbetl.stipendi_dipen S
ON A.id_anag = S.id_anag
WHERE A.sesso = 'U';

--- ESEMPIO DI INNER JOIN CON 3 TABELLE
--voglio titolo, id_att, codice film e cognome

SELECT F.titolo, R.id_att , R.cod_film, A.cognome
FROM dbetl.film F, DBETL.recita R, dbetl.attori A
WHERE F.cod_film = R.cod_film
    AND A.id_att = R.id_att
AND F.titolo LIKE 'F%';

--OUTER JOIN: si usa quando vogliamo includere anche dati senza corrispondenza (null)

-- LEFT OUTER JOIN --> include dati della tabella specificata a sinistra
--esempio: voglio denominazione e descrizione dei prodotti :

SELECT F.denominazione, P.descr
FROM dbetl.market_fornitori F  RIGHT OUTER JOIN dbetl.market_prodotti P
ON f.id_fornitore = p.id_fornitore
ORDER BY p.descr DESC;

-- FULL OUTER  JOIN  --> (left + right) 

SELECT F.denominazione, P.descr
FROM dbetl.market_fornitori F  FULL OUTER JOIN dbetl.market_prodotti P
ON f.id_fornitore = p.id_fornitore
ORDER BY p.descr DESC;

-- INTERSECT --> serve a vedere i dati in comune tra due tabelle 
SELECT ID_cliente
From DBETL.hotel_clienti
INTERSECT
SELECT ID_cliente
From DBETL.hotel_PREN;

-- MINUS --> serve a vedere i dati NON comuni tra le tabelle
-- quando utilizziamo MINUS, mettiamo prima la select sulla tabella con più dati
SELECT ID_cliente
From DBETL.hotel_PREN
MINUS
SELECT ID_cliente
From DBETL.hotel_clienti;

--- concatenazione di stringhe:
SELECT anag_cognome || ' ' || anag_nome || ' ha lo stipendio di: '|| anag_stip || ' euro mensili' AS stringa
FROM dbetl.anag_cli

