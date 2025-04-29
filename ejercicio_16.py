print("Ubicación de Numeros")

ls = [1,23,77,45,24]

busqueda = int(input("Ingrese el numero que desea encontrar:  "))

if busqueda in ls:
    buscar = ls.index(busqueda)
    print(f"El numero {busqueda} está en ls en la posición {buscar}.")
else:
    print(f"El numero {busqueda} no se encuentra en la lista.")

