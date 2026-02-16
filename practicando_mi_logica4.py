ventas = [120, 340, 560, 230, 150, 980, 430, 210, 890, 300]
bajo_promedio = []
alto_promedio = []

# Fase 1
total = sum(ventas)
unidad_ventas = len(ventas)
promedio = (total / unidad_ventas) 

for detalles in ventas:
    if detalles < promedio:
        bajo_promedio.append(detalles)

    else:
        alto_promedio.append(detalles)


#=============
# Impresiones
#=============


print("Promedio De Ventas:", promedio)

# total
print("\nTotal De Ventas:", total)
print(f"Ventas por debajo del promedio: {bajo_promedio}")
print(f"Ventas por encima del promedio: {alto_promedio}")

# Porcentaje de ventas por ensima del promedio
porcentaje = ( len(alto_promedio) / unidad_ventas ) * 100
print(f"\nPorcentaje De Ventas Por Encima Del Promedio: {porcentaje}")