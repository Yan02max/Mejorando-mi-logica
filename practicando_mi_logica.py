import matplotlib as mp
import random as rd

#==============
# Crear Cuenta
#==============

try:
    nombre = input("Introduce Tu Nombre Completo: ").title()
    nombre_usuario = input("Introduce Un nombre de Usuario: ")
    edad = int(input("Introduce Tu Edad: "))
    pais = input("¿De Donde Eres?: ").upper()

    Datos = {
        "Nombre": nombre,
        "Usuario": nombre_usuario,
        "Edad": edad,
        "Pais": pais
    }

    if edad >= 18:
        # Crear contraseña
        while True:
            crear_contraseña = input("\nIngresa una contraseña: ")
            confirma_contraseña = input("Confirma la contraseña: ")

            if len(crear_contraseña) < 6:
                print("La contraseña debe tener al menos 6 caracteres.")
            elif crear_contraseña != confirma_contraseña:
                print("Las contraseñas no coinciden.")
            else:
                contraseña_guardar = crear_contraseña
                print("¡Contraseña guardada con éxito!")
                break

        # Bucle de inicio de sesión
        intentos = 3
        while intentos > 0:
            acceso = input("\nIntroduce la contraseña para iniciar sesión: ")
            if acceso == contraseña_guardar:
                print("\n¡Acceso confirmado!")
                print(f'Tus datos:\nNombre: {Datos["Nombre"]}')
                print(f'Usuario: {Datos["Usuario"]}')
                print(f'Edad: {Datos["Edad"]}')
                print(f'País: {Datos["Pais"]}')
                break
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
                else:
                    print("Has agotado el total de intentos. ¡Cuenta bloqueada!")

    else:
        print("No cumples la edad suficiente para crear una cuenta.")

except ValueError:
    print("La edad debe ser un número entero.")

except Exception as e:
    print("Este caracter no es valido.", e)
