from functools import reduce

#contruye una funcion que te devuelva la media aritmetica

def get_average(list):
    total = reduce((lambda total, element: total + element), list)
    return total / len(list)


avg = get_average([1, 2, 3, 4, 5, 6])

print(avg)