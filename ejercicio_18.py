print("Cambio de posición")

ls = [10,20,30,40,50]

numero = int(input("Numero que desea agregar:  "))
posicion = int(input("Lugar en el cual desea ponerlo (0 a 4):  "))

ls.insert(posicion, numero)
print(f"Lista actualizada: {ls}")