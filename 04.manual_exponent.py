import math

def manual_exponent(number, exponent):
    result = 1
    for i in range(exponent):
        result *= number

    return result

print(manual_exponent(5,2))
    
