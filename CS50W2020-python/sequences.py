# String
name = "Harry"
print(name[0])

# Array
names = ["Harry", "Ben", "Tom"]
names.append("Joe")
names.sort()
print(names)


# tuple - Sequence of imutable value
coordX = 10.0
coordY = 10.0
coord = (10.0, 10.0)
print(coord)
coord2 = (10.0, 2,3)
print(coord2)

# set - collection of unique values
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(1)
s.remove(2)
print(s)
print(f"the set has {len(s)} elements")

# dict - collection of key-value pairs
houses = {"Harry": "Grif", "Draco": "Slyt"}
houses["Hermione"] = "Gryf"
print(houses["Hermione"])


#Loops
names = ["ben", "jones", "adam"]
for name in names:
    print(name)

for i in range(6):
    print(i)

