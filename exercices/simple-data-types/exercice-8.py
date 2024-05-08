# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

numero_1 = int(input('Ingrese el primer numero entero: '))
numero_2 = int(input('Ingrese el segundo numero entero: '))
cociente = numero_1 // numero_2
resto = numero_1 % numero_2

print(f"{numero_1} entre {numero_2} da un cociente {cociente} y un resto {resto}")