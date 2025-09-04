class Animal() :
    def __init__(self,name,age,species):
        self.name =name
        self.age = age
        self.species = species
    
    def info(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"species : {self.species}")
#-------------------------------------------------
class Dog (Animal) :
    def __init__(self, name, age, species, breed):
        super().__init__(name, age, species) 
        self.breed = breed

    def info(self) :
        super().info()  
        print(self.breed) 
#-------------------------------------------------
class Cat (Animal) :
    def __init__(self, name, age, species, color):
        super().__init__(name, age, species) 
        self.color = color

    def info(self) :
        super().info()  
        print(f"color : {self.color}") 
#------------------------------------------------
a1=Cat("lolo",4,"persian","white")
a1.info()