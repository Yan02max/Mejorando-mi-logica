import random as rnd

print("Bienvenido a 'Adivina el numero secreto'")
print("He seleccionado un numero entre 1 y 100. ¡Adivina cual es!\n")

indice = 10
numero_secreto = rnd.randint(1, 100)
ingresa = 0


    
for x in range(1, indice + 1):
    print(f"\nIntento {x}/{indice}")
    
    try:

        ingresa = int(input("Ingresa tu adivinanza: "))

        if ingresa > numero_secreto:
            print("El numero es menor.")
        elif ingresa < numero_secreto:
            print("El numero es mayor.")
        else:
            print(f"\n¡Felicidades! ¡Has adivinado el numero secreto ({numero_secreto}) en {x} intentos!")
            break
           
    except ValueError:
        print("Debes ingresar un numero entero")

    except Exception as e:
        print("Debes ingresar un numero entero", e)

if ingresa != numero_secreto:
    print(f"\nLo siento el numero secreto era {numero_secreto}. ¡Mejor suerte la proxima vez!")
