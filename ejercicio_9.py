print("Calificación\n")

n1 = float(input("Dime tu calificación:  "))

if n1 < 0 and n1 > 10:
    print("Caracter no valido")
elif n1 >= 0 and n1 < 5:
    print("Reprobado.")
elif n1 >= 6 and n1 < 8:
    print("Aprobado.")
elif n1 >= 8 and n1 <= 10:
    print("Sobresaliente")