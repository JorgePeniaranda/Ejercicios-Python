# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad = float(input('Ingrese la cantidad a invertir: '))
interes_anual = float(input('Ingrese el interes anual: '))
anios = int(input('Ingrese el plazo en años: '))
capital_obtenido = cantidad * (1+interes_anual/100)**anios

print(f"El capital obtenido en {anios} invirtiendo {cantidad} con un interes de {interes_anual} es de: {capital_obtenido}")