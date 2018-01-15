#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__ = "Barack Obama"


class BaseMetabolicRate:
    weight = 85
    height = 72
    age = 37

    def bmr(self):
        bmr = self.weight * 10 + self.height * 6.25 - self.age * 5 + 5
        return bmr

    def show(self):
        print(self.bmr())


if __name__ == '__main__':
    bmr = BaseMetabolicRate()
    bmr.show()
