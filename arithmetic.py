# This is just to play around and have another version for git

def add(num1, num2):
    #return 10
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    #pass
    return num1 * num2

def divide(num1, num2):
    return float(num1) / num2

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1 

def power(num1, num2):
#    return pow(num1, num2)
    x = 1

    for i in range(num2):
        x = x * num1
    return x

def mod(num1, num2):
    return num1 % num2

