class Vehicle:
    def __init__(self, color, make, model, year, top_speed):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed


my_car = Vehicle("black", "Tesla", "P90", 2021, 200)
print(type(my_car), "Color is", my_car.color)
