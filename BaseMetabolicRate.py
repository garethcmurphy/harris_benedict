#!/usr/bin/env python

"""BasalMetabolicRate.py: Calculates BMR."""

__author__ = "Gareth Murphy"


class BaseMetabolicRate:
    weight = 85
    height = 172
    age = 37
    totalheat = 1745
    leanbodyweight = 0.79 * weight

    def bmr(self):
        bmr = self.weight * 10 + self.height * 6.25 - self.age * 5 + 5
        return bmr

    def katchmacardle(self):
        return 370 + 21.6* self.leanbodyweight

    def show(self):
        print(self.bmr())


if __name__ == '__main__':
    bmr = BaseMetabolicRate()
    bmr.show()
    print (bmr.katchmacardle())
