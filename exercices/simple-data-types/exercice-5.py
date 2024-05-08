# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = float(input('Ingrese horas trabajadas: '))
costo_por_hora = float(input('Ingrese coste por hora: '))

print(f"Le corresponde un pago de: {horas_trabajadas * costo_por_hora}")