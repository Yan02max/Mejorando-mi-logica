print("Calculadora con una sola variable")


print("==================")
print("Menu de opciones")
print("==================")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Divicion")
print("5. Divicion Entera")
print("6. Exponente")
print("7. Modulo o Resto \n")

opcion = int(input("Introduce la opcion deseada: "))

if opcion == 1:
    print("Elegiste Suma")

    numero = int(input("\nIntroduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la Suma es: ", numero)

elif opcion == 2:
    print("Elegiste resta")

    numero = int(input("\nIntroduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la Resta es: ", numero)

elif opcion == 3:
    print("Elegiste multiplicacion")

    numero = int(input("\nIntroduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado de la Multiplicacion es: ", numero)

elif opcion == 4:
    print("Elegiste Division")

    numero = float(input("\nIntroduce el primer numero: "))
    numero /= float(input("Introduce el segundo numero: "))
    print("El resultado de la Division es: ", round(numero, 2))

elif opcion == 5:
    print("Elegiste division entera")

    numero = int(input("\nIntroduce el primer numero: "))
    numero //= int(input("Introduce el segundo numero: "))
    print("El resultado de la Division Entera es: ", numero)

elif opcion == 6:
    print("Elegiste exponente")

    numero = int(input("\nIntroduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print("El resultado del Exponente es: ", numero)

elif opcion == 7:
    print("Elegiste Modulo")

    numero = int(input("\nIntroduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print("El Modulo o Resto es: ", numero)
    
else:
    print("Esta opcion no existe.")

