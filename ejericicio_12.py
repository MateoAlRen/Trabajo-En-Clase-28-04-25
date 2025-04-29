print("Listado de frutas")

frutas = ['Manzana', 'Pera', 'Aguacate', 'Arroz']

print(frutas)
eliminar = input("¿Cual fruta deseas eliminar?")

if eliminar in frutas:
    frutas.remove(eliminar)
else:
    print("La fruta no esta en la lista.")

print(frutas)