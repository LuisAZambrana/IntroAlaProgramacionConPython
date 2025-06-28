# Clase 3 Ejercicio 1

a = 10
b = 5
print("Suma:", a + b)

# Clase 3 Ejercicio 2

x = 7
y = 3
print("Resta:", x - y)

# Clase 3 Ejercicio 3

n1 = 4
n2 = 2
print("Multiplicación:", n1 * n2)

# Clase 3 Ejercicio 4

m1 = 20
m2 = 4
print("División:", m1 / m2)

# Clase 3 Ejercicio 5

a1 = 15
b1 = 4
print("División entera:", a1 // b1)
print("Resto:", a1 % b1)

# Clase 3 Ejercicio 6
edad = 18
print("¿Es mayor de edad?", edad >= 18)

# Clase 3 Ejercicio 7

a3 = 10
b3 = 20
print("¿a3 es igual a b3?", a3 == b3)

# Clase 3 Ejercicio 8
nota = 7
print("¿Aprobó la materia?", nota >= 6)

# Clase 3 Ejercicio 9
mayor_edad = True
tiene_dni = True
print("¿Puede votar?", mayor_edad and tiene_dni)

# Clase 3 Ejercicio 10
es_admin = False
tiene_permiso = True
print("¿Puede ingresar?", es_admin or tiene_permiso)

#Ejercicio final de practica
"""
Consigna: Crear un programa que reciba dos números del usuario y diga:

Si son iguales o no.

Cuál es mayor.

Si ambos números son mayores a 10.

Si al menos uno de los dos es menor a 5.
"""

#Resultado del ejercicio final:
n1 = int(input("Ingresá el primer número: "))
n2 = int(input("Ingresá el segundo número: "))

print("¿Son iguales?", n1 == n2)
print("¿Cuál es mayor?")
if n1 > n2:
    print("El primer número es mayor.")
elif n2 > n1:
    print("El segundo número es mayor.")
else:
    print("Son iguales.")

print("¿Ambos son mayores a 10?", n1 > 10 and n2 > 10)
print("¿Alguno es menor a 5?", n1 < 5 or n2 < 5)



