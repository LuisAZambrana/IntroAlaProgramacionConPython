# 1. Imprimir los números del 1 al 5 usando for

for i in range(1, 6):
    print(i)

# 2. Imprimir los números del 1 al 5 usando while

i = 1
while i <= 5:
    print(i)
    i += 1

# 3. Sumar los números del 1 al 10

suma = 0
for i in range(1, 11):
    suma += i
print("La suma es:", suma)

# 4. Mostrar los caracteres de una palabra
palabra = "Python"
for letra in palabra:
    print(letra)

#5. Contar hacia atrás del 5 al 1 usando while

i = 5
while i > 0:
    print(i)
    i -= 1
# 6. Mostrar los números pares del 1 al 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
#7. Pedir al usuario números hasta que ingrese 0

numero = int(input("Ingresa un número (0 para salir): "))
while numero != 0:
    print("Ingresaste:", numero)
    numero = int(input("Ingresa otro número (0 para salir): "))
# 8. Mostrar una tabla de multiplicar (por ejemplo del 3)

numero = 3
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 9. Adivina el número (juego simple con while)
secreto = 7
adivina = int(input("Adivina el número (entre 1 y 10): "))

while adivina != secreto:
    print("Incorrecto, intenta de nuevo.")
    adivina = int(input("Adivina el número (entre 1 y 10): "))

print("¡Correcto!")
