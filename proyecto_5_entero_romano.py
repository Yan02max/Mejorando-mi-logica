# =============================
# Diccionario De Numero Romanos
# =============================

Romanos_numeros = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000
            }
                   
# =====================
# Algoritmo de programa
# =====================
try:

    eleccion = input("Ingresa Un Numero Romano Para Convertir a Entero: ").upper()
    numero_entero = 0
    numero_anteriol = 0

    # Inverti la operacion 
    for caracter in eleccion[::-1]:
        # El get se uso para consultar o buscar los caracteres
        Numero_actual = Romanos_numeros.get(caracter, 0)
        # Se creo esta condiciones para calcular el numero exacto a convertir
        if Numero_actual < numero_anteriol:
            numero_entero -= Numero_actual
        else:
            numero_entero += Numero_actual
        # Se asigna para guardar temporal mente el numero convertido
        numero_anteriol = Numero_actual
    # Aqui tenemos el resultado del numero convertido
    print("Resultado", numero_entero)

except Exception as e:
    print("Ingresa un numero romano valido.", e)
