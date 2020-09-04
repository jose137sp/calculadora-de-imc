print("\nCalculadora Indice de Masa Corporal")
p=float(input("Ingrese el peso en Kg: \n"))
t=float(input("Ingrese la talla en metros: \n"))

imc= p/(t**2)

if imc<18.5:
    print("\nUsted esta desnutrido :(...")
    print(("Su IMC es de: %.2f")%(imc))
elif imc>=18.5 and imc<=25.5:
    print("\nUsted esta saludable :)...")
    print(("Su IMC es de: %.2f")%(imc))
elif imc<25.5:
    print("\nUsted esta en sobrepeso :()...")
    print(("Su IMC es de: %.2f")%(imc))




