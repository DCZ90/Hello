class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger (self,name):
        self.passengers.append(name)


Vuelo = Flight(3)