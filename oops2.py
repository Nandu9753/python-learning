class Animal:
    def set(self,name):
        self.name = name

# inherit from Animal
class Dog(Animal):

    def display(self):
        print("My name is ", self.name)

labrador = Dog()
labrador.set('fakru')
labrador.display()