# Se anida un diccionario dentro de una lista

people = [
    {"name":"Harry","house":"Slpaz"},
    {"name":"Cho","house":"TDDF"},
    {"name":"Draco","house":"uuuu"},
]

#def f(person):
#    return person["name"]

#people.sort(key=f)

people.sort(key=lambda person:person["house"])

print(people)