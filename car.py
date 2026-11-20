
class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.kilometers = 0

    def drive(self, km):
        if km <= 0:
            print("Invalid distance!")
            return

        self.kilometers += km
        print(f"{self.brand} {self.model} drove {km} km.")

    def age(self, year):
        return year - self.year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.kilometers} km driven"

car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Mitsubishi", "Mirage", 2021)

car1.drive(100)
car2.drive(50)
car3.drive(0)

print("Car 1 age:", car1.age(2026))
print("Car 2 age:", car2.age(2026))
print("Car 3 age:", car3.age(2026))

print(car1)
print(car2)
print(car3)
