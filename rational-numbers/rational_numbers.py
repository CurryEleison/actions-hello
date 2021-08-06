"""Working with rationals"""
from __future__ import division


class Rational:
    """Implementation of rational numbers"""
    def __init__(self, numer, denom):
        cmn = Rational._gcd(numer, denom)
        smaller_numer = numer // cmn
        smaller_denom = denom // cmn
        sign_correct = -1 if smaller_denom < 0 else 1

        self.numer = sign_correct * smaller_numer
        self.denom = sign_correct * smaller_denom

    @staticmethod
    def _gcd(a, b):
        # pylint: disable=invalid-name
        if b == 0:
            return a
        return Rational._gcd(b, a%b)


    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer*other.denom + self.denom*other.numer, self.denom*other.denom)

    def __sub__(self, other):
        return Rational(self.numer*other.denom - self.denom*other.numer, self.denom*other.denom)

    def __mul__(self, other):
        return Rational(self.numer*other.numer, self.denom*other.denom)

    def __truediv__(self, other):
        return Rational(self.numer*other.denom, self.denom*other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return base**(self.numer/self.denom)
