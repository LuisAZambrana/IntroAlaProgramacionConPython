#1. Crear una lista y mostrarla
frutas = ["manzana", "banana", "naranja"]
print(frutas)
#2. Acceder a un elemento por su índice
colores = ["rojo", "verde", "azul"]
print(colores[1])  # Muestra: verde
#3. Modificar un valor en la lista
nombres = ["Ana", "Luis", "Pedro"]
nombres[0] = "María"
print(nombres)
#4. Agregar un elemento al final
numeros = [1, 2, 3]
numeros.append(4)
print(numeros)
#5. Insertar un elemento en una posición específica
dias = ["lunes", "martes", "jueves"]
dias.insert(2, "miércoles")
print(dias)
#6. Eliminar un elemento por su valor
animales = ["perro", "gato", "pez"]
animales.remove("gato")
print(animales)
#7. Eliminar un elemento por su índice
paises = ["Argentina", "Brasil", "Chile"]
del paises[1]
print(paises)
#8. Recorrer una lista con un bucle for
lenguajes = ["Python", "Java", "C++"]
for lenguaje in lenguajes:
    print("Lenguaje:", lenguaje)
#9. Saber cuántos elementos tiene una lista
edades = [20, 25, 30, 35]
print("Cantidad de edades:", len(edades))
#10. Ordenar una lista
notas = [7, 10, 4, 6, 9]
notas.sort()
print("Notas ordenadas:", notas)


"""
Consignas para seguir practicando:
1-Crea una lista llamada alumnos que contenga tres nombres. Luego, mostrá la lista completa en pantalla.
2-Crea una lista de números del 1 al 4. Agregá el número 5 y luego eliminá el número 2. Mostrá la lista resultante.
3-Crea una lista con las estaciones del año: "verano", "otoño", "invierno", "primavera". Usá un bucle for para mostrar cada estación con el texto: "Estación: ___".
4-Dada la lista de edades [22, 18, 25, 20, 18], ordenala de menor a mayor y mostrá cuántos elementos hay en total.
"""
