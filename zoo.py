class Animal:
  def __init__(self, name):
    self.name = name
  
  def eat(self):
    print(self.name, "is eating")
  
  def make_sound(self):
    print(self.name, "makes sound")

class Lion(Animal):
  def eat(self):
    print(self.name, "eats fresh meat")
  
  def make_sound(self):
    print(self.name, "roars loudly!")

class Elephant(Animal):
  def eat(self):
    print(self.name, "eats grass and fruit")
  
  def make_sound(self):
    print(self.name, "trumpets!")

class Monkey(Animal):
  def eat(self):
    print(self.name, "eats bananas")
  
  def make_sound(self):
    print(self.name, "chatters!")

animal1 = Animal("Generic")
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("----")

print(elephant.make_sound())
print(elephant.eat())
print("----")

print(monkey.make_sound())
print(monkey.eat())
print("----")

