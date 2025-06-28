#asignar e imprimir un nombre

nombre = "Juan Alberto"
print("El nombre es: ", nombre)

#asingar e imprimir varios datos personales

nombre = "Ana"
apellido = "Gómez"
ciudad = "Córdoba"

print("Nombre:", nombre)
print("Apellido:", apellido)
print("Ciudad:", ciudad)

print ("Su nombre es", nombre, apellido, "y vive en la ciudad de", ciudad)

#unir variables de texto para despues imprimirlas por pantalla

saludo = "Hola"
persona = "Carlos"
mensaje = saludo + " " + persona

print(mensaje)

#mostrar edad sin hacer calculos

nombre = "Lucía"
edad = "25"  # entre comillas para que sea texto
print(nombre + " tiene " + edad + " años.")
print (nombre, "tiene ", edad, "años!")

#reutilizar variables

mensaje = "Bienvenidos al curso de Python"
saludito = "esto es un saludo"
print(mensaje)
print(saludito)
print(mensaje)
print(mensaje)
print(mensaje)

#simular como una ficha de datos personales
nombre = "Mario"
documento = "12345678"
email = "mario@gmail.com"
print("##################")
print("#Ficha Personal: #")
print("##################")
print("Nombre:", nombre)
print("DNI:", documento)
print("Correo:", email)
print("##################")

#utilizar input para solicitar datos al usuario

nombre = input("¿Cómo te llamás? ")
ciudad = input("¿En qué ciudad vivís? ")

print("Hola", nombre + ", vivís en", ciudad + ".")

