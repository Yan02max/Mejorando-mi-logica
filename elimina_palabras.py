tareas = []


while True:
    tarea = input("Escribe una tarea: ")
    tareas.append(tarea)

    decision = input("¿Agregar otra? (s/n): ").lower()
    if decision == "n":
        break

print("\nTus tareas son:")
for i, tarea in enumerate(tareas, start=1):
    print(i, tarea)

eliminar = input("\n¿Quieres eliminar una tarea? (s/n): ").lower()

if eliminar == "s":
    numero = int(input("Número de la tarea a eliminar: "))

    if 1 <= numero <= len(tareas):
        tareas.pop(numero - 1)
        print("\nTarea eliminada.")
    else:
        print("Número inválido.")

print("\nLista final de tareas:")
for i, tarea in enumerate(tareas, start=1):
    print(i, tarea)


