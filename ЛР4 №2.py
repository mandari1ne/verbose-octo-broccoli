class Transport:
    def __init__(self, name):
        self.name = name

    def move(self, distance):
        pass

    def write_info_to_file(self, file_name):
        with open(file_name, 'a') as file:
            file.write(f"Transport: {self.name}\n")
            file.write(f"Distance: {self.distance} km\n")
            file.write(f"Time: {self.time} hours\n")
            file.write(f"Cost: {self.cost} dollars\n\n")

class Airplane(Transport):
    def move(self, distance):
        self.distance = distance
        self.time = round(distance / 800, 2)
        self.cost = round(distance * 0.1, 2)

class Train(Transport):
    def move(self, distance):
        self.distance = distance
        self.time = round(distance / 120, 2)
        self.cost = round(distance * 0.05, 2)

class Car(Transport):
    def move(self, distance):
        self.distance = distance
        self.time = round(distance / 60, 2)
        self.cost = round(distance * 0.08, 2)

def get_fastest_transport(transport_lis):
    fastest_transport = None
    fastest_time = float('inf')

    for transport in transport_lis:
        if transport.time < fastest_time:
            fastest_transport = transport
            fastest_time = transport.time

    return fastest_transport

def get_cheapest_transport(transport_list):
    cheapest_transport = None
    cheapest_cost = float('inf')

    for transport in transport_list:
        if transport.cost < cheapest_cost:
            cheapest_transport = transport
            cheapest_cost = transport.cost

    return cheapest_transport

airplane = Airplane("Airplane")
train = Train("Train")
car = Car("Car")

airplane.move(500)
train.move(500)
car.move(500)

fastest_transport = get_fastest_transport([airplane, train, car])
cheapest_transport = get_cheapest_transport([airplane, train, car])

print(f"Fastest Transport: {fastest_transport.name}")
print(f"Time: {fastest_transport.time}")

print(f"\nCheapest Transport: {cheapest_transport.name}")
print(f"Cost: {cheapest_transport.cost} dollars")

airplane.write_info_to_file(r"D:\БГУИР\2 курс\СЯП\лр4\транспорт.txt")
train.write_info_to_file(r"D:\БГУИР\2 курс\СЯП\лр4\транспорт.txt")
car.write_info_to_file(r"D:\БГУИР\2 курс\СЯП\лр4\транспорт.txt")