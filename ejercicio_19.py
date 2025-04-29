print("Lista exclusiva de numeros pares.")

ls = []

for i in range(5):
    numero = int(input("Ingrese su numero"))
    if numero % 2 == 0:
        ls.append(numero)

print("Los numeros que lograste ingresar fueron:  ", ls)