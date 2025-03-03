'''
ESERCIZI SULLE CLASSI

Esercizio 1
Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

Esercizio 2
Creare una classe Animale che abbia gli attributi “nome” e “specie”. Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.

Esercizio 3
Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, ad esempio “Questa è una Toyota Corolla del 2017”.

Esercizio 4
Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”. Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

Esercizio 5
Creare una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno. Aggiungi poi i metodi accellera e frena. Creare poi una classe Auto che eredita da Veicolo ma aggiunge la proprietà colore ed il metodo cambia_colore().

Esercizio 6
Seguendo la logica dello schema sottostante, creare classi, sottoclassi ed oggetti.
Inserisci anche attributi e metodi privati
//photo

Esercizio 7 (facoltativo)
Seguendo la logica dello schema sottostante, creare classi, sottoclassi ed oggetti.
//photo
'''
print("-----------------------ESERCIZIO 1------------------------")
class Persona:
    def __init__(self, nome, eta, sesso):
        self.nome = nome
        self.eta = eta
        self.sesso = sesso
    
    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

p1 = Persona("Marco", 32, "Maschio")
p1.presentati()

print("-----------------------ESERCIZIO 2------------------------")
class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
    
    def emetti_suono(self):
        suoni = {"gatto": "Miao!", "cane": "Bau!", "mucca": "Muu!"}
        print(suoni.get(self.specie.lower(), "Suono non definito.")) 

a1 = Animale("Fuffi", "Gatto")
a1.emetti_suono()
a2 = Animale("Rex", "cane")
a2.emetti_suono()

print("-----------------------ESERCIZIO 3------------------------")
class Automobile:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def descrivi(self):
        print(f"Questa è una {self.marca} {self.modello} del {self.anno}.")

auto3 = Automobile("Honda", "Civic", 2017)
auto3.descrivi()

print("-----------------------ESERCIZIO 4------------------------")
class Impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio
    
    def aumenta_stipendio(self):
        self.stipendio *= 1.1
    
    def stampa_dettagli(self):
        print(f"Impiegato: {self.nome} {self.cognome}, matricola {self.matricola}, stipendio: {self.stipendio:.2f} Euro")

imp1 = Impiegato("Marco", "Polo", 12345, 3000)
imp1.stampa_dettagli()
imp1.aumenta_stipendio()
imp1.stampa_dettagli()

print("-----------------------ESERCIZIO 5------------------------")
class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def accellera(self):
        print("Il veicolo sta accelerando.")
    
    def frena(self):
        print("Il veicolo sta frenando.")

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, colore):
        super().__init__(marca, modello, anno)
        self.colore = colore
    
    def cambia_colore(self, nuovo_colore):
        self.colore = nuovo_colore
        print(f"Il colore dell'auto è stato cambiato in {self.colore}.")

auto5 = Auto("Fiat", "Punto", 2015, "Blu")
print(auto5.colore)
auto5.cambia_colore("Rosso")
print(auto5.colore)

print("-----------------------ESERCIZIO 6------------------------")
class Cibo:
    def __init__(self, nome):
        self.nome = nome
    
    def descrizione(self):
        return f"Questo è un alimento della categoria {self.nome}."

class DerivatoVegetale(Cibo):
    def __init__(self, nome):
        super().__init__(nome)

class DerivatoAnimale(Cibo):
    def __init__(self, nome):
        super().__init__(nome)

class Frutta(DerivatoVegetale):
    def __init__(self, nome, tipo, dolcezza):
        super().__init__(nome)
        self.__tipo = tipo  # Es. agrume, drupa, bacca
        self.__dolcezza = dolcezza  # Scala da 1 a 10
    
    def get_info(self):
        return f"{self.nome}: Tipo {self.__tipo}, Dolcezza {self.__dolcezza}/10"

class Verdura(DerivatoVegetale):
    def __init__(self, nome, colore, stagione):
        super().__init__(nome)
        self.__colore = colore
        self.__stagione = stagione
    
    def get_info(self):
        return f"{self.nome}: Colore {self.__colore}, Stagione {self.__stagione}"

class Pesce(DerivatoAnimale):
    def __init__(self, nome, habitat, omega3):
        super().__init__(nome)
        self.__habitat = habitat  # Es. acqua dolce, salata
        self.__omega3 = omega3  # mg di Omega-3 per 100g
    
    def get_info(self):
        return f"{self.nome}: Habitat {self.__habitat}, Omega-3 {self.__omega3} mg/100g"

class Carne(DerivatoAnimale):
    def __init__(self, nome, tipo, grasso):
        super().__init__(nome)
        self.__tipo = tipo  # Es. bianca, rossa
        self.__grasso = grasso  # Percentuale di grasso
    
    def get_info(self):
        return f"{self.nome}: Tipo {self.__tipo}, Grasso {self.__grasso}%"

# Creazione di oggetti
mela = Frutta("Mela", "Drupa", 7)
carota = Verdura("Carota", "Arancione", "Autunno")
salmone = Pesce("Salmone", "Acqua Salata", 2500)
manzo = Carne("Manzo", "Rossa", 15)

# Output di esempio
print(mela.get_info())
print(carota.get_info())
print(salmone.get_info())
print(manzo.get_info())

print("-----------------------ESERCIZIO 7------------------------")
class Animale:
    def __init__(self, nome, habitat):
        self.nome = nome
        self.habitat = habitat

    def descrizione(self):
        return f"{self.nome} vive in {self.habitat}."

# --- VERTEBRATI ---
class Vertebrato(Animale):
    def __init__(self, nome, habitat, colonna_vertebrale=True):
        super().__init__(nome, habitat)
        self.colonna_vertebrale = colonna_vertebrale

class Mammifero(Vertebrato):
    def __init__(self, nome, habitat, pelo, viviparo=True):
        super().__init__(nome, habitat)
        self.pelo = pelo
        self.viviparo = viviparo

    def get_info(self):
        return f"{self.nome} è un mammifero con {self.pelo} pelo."

class Uccello(Vertebrato):
    def __init__(self, nome, habitat, volo, piumaggio):
        super().__init__(nome, habitat)
        self.volo = volo
        self.piumaggio = piumaggio

    def get_info(self):
        return f"{self.nome} ha piume di colore {self.piumaggio} e {'può' if self.volo else 'non può'} volare."

class Rettili(Vertebrato):
    def __init__(self, nome, habitat, velenoso):
        super().__init__(nome, habitat)
        self.velenoso = velenoso

    def get_info(self):
        return f"{self.nome} è {'velenoso' if self.velenoso else 'non velenoso'}."

class Pesce(Vertebrato):
    def __init__(self, nome, habitat, tipo_acqua):
        super().__init__(nome, habitat)
        self.tipo_acqua = tipo_acqua

    def get_info(self):
        return f"{self.nome} vive in acqua {self.tipo_acqua}."

class Anfibio(Vertebrato):
    def __init__(self, nome, habitat, metamorfosi=True):
        super().__init__(nome, habitat)
        self.metamorfosi = metamorfosi

    def get_info(self):
        return f"{self.nome} {'subisce' if self.metamorfosi else 'non subisce'} metamorfosi."

# --- INVERTEBRATI ---
class Invertebrato(Animale):
    def __init__(self, nome, habitat, esoscheletro=False):
        super().__init__(nome, habitat)
        self.esoscheletro = esoscheletro

class Verme(Invertebrato):
    def __init__(self, nome, habitat, segmentato):
        super().__init__(nome, habitat)
        self.segmentato = segmentato

    def get_info(self):
        return f"{self.nome} è un verme {'segmentato' if self.segmentato else 'non segmentato'}."

class Mollusco(Invertebrato):
    def __init__(self, nome, habitat, conchiglia):
        super().__init__(nome, habitat)
        self.conchiglia = conchiglia

    def get_info(self):
        return f"{self.nome} {'ha' if self.conchiglia else 'non ha'} una conchiglia."

class Artropode(Invertebrato):
    def __init__(self, nome, habitat, zampe):
        super().__init__(nome, habitat)
        self.zampe = zampe

class Crostaceo(Artropode):
    def __init__(self, nome, habitat, carapace):
        super().__init__(nome, habitat, zampe=10)
        self.carapace = carapace

    def get_info(self):
        return f"{self.nome} ha un carapace {'duro' if self.carapace else 'morbido'}."

class Insetto(Artropode):
    def __init__(self, nome, habitat, ali):
        super().__init__(nome, habitat, zampe=6)
        self.ali = ali

    def get_info(self):
        return f"{self.nome} {'ha' if self.ali else 'non ha'} ali."

class Aracnide(Artropode):
    def __init__(self, nome, habitat, velenoso):
        super().__init__(nome, habitat, zampe=8)
        self.velenoso = velenoso

    def get_info(self):
        return f"{self.nome} è un aracnide {'velenoso' if self.velenoso else 'non velenoso'}."

# Creazione di oggetti
leone = Mammifero("Leone", "Savana", "folto")
aquila = Uccello("Aquila", "Montagne", True, "marrone")
serpente = Rettili("Serpente", "Foresta", True)
squalo = Pesce("Squalo", "Oceano", "salata")
rana = Anfibio("Rana", "Palude", True)

ragno = Aracnide("Ragno", "Terrestre", True)
granchio = Crostaceo("Granchio", "Mare", True)
farfalla = Insetto("Farfalla", "Prati", True)

# Output di esempio
print(leone.get_info())
print(aquila.get_info())
print(serpente.get_info())
print(squalo.get_info())
print(rana.get_info())

print(ragno.get_info())
print(granchio.get_info())
print(farfalla.get_info())
