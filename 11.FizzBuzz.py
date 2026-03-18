# Vamos a escribir un programa que imprima los números del 1 al 100, pero con algunas reglas especiales.
# Para los números múltiplos de 3, en lugar de imprimir el número se debe imprimir la palabra "Fizz".
# Para los números múltiplos de 5, en lugar del número se debe imprimir "Buzz".
# Para los números que sean múltiplos de 3 y de 5 al mismo tiempo, se debe imprimir "FizzBuzz".

def fizzBuzz (max_value):
    for num in range(1, max_value + 1):

        if (num %3 == 0 and num %5 == 0):
            print('FizzBuzz')

        elif (num %3 == 0):
            print('Fizz')

        elif (num %5 == 0):
            print('Buzz')

        else:
            print(num)

fizzBuzz(16)

#  primera otra manera
def fizzbuzz(max_value):
    for n in range(1, max_value + 1):
        print("Fizz"*(n%3==0) + "Buzz"*(n%5==0) or n)

fizzbuzz(16)

# segunda manera
def fizzbuzz(max_num):
    for num in range(1, max_num + 1):
        resultado = ""

        if num % 3 == 0:
            resultado += "Fizz"

        if num % 5 == 0:
            resultado += "Buzz"

        print(resultado or num)

fizzbuzz(20)

#tercera maneradef fizzbuzz(max_num):
for num in range(1, num_max + 1):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)