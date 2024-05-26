"""1) Crear una clase gato que contenga 5 atributos (Nombre, Color de pelo, color de
ojos, cansancio y hambre) y 4 métodos (Comer, Dormir, Jugar, Acariciar). Luego
instanciar 3 objetos de la clase gato con distintos atributos y utilizar sus
Metodos."""
class gatito.1():
    def __init__(self,Nombre,Pelo,Ojos,CansancioMaximo,HambreMaximo):
        self.Nombre=Nombre
        self.Pelo=Pelo
        self.Ojos=Ojos
        self.CansancioMaximo=CansancioMaximo
        self.HambreMaximo=HambreMaximo

    def describir(self):
        print (f"nombre {self.Nombre}, pelo {self.Pelo}, ojos {self.Ojos}, cansancio {self.CansancioMaximo}, hambre {self.HambreMaximo}")

    def comer(self):
        print(f"{self.nombre} está comiendo.")
        self.hambre = max(0, self.hambre - 1)
        print(f"Hambre de {self.nombre}: {self.hambre}")
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo.")
        self.cansancio = max(0, self.cansancio - 1)
        print(f"Cansancio de {self.nombre}: {self.cansancio}")

    def jugar(self):
        print(f"{self.nombre} está jugando.")
        self.cansancio += 1
        self.hambre += 1
        print(f"Cansancio de {self.nombre}: {self.cansancio}")
        print(f"Hambre de {self.nombre}: {self.hambre}")

    def acariciar(self):
        print(f"Estás acariciando a {self.nombre}.")
        self.cansancio = max(0, self.cansancio - 1)
        print(f"Cansancio de {self.nombre}: {self.cansancio}")

gatito1=Gato("Salem", "Negro", "Verdes", cansancio=2, hambre=3)
#gatito1.describir()
#gatito1.comer() 
#gatito1.dormir()
#gatito1.jugar()
#gatito1.acariciar()        
