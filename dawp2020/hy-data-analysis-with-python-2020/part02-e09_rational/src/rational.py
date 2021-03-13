#!/usr/bin/env python3

from os import supports_bytes_environ


class Rational(object):
    def __init__(self, a, b) -> None:
        if b == 0:
            return None     # ZeroDivisor
        self.a = a
        self.b = b
    
    def __str__(self) -> str:
        return '{0}/{1}'.format(self.a, self.b)

    def __mul__(self, o: object) -> object:
        return Rational(self.a * o.a, self.b * o.b)

    def __truediv__(self, o: object) -> object:
        if o.a == 0:
            return None
        return Rational(self.a * o.b, self.b * o.a)

    def __add__(self, o: object) -> object:
        return Rational(self.a * o.b + self.b * o.a, self.b * o.b)

    def __sub__(self, o: object) -> object:
        return Rational(self.a * o.b - self.b * o.a, self.b * o.b)

    def __eq__(self, o: object) -> bool:
        return self.a == o.a and self.b == o.b

    def __gt__(self, o: object) -> bool:
        return self.a * o.b > self.b * o.a
    
    def __lt__(self, o: object) -> bool:
        return self.a * o.b < self.b * o.a


def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
