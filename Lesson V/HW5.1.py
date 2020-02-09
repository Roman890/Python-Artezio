"""
Разработать класс Complex, который бы описывал комплексные числа,
позволял их складывать, вычитать, умножать, делить и получать модуль
"""


class Complex(object):
    """Класс для комплексного числа"""
    def __init__(self, real_part=0, imaginary_part=0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

# сложение
    def __add__(self, other):
        return Complex(self.real_part + other.real_part,
                       self.imaginary_part + other.imaginary_part)

# вычитание
    def __sub__(self, other):
        return Complex(self.real_part - other.real_part,
                       self.imaginary_part - other.imaginary_part)

# умножение
    def __mul__(self, other):
        return Complex(self.real_part * other.real_part
                       - self.imaginary_part * other.imaginary_part,
                       self.imaginary_part * other.real_part
                       + self.real_part * other.imaginary_part)

# деление
    def __truediv__(self, other):
        return Complex((self.real_part * other.real_part
                        + self.imaginary_part * other.imaginary_part)
                       / (pow(other.real_part, 2)
                          + pow(other.imaginary_part, 2)),
                       (self.imaginary_part * other.real_part
                        - self.real_part * other.imaginary_part)
                       / (pow(other.real_part, 2)
                          + pow(other.imaginary_part, 2)))

# модуль
    def __abs__(self):
        return Complex(pow((pow(self.real_part, 2)
                            + pow(self.imaginary_part, 2)), 0.5))

# подготовка строк для вывода
    def __str__(self):
        return "{0.real:.2f}{0.imag:+.2f}i".format(
            complex(self.real_part, self.imaginary_part))

    @staticmethod
    def print_number(number_1, number_2):
        """функция вывода"""
        print(number_1 + number_2)
        print(number_1 - number_2)
        print(number_1 * number_2)
        print(number_1 / number_2)
        print(abs(number_1))
        print(abs(number_2))


STRING = input("Введите первые два числа: ")
NUMBER1 = Complex(int(STRING.split()[0]), int(STRING.split()[-1]))
STRING = input("Введите вторые два числа: ")
NUMBER2 = Complex(int(STRING.split()[0]), int(STRING.split()[-1]))
Complex.print_number(NUMBER1, NUMBER2)
