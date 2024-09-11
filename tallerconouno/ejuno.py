# Elabore un programa para la Universidad de Florida que calcule los primeros 100 números de la siguiente serie 5, 8, 13, 21, ... sin mostrar el 13, y muestre la lista del resultado de los números.


a = 5
b = 8

#diccionario para serie y posicion
serie = {}
posicion = 1

# Calculamos los primeros 100 números de la serie
while posicion <= 100:
    # Calculamos el siguiente número en la serie
    nsiguiente = a + b
    
    # Verificamos si el número es diferente de 13 antes de agregarlo al diccionario
    if nsiguiente != 13:
        serie[posicion] = nsiguiente
        posicion += 1
    
    # a y b para el siguiente ciclo
    a = b
    b = nsiguiente


print(serie)
