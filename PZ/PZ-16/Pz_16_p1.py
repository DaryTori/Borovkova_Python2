# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.

class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value
counter = Counter(5)

print("Начальное значение:", counter.get_value())
counter.decrement()
print(counter.get_value())
counter.increment()
counter.increment()
counter.increment()
print(counter.get_value())
