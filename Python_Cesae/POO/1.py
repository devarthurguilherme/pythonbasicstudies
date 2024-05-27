class Person:
    # definimos propriedades e comportamentos (métodos)
    # construtor - inicializa uma instância
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # self.__name - private
        # self._name - protected
   
    def __str__(self): # toString __repr__
        return f"O(a) {self.name} tem {self.age} anos!"
 
    # getters - buscar informação
    def getName(self):
        return self.name
   
   
    # setters - atualizar
    def setName(self, name):
        self.name = name
 
 
p = Person("Bruno", 33) # instância do objeto Pessoa
p.setName("Bruna")
print(p.getName())
print(p)