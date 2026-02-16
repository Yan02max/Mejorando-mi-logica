
empleados = [
    {"nombre": "Ana", "salario": 1200, "departamento": "IT"},
    {"nombre": "Luis", "salario": 900, "departamento": "Ventas"},
    {"nombre": "Carlos", "salario": 1500, "departamento": "IT"},
    {"nombre": "Marta", "salario": 1100, "departamento": "HR"},
    {"nombre": "Sofia", "salario": 2000, "departamento": "Ventas"}
]
# Almacen De Datos.
departamentos = {}

for emp in empleados:
    depto = emp["departamento"]
    sal = emp["salario"]

    if depto not in departamentos:
        departamentos[depto] = {
            "total": sal,
            "cantidad": 1
    }
    else:
        departamentos[depto]["total"] += sal
        departamentos[depto]["cantidad"] += 1


promedios = {}
for depto, datos in departamentos.items():
    promedios[depto] = datos["total"] / datos["cantidad"]
    print(f"Promedio salarial en {depto}: ${promedios[depto]:.2f}")
    print(f"Cuántos empleados trabajan en el area de {depto}: {datos['cantidad']}")

# Promedio mas alto.
depto_mayor_salario = max(promedios, key=promedios.get)
mayor_promedio = promedios[depto_mayor_salario]
print("Qué departamento tiene el salario promedio más alto:", depto_mayor_salario, mayor_promedio)

