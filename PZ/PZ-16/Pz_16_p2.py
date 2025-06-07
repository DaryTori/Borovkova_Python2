#Создайте класс "Автомобиль", который содержит информацию о марке, модели и
#годе выпуска. Создайте класс "Грузовик", который наследуется от класса
#"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
#"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
#информацию о количестве пассажиров

class Automobile:
    def __init__(self, marka, model, year):
        self.marka = marka
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.marka} {self.model} ({self.year})"

class Gruzovik(Automobile):
    def __init__(self, marka, model, year, load_capacity):
        super().__init__(marka, model, year)
        self.load_capacity = load_capacity

    def __str__(self):
        return f"{super().__str__()} {self.load_capacity}"

class Legkovoy(Automobile):
    def __init__(self, marka, model, year, passengers):
        super().__init__(marka, model, year)
        self.passengers = passengers

    def __str__(self):
        return f"{super().__str__()} {self.passengers}"

truck = Gruzovik("Volvo", "FH16", 2020, 25000)
car = Legkovoy("Toyota", "Camry", 2022, 5)

print(truck)
print(car)