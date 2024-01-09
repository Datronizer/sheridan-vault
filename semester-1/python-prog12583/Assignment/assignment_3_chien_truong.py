import math

def my_power(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result

def my_factorial(x):
    result = 1
    for i in range(x):
        result *= (i + 1)
    return result

def inner(x, n):
    return my_power(-1, n) * (my_power(x, (2 * n + 1)) / my_factorial(2 * n + 1))

def maclaurin(x):
    result = 0
    for i in range(5):
        result += inner(x, i)
    return result 
        
def toRadians(x):
    return x * math.pi / 180
        
x = float(input("Enter angle in degrees: "))
print("sin(%5.1f) = %5.3f" % (x, maclaurin(toRadians(x))))