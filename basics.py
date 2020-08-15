print("Hello, world!")

## TYPES OF VARIABLES
a = 28
b = 1.5
c = "Hello!"
d = True
e = None

## GET AND PRINT INFORMATION
name = input("Name: ")
print("Hello, " + name)
print(f"Hello, {name}")
print(name[0])

n = int(input("Number: "))

## CONDITIONS
if n > 0:
  print("n is positive")
elif n < 0:
  print("n is not positive")
else:
  print("n is zero")

## DATA STRUCTURES

# list - squence of mutable values (you can change the elements in the list)
names = ["Harry", "Ron", "Hermione"]
names.append("Draco") #To add an element
names.sort()
print(names) #['Draco', 'Harry', 'Hermione', 'Ron']

# tople - sequence of inmmutable values
corditnate = (10.0, 20.0)

# set - collection of unique values
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(3)
print (s) #{1, 2, 3}
s.remove(3)
print(f"The set has {len(s)} elements") #The set has 2 elements

# dict - collection of key-value pairs (dictionary)
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Hermione"] = "Gryffindor"
print(houses["Harry"])
print(houses["Hermione"])

## LOOPS
for i in [0, 1, 2, 3,4, 5]:
  print(i)

for i in range(6):
  print(i)

for name in names:
  print(name)

name = "Harry"

for character in name:
  print(character)

## FUNCTIONS
from functions import square # To import functions from other file
for i in range(10):
  print(f"The square of {i} is {square(i)}")

import functions # another way to do it
for i in range(10):
  print(f"The square of {i} is {functions.square(i)}")
