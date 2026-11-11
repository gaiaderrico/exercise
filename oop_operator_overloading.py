# EXERCISES OOP - Operator Overloading
# https://gist.github.com/bdallard/b2f2c910e3a9b564a30c86991c97b4fc

import math


# PROBLEM 1
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# PROBLEM 2
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        return self.age > other.age


# PROBLEM 4
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


# PROBLEM 5
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius


# PROBLEM 6
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, other):
        return self.distance() < other.distance()

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __eq__(self, other):
        return self.distance() == other.distance()

    def __ne__(self, other):
        return self.distance() != other.distance()

    def __ge__(self, other):
        return self.distance() >= other.distance()

    def __le__(self, other):
        return self.distance() <= other.distance()


# PROBLEM 7
class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __mul__(self, other):
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("Incompatible dimensions")
        result = []
        for i in range(len(self.rows)):
            row = []
            for j in range(len(other.rows[0])):
                total = 0
                for k in range(len(other.rows)):
                    total += self.rows[i][k] * other.rows[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)

    def __str__(self):
        return "\n".join(str(row) for row in self.rows)


if __name__ == "__main__":
    print(Complex(1, 2) + Complex(3, 4))                    # 4 + 6i
    print(Complex(3, 4) - Complex(1, 2))                    # 2 + 2i
    print(Person("Anna", 30, "F") > Person("Luca", 20, "M"))  # True
    print(Vector(1, 2, 3) * Vector(4, 5, 6))                # 32
    print(Circle(5) == Circle(5), Circle(2) < Circle(3))    # True True
    print(Point(3, 4) > Point(1, 1))                        # True
    print(Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [7, 8]]))  # [19, 22] / [43, 50]
