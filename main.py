#!/usr/bin/python
# -*- coding: utf-8 -*-


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


# def number_of_groups(n, k):


print(factorial(5))  # виведе 120
