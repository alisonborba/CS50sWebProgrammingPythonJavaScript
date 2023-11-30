people = [
    {"name": "Harry", "house": "Grif"},
    {"name": "Cho", "house": "Raven"},
    {"name": "Draco", "house": "Slyt"},
]

# def f(person):
    # return person["name"]

print(people)
people.sort(key=lambda person: person["name"])
print(people)