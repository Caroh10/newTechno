#2)	Elabore un programa para el Éxito que determine el salario de los 1897 empleados de su compañía, teniendo en cuenta las comisiones y la seguridad social que debe pagar, e imprima el listado de la información. 


# Variables
salario = float(input("Por favor ingrese el salario base de los empleados: "))
comision = float(input("Por favor ingrese la comisión de los empleados: "))
nempleados = 1897 
ssocial = salario * 0.08  # Deducción de seguridad social

# Lista para almacenar  de los empleados
empleados = []

# Calculamos el salario para cada empleado
for i in range(1, nempleados + 1):
    salariototal = (salario + comision) - ssocial
    
    # Guardamos en la lista
    empleados.append({
        'Empleado': i,
        'Salario Base': salario,
        'Comisión': comision,
        'Deducción Seguridad Social': ssocial,
        'Salario Neto': salariototal
    })

# Imprimimos la información de cada empleado
print("\nListado de empleados:")
for empleado in empleados:
    print(f"Empleado {empleado['Empleado']}:")
    print(f"  Salario Base: {empleado['Salario Base']:.2f}")
    print(f"  Comisión: {empleado['Comisión']:.2f}")
    print(f"  Deducción Seguridad Social: {empleado['Deducción Seguridad Social']:.2f}")
    print(f"  Salario Neto: {empleado['Salario Neto']:.2f}")
    print()
