print("Edades\n")

n1 = int(input("Por favor, ingrese su edad:  "))

if n1 >= 0 and n1 <= 12:
    print("Eres un niño.")
elif n1 >= 13 and n1 < 18:
    print("Eres un adolecente.")
elif n1 >= 18 and n1 < 50:
    print ("Eres un adulto")
elif n1 >= 50 and n1 < 120:
    print ("Eres un anciano.")
else:
    print("Edad no valida")