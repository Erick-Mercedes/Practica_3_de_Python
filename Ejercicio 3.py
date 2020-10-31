# Pedir tres números por teclado e imprimir el mayor de ellos solamente.

E = int(input("Digitar el primer valor: "))
R = int(input("Digitar el segundo valor: "))
I = int(input("Digitar el tercer valor: "))

if E > R and E > I:
    print ("El primer numero es mayor")

elif R > E and R > I:
    print ("El segundo numero es mayor")

else:
    I > E and I > R
    print ("El tercer numero es mayor")
