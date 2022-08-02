import math


def func(x):
    result = 3 * x - math.cos(x) - 1
    return result


def bisection(a, b):
    if (func(a) * func(b)) >= 0:
        print("Wrong input")
        return
    c = a
    while ((b - a) >= 0.01):
        c = (a + b) / 2
        if (func(c) == 0.0):
            break

        if (func(a) * func(c)) < 0:
            b = c
        else:
            a = c

    print("The value of root is : ", "%.4f" % c)


low = -200
high = 300

bisection(low, high)