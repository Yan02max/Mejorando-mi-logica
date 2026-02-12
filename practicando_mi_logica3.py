# Datos
edades = [15, 22, 17, 30, 45, 18, 19, 60, 13, 25]
mayor_de_cuarenta = 0
mayor_de_dieciocho = 0
menor_de_edad = 0

for e in edades:
    if e >= 40:
        mayor_de_cuarenta += 1


    elif e >= 18:
        mayor_de_dieciocho += 1
    
    else:
        menor_de_edad += 1


# Impresiones
datos_del_porcentaje = len(edades)

porcentaje = (menor_de_edad/ datos_del_porcentaje) * 100
print("El porsentaje de edad entre 0-17 es:", porcentaje,"%")
print("Cuantas Persona Hay Entre 0-17:", menor_de_edad)

porcentaje_dos = (mayor_de_dieciocho/ datos_del_porcentaje) * 100
print("\nEl porsentaje de edad entre 18-40 es:", porcentaje_dos,"%")
print("Cuantas Persona Hay Entre 18-40:", mayor_de_dieciocho)

porcentaje_tres = (mayor_de_cuarenta/ datos_del_porcentaje) * 100
print("\nEl porsentaje de mayores de 40 es:", porcentaje_tres,"%")
print("Cuantas Persona Hay De 40 En Adelante:", mayor_de_cuarenta)
