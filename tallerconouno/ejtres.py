#3)	Elabore un programa para la facultad de Ingeniería que pida 400 números e indique si ese número es par o impar; me muestre un listado y me indique cuantos son pares y cuantos son impares.

# Contadores
conpares = 0
conimpares = 0

# Número de entradas
numeros = 10
iniciocont = 1

# Lista para almacenar la información de los números
numerosinfo = []


for i in range(iniciocont, numeros + 1):
    
    if i % 2 == 0:
        tipo = 'Par'
        conpares += 1
    else:
        tipo = 'Impar'
        conimpares += 1
    
    # Guardamos  en la lista
    numerosinfo.append({
        'Número': i,
        'Tipo': tipo
    })

# Listado de números
print("\nListado de números:")
for info in numerosinfo:
    print(f"Número {info['Número']}: {info['Tipo']}")

# Pares e impares
print(f"\nTotal de números pares: {conpares}")
print(f"Total de números impares: {conimpares}")
