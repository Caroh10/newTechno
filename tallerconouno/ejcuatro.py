#Elabore un programa para un Hospital que determine, y muestre el nivel de Leucemia de 803 pacientes clasificando su puntaje si esta inferior a 10 no tiene Leucemia; si esta entre 11 y 40, nivel bajo de Leucemia; si esta entre 40 y 69, nivel moderado de Leucemia, si esta entre 70 y 100, nivel grave de Leucemia.

import random

# Contadores 
noleucemia = 0
nivelbajo = 0
nivelmoderado = 0
nivelgrave = 0

npacientes = 803

# Lista para almacenar la información de los pacientes
pacientes_info = []

# puntajes aleatorios 
for i in range(1, npacientes + 1):
    
    puntaje = random.randint(0, 100)  # Genera un puntaje entre 0 y 100
    
   
    if puntaje <= 10:
        nivel = 'No tiene Leucemia'
        noleucemia += 1
    elif 11 <= puntaje <= 40:
        nivel = 'Nivel Bajo de Leucemia'
        nivelbajo += 1
    elif 41 <= puntaje <= 69:
        nivel = 'Nivel Moderado de Leucemia'
        nivelmoderado += 1
    else:
        nivel = 'Nivel Grave de Leucemia'
        nivelgrave += 1
    
    # Guard en la lista
    pacientes_info.append({
        'Paciente': i,
        'Puntaje': puntaje,
        'Nivel de Leucemia': nivel
    })

# Listado de pacientes
print("\nListado de pacientes:")
for info in pacientes_info:
    print(f"Paciente {info['Paciente']}: Puntaje {info['Puntaje']}, {info['Nivel de Leucemia']}")

# Conteo de cada nivel de leucemia
print(f"\nTotal de pacientes con Leucemia No: {noleucemia}")
print(f"Total de pacientes con Leucemia Nivel Bajo: {nivelbajo}")
print(f"Total de pacientes con Leucemia Nivel Moderado: {nivelmoderado}")
print(f"Total de pacientes con Leucemia Nivel Grave: {nivelgrave}")
