class MyClass:
  x = 5              #Create a class named MyClass, with a property named x

p1 = MyClass()   #Create an object named p1, and print the value of x
print(p1.x)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



x = MyClass()

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter



print("-----"*10)





class Dog:
  tricks = []             # mistaken use of a class variable

  def __init__(self, name):
    self.name = name

  def add_trick(self, trick):
    self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead') 
print(d.tricks)             # unexpectedly shared by all dogs


print("------"*5)


class Dog:

  def __init__(self, name,):
    self.name = name
    self.tricks = []     ## creates a new empty list for each dog

  def add_trick(self, trick):
    self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead') 
print(d.tricks)   



class Warehouse:
  purpose = 'storage'
  region = 'west'


w1=Warehouse()
w2=Warehouse()
print(w1.purpose , w1.region)
w2.region= "east"

print(w2.purpose , w2.region)

print(w1.purpose , w1.region)




print("------"*5)


# Function defined outside the class
def f1(self,x, y):
  return min(x, x+y)

class C:
  f = f1

  def g(self):
    return 'hello world'
      
  h = g


z1=C()
print(z1.f(5,6))