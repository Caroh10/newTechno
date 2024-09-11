#5)	Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas de metro cable, registrando un puntaje que se clasifica de la siguiente forma si tiene 2 puntos está con un funcionamiento defectuoso, si tiene 3 puntos el funcionamiento es moderado y si tiene 4 puntos el funcionamiento es óptimo.

#Variables
ncabinas = 407

# Diccionario para la información de las cabinas
cabinasinfo = {}

# Inicializar contadores para cada categoría
defectuoso = 0
moderado = 0
optimo = 0

# Asignamos puntajes y clasificamos el funcionamiento
for i in range(1, ncabinas + 1):
    
    puntaje = 2 + (i % 3)  # secuencia de puntajes: 2, 3, 4 repetidamente
    
   
    if puntaje == 2:
        estado = 'Funcionamiento Defectuoso'
        defectuoso += 1
    elif puntaje == 3:
        estado = 'Funcionamiento Moderado'
        moderado += 1
    elif puntaje == 4:
        estado = 'Funcionamiento Óptimo'
        optimo += 1
    
    # Guardamos en el diccionario
    cabinasinfo[i] = {
        'Puntaje': puntaje,
        'Estado': estado
    }

# Listado de cabinas
print("\nListado de cabinas:")
for cabina, info in cabinasinfo.items():
    print(f"Cabina {cabina}: Puntaje {info['Puntaje']}, {info['Estado']}")


print(f"\nTotal de cabinas con Funcionamiento Defectuoso: {defectuoso}")
print(f"Total de cabinas con Funcionamiento Moderado: {moderado}")
print(f"Total de cabinas con Funcionamiento Óptimo: {optimo}")
