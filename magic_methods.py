class Person:
     def __init__(self, name, age):
          self.name = name
          self.age = age
     def __sts__(self):  #mage method two undersscore... 
          return f"Person {self.name} , {self.age} years old."
     def __repr__(self):
          return f"<Person('{self.name}', {self.age})>"
bob = Person("Bob", 35)

print(bob.__str__())
print(bob.__repr__())

