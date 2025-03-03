class Persona:
    def __init__(self, nome, cognome, eta):  # metodo costruttore
        self.nome = nome #attributo pubblico
        self.cognome= cognome #attributo pubblico
        self.__eta=eta #attributo privato
        
    # Metodo per accedere in lettura ad età (attributo privato)
    def leggi_eta(self):
        return self.__eta
    
    # Metodo per modificare il valore di età:
    def modifica_eta(self, nuovo_valore):
        if nuovo_valore != self.__eta:
            self.__eta= nuovo_valore
            
    # creo un metodo privato:
    def __metodoPrivato(self):
        print("non accessibile dall'esterno")
        
    # creo un metodo per poter utilizzare il metodo privato
    def usaMetodo(self):
        self.__metodoPrivato() #inserisco la chiamata al metodo
 
             
# creo oggetto:            
    
persona1= Persona("Mario", "Rossi", 30)

print(persona1.nome)

# print(persona1.__eta) ---> da errore!!!

#accedo in lettura:
print(persona1.leggi_eta())

#modifico eta:

persona1.modifica_eta(40)

print("valore aggiornato", persona1.leggi_eta())

#accedo al metodo privato

#persona1.__metodoPrivato() ----> da errore!!!

persona1.usaMetodo()