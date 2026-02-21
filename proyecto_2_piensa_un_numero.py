import random 
print("Piensa en un numero entre 1 y 100. Yo tratare de adivinarlo.")

intento = 0
adivinanza_mi = 1
adivinanza_ma = 100
adivinanza_ac = 0

while True:
    intento += 1
    try:
        adivinanza_ac = random.randint(adivinanza_mi, adivinanza_ma)
        print(f"¿Es {adivinanza_ac} tu numero?")
        numero = input("Ingresa 'Mayor', 'Menor' o 'Correcto': ").lower()

        if numero == "correcto":
            print(f"¡Adivine tu numero ({adivinanza_ac}) en {intento} intentos!")
            break
        elif numero == "mayor":
            adivinanza_mi = adivinanza_ac + 1
        elif numero == "menor":
            adivinanza_ma = adivinanza_ac - 1
        else:
            print("Respuesta no valida. Ingresa 'Mayor', 'Menor' o 'Correcto'.")
    except Exception:
        print("\nYa e adivinado tu numero y no lo reconociste.")
        break

        




       
        
          