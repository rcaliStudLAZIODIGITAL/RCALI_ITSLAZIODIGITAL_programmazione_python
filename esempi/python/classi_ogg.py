# CLASSI E OGGETTI

# le classi sono strutture dati che ci permettono di creare oggetti:
# le classi hanno: proprietà e metodi

#COME CREARE UNA CLASSE

class Persona:
    def __init__(self, nome, cognome, eta):  # metodo costruttore
        self.nome = nome
        self.cognome= cognome
        self.eta=eta
    
    
#COME CREARE OGGETTI DELLA CLASSE PERSONA:

persona1 = Persona("Mario", "Rossi", 30)
persona2 = Persona("Giulia", "Bianchi", 25)

print(persona1.nome) # accedo alla proprietà nome dell'oggetto persona1

 # LE CLASSI HANNO ANCHE METODI:
 
class Telefono:
    def __init__(self, modello, marca, colore):
        self.modello=modello
        self.marca=marca
        self.colore=colore 
        
    #definisco i metodi della classe:
    
    def chiamare(self):
        print("sto chiamando")
    
    def fotografare(self):
        print("foto scattata con telefono: ", self.modello, self.marca)

#creo oggetto di Telefono:

telefono1= Telefono("Apple", "iphone 16", "nero")

# invoco i metodi di Telefono

telefono1.chiamare()
telefono1.fotografare()

# MODIFICARE ed ELIMINARE proprietà di un oggetto:

telefono1.modello = "iphone 15"

del telefono1.colore #elimina proprietà

del telefono1 #dealloca l'oggetto
