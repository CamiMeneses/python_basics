people = [
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Cho", "house": "Ravenclaw"},
  {"name": "Draco", "house": "Slytherin"}
]

# Sin lambda
def f(person):
  return person["name"]

people.sort(key=f)

# Lambda

people.sort(key=lambda person: person["name"])

print(people)
