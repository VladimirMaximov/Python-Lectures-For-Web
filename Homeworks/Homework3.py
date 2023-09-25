import math


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    @property
    def value(self):
        return self.num / self.den

    def reduce_fraction(self):
        gcd = math.gcd(self.num, self.den)
        self.num /= gcd
        self.den /= gcd

    @classmethod
    def create_fraction(cls, num: int, den: int):
        if den == 0:
            den_m = 1
            num_m = num
        elif den < 0:
            den_m = -den
            num_m = -num
        else:
            den_m = den
            num_m = num

        gcd = math.gcd(num_m, den_m)
        if gcd != 1:
            num_m //= gcd
            den_m //= gcd

        return cls(num_m, den_m)

    def check_fraction(self):
        return isinstance(self.num, int) \
               and isinstance(self.den, int) \
               and self.den > 0 \
               and math.gcd(self.num, self.den) == 1

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __mul__(self, other):
        fraction = other
        if isinstance(other, int):
            fraction = Fraction.create_fraction(other, 1)

        fraction = Fraction.create_fraction(self.num * fraction.num, self.den * fraction.den)
        return fraction

    def __imul__(self, other):
        fraction = other
        if isinstance(other, int):
            fraction = Fraction.create_fraction(other, 1)

        fraction = Fraction.create_fraction(self.num * fraction.num, self.den * fraction.den)
        return fraction

    def __add__(self, other):
        if isinstance(other, int):
            return Fraction.create_fraction(self.num + other * self.den, self.den)

        return Fraction.create_fraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def __iadd__(self, other):
        if isinstance(other, int):
            return Fraction.create_fraction(self.num + other * self.den, self.den)

        return Fraction.create_fraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def whole_fraction(self):
        return self.num // self.den

    def frac_part_fraction(self):
        return Fraction.create_fraction(self.num % self.den, self.den)

    def __eq__(self, other):
        fraction1 = Fraction.create_fraction(other.num, other.den)
        fraction2 = self
        fraction2.reduce_fraction()

        return fraction1.num == fraction2.num and fraction1.den == fraction2.den

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > self.value
