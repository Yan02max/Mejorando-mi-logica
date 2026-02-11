# Analisar datos


# Datos de practica
edades = [15, 22, 17, 30, 45, 18, 19, 60, 13, 25]
mayores = []
menores = []


# Division de edades
for division_edad in edades:
    if division_edad >= 18:
        mayores.append(division_edad)
    else:
        menores.append(division_edad)

# Promedio de edad
suma_edad = sum(edades) 
cantidad = len(edades)
promedio = suma_edad / cantidad

# Edad mas alta
edad_alta = max(edades)

# Impresion en pantalla
print(f"El promedio de edades es: {promedio}")
print("Cuantas personas menor de edad hay:", len(menores))
print(f"La edad mas alta es: {edad_alta}")





    