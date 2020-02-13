#!/usr/bin/env python


def euclid(x, y):
    if x == 0:
         return y
    elif y == 0:
        return x
    else:
        remain = max(x,y) % min(x,y)
        return euclid(min(x,y), remain)

def refactor(x, y):
    gcd = euclid(x, y)
    return (x / gcd, y / gcd)
    def __repr__(self) -> str:
        return f"{self.numer}/{self.denom}"


class Rational:

    def __init__(self, numerator, denominator):
        self.numer, self.denom = refactor(numerator, denominator)

    def __str__(self) -> str:
        return f"{self.numer}/{self.denom}"

    def __add__(self, other: object):
        if not isinstance(other, Rational):
            return NotImplemented
        ret_numer = self.numer * other.denom + self.denom * other.numer
        ret_denom = other.denom * self.denom
        return Rational(ret_numer, ret_denom)

    def __sub__(self, other: object):
        if not isinstance(other, Rational):
            return NotImplemented
        ret_numer = self.numer * other.denom - self.denom * other.numer
        ret_denom = other.denom * self.denom
        return Rational(ret_numer, ret_denom)

    def __mul__(self, other: object):
        if not isinstance(other, Rational):
            return NotImplemented
        ret_numer = self.numer * other.numer
        ret_denom = other.denom * self.denom
        return Rational(ret_numer, ret_denom)

    def __truediv__(self, other: object):
        if not isinstance(other, Rational):
            return NotImplemented
        ret_numer = self.numer * other.denom
        ret_denom = other.numer * self.denom
        return Rational(ret_numer, ret_denom)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rational):
            return NotImplemented
        if type(other) is type(self) and self.numer == other.numer and self.denom == other.denom:
            return True
        else:
            return False

if __name__ == "__main__":
    print(euclid(270, 192))
    print(Rational(270, 192))
    print(Rational(45, 32))

    assert Rational(270, 192) == Rational(45, 32)
    assert Rational(3, 2) + Rational(3, 2) == Rational(3, 1)
    assert Rational(3, 2) - Rational(1, 2) == Rational(1, 1)
    assert Rational(3, 2) * Rational(1, 2) == Rational(3, 4)
    assert Rational(3, 2) / Rational(1, 2) == Rational(3, 1)
