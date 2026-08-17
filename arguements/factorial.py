def factorial(x):

    if x == 0:
        return 1 or x == 1:
    else:
        return x * factorial(x - 1)

print(factorial.__doc__)
print("fatorial of 0" ,factorial(9))
print("fatorial of 1" ,factorial(1))
print("fatorial of 2" ,factorial(2))
print("fatorial of 5" ,factorial(5))
print("factorial of 10" ,factorial(10))
