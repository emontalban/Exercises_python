# Crear una funcion que calcule la media de una lista de numeros manualmente
def mediana(numbers):
    orden_list = sorted(numbers)
    print(orden_list)
    center_list = orden_list[len(orden_list)//2]
    return center_list

print(mediana( [100, 83, 56, 220, 40, 120, 400, 1, 3]))

print("*****************************************")

print( "Segundo Ejemplo")
# Otra solucion
import math

nums = [100, 83, 56, 220, 40, 120, 400, 1, 3]
order_nums = sorted(nums)
list_nums = len(nums)  # 9
first_nums = order_nums[:math.floor(list_nums/2)]
end_nums = order_nums[-math.floor(list_nums/2):]
median = order_nums[math.floor(list_nums/2):math.floor(list_nums/2)+1]


print(order_nums)
print(list_nums)
print(first_nums)
print(end_nums)
print(median)



print ("**************Mejores Practicas **********")
sale_prices = [10, 183, 5, 6, 2, 20, 40, 120, 400, 1, 3] 
sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)