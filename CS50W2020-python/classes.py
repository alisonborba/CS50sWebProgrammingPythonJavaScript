class Point():
    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY

p1 = Point(1, 8)
p2 = Point(2, 8)
p3 = Point(3, 8)
print(p1.x)
print(p2.x)
print(p3.x)



class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []
   
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True
   
    def open_seats(self):
        return self.capacity - len(self.passenger)

flight = Flight(3)

people = ["a", "b", "c", "d"]

for person in people:
    if flight.add_passenger(person):
        print(f"Person {person} added successfuly")
    else:
        print(f"Flight is full")


