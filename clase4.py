#Ejercicio 1: ¿Es mayor de edad?
edad = int(input("Ingresá tu edad: "))

if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")
# Ejercicio 2: Número positivo, negativo o cero
numero = int(input("Ingresá un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
# Ejercicio 3: Verificar contraseña

contraseña = input("Ingresá la contraseña: ")

if contraseña == "python123":
    print("Contraseña correcta. Bienvenido.")
else:
    print("Contraseña incorrecta.")
# Ejercicio 4: Clasificación de nota
nota = int(input("Ingresá tu nota (0 a 10): "))

if nota >= 6:
    print("Aprobado")
elif nota >= 4:
    print("Desaprobado, pero cerca.")
else:
    print("Desaprobado.")
# Ejercicio 5: ¿Número par o impar?
numero = int(input("Ingresá un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
# Ejercicio 6: Menú de opciones
print("Menú:")
print("1. Saludar")
print("2. Mostrar edad")
print("3. Salir")

opcion = input("Elegí una opción (1/2/3): ")

if opcion == "1":
    print("¡Hola!")
elif opcion == "2":
    print("Tenés 25 años.")
elif opcion == "3":
    print("Chau, gracias por usar el programa.")
else:
    print("Opción no válida.")

# yapa probando con dos condiciones

edad = int(input("Ingresá tu edad: "))
curso_basico = input("¿Completaste el curso básico? (si/no): ")

if edad > 18 and curso_basico == "si":
    print("Podés inscribirte al curso avanzado.")
elif edad <= 18 and curso_basico == "si":
    print("Todavía sos menor de edad para este curso.")
elif edad > 18 and curso_basico != "si":
    print("Necesitás completar el curso básico primero.")
else:
    print("No cumplís con los requisitos para inscribirte.")




