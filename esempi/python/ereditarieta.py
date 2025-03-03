
class Persona:
    def __init__(self, nome, cognome, eta):  # metodo costruttore
        self.nome = nome
        self.cognome= cognome
        self.eta=eta
    
    def saluta(self):
        print("ciao sono", self.nome)
    
    
# CREO UNA SOTTOCLASSE Professore

class Professore(Persona):
    def __init__(self, nome, cognome, eta, materia):
        super().__init__(nome, cognome, eta)
        
        self.materia=materia # inizializzo solo la proprietà che ho aggiunto
        
    # faccio l'override del metodo che ho ereditato da Persona
    def saluta(self):
        print("buongiorno, sono il prof", self.nome, self.cognome)
        
    # aggiungo il metodo insegna solo per la classe Professore
    def insegna(self):
        print("oggi vi insegno", self.materia)    
    

professore1= Professore("Mario", "Rossi", 40, "matematica") 

# invoco i metodi:

professore1.saluta()

professore1.insegna()

persona1= Persona("Giorgia", "Verdi", 15)
persona1.saluta()
persona1.insegna()