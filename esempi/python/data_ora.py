# Modulo datetime --> utile a lavorare con oggetti "data/ora"

import datetime

#  creare un oggetto con data e ora attuale:
x= datetime.datetime.now()
print(x)

# creo un oggetto datetime con data definita da me
y=datetime.date(2021,2,21)
print(y)

# creo un oggetto datetime con orario definito da me
k=datetime.time(13,35,15)
print(k)

# creo un oggetto datetime con data e orario definiti da me:

z= datetime.datetime(2021,2,21,13,35,15)
print(z)

#PER FORMATTARE LE DATE utilizziamo il metodo stfrtime() che ha diversi parametri

#dichiaro un ogg con data/ora attuale
adesso= datetime.datetime.now()

#formatto con diversi parametri di stfrtime():

# %A --> restituisce il giorno della settimana in lettere:
giorno_settimana= adesso.strftime("%A")
print(giorno_settimana)

# %B --> restituisce il mese in lettere
mese= adesso.strftime("%B")
print(mese)

# %d --> restituisce solo il giorno (numerico)
giorno= adesso.strftime("%d")
print(giorno)

# %m --> restituisce solo il mese (numerico)
month= adesso.strftime("%m")
print(month)

# %Y --> restituisce solo l'anno 
anno= adesso.strftime("%Y")
print(anno)

#PER FORMATTARE GLI ORARI utilizziamo il metodo stfrtime() che ha diversi parametri:

# %H --> restituisce solo l'ora ( formato 24h )
h_24= adesso.strftime("%H")
print(h_24)

# %I --> restituisce solo l'ora ( formato 12h )
h_12= adesso.strftime("%I")
print(h_12)

# %p --> restituisce solo am o pm:
am_pm= adesso.strftime("%p")
print(am_pm)

# %M --> restituisce solo i minuti:
min= adesso.strftime("%M")
print(min)

# %S --> restituisce solo i secondi:
sec= adesso.strftime("%S")
print(sec)

# %x --> formatta la data in gg/mm/aa:
formattazione= adesso.strftime("%x")
print(formattazione)

# %X --> formatta l'ora in H : M : S:
formattazione_ora= adesso.strftime("%X")
print(formattazione_ora)

# posso utilizzare anche più di un parametro alla volta:

concat= datetime.datetime.now().strftime("%d %m %Y")
print(concat)