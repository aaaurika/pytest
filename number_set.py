class NumberSet:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def mean(self):
        if self.numbers:  # Проверяем, не пустой ли набор
            return sum(self.numbers) / len(self.numbers)
        else:
            return 0  # Если набор пустой, среднее равно 0

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)

