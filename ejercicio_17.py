print("Numero de veces que aparece un nombre")

ls = ['Mateo', 'Julian', 'Samuel', 'Samuel', 'Ana', 'Samuel']

nombre = input("Ingrese el nombre que quiere contar:  ")

contador = ls.count(nombre)
print(f"El nombre {nombre} aparece {contador} veces.")