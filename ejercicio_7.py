print("Conducción segura.\n")

n1 = input("¿Llevas casco? s/n")
n2 = input("¿Llevas licencia? s/n")

if n1 != 's' and n2 != 's':
    print("No puedes conducir")
else:
    print("Puedes conducir")