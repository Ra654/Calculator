def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return float(b) / float(a)


def square(a):
    return float(a)**2


def sqrt(a):
    return round((float(a)**.5), 2)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        c = a + b
        self.result = add(a, b)
        return self.result

    def subtract(self, a, b):
        c = a - b
        self.result = subtract(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = sqrt(a)
        return self.result




