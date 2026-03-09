# Crear un histograma, 
# Google   $$$$$$$$$$$$$$$$$$$$
# Facebook $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Twitter  $$$$$$$$$$
# Offline  $$$$$$$$$$
# cada linea representa una empresa y su numero de ventas

sales = {
    "Google": 20,
    "Facebook": 42,
    "Twitter": 10,
    "Offline": 12
}
print('g ' + sales['Google'] * '$')
print('f ' + sales['Facebook'] * '$')
print('t ' + sales['Twitter'] * '$')
print('o ' + sales['Offline'] * '$')
print ('****************************************')



# otra solucion con un bucle for

for company, count in sales.items():
    print(company[0], '$' * count)

