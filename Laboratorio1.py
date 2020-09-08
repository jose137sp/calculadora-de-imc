#Imprimir las opciones del Menú
def menu():
    print("\nSelecciona una opción")
    print("\t1 - Presentacion")
    print("\t2 - Tienda de zapatos")
    print("\t3 - Planilla")
    print("\t4 - Supermercado")
    print("\t5 - Salud")
    print("\t6 - Orden descendente")
    print("\t7 - salir")

#Problema 1 Tienda de Zapatos
def Zapatos():
    zapatos=int(input("Ingrese la cantidad de zapatos a comprar "))
    precio=15
    subtotal=precio*zapatos
    if zapatos<10:
        total= subtotal
    elif zapatos>=10 and zapatos<20 :
        total=subtotal-(subtotal*0.10)
    elif zapatos>=20 and zapatos<=25:
        total=subtotal-(subtotal*0.20)
    elif zapatos>=40:
        total=subtotal-(subtotal*0.40)    
    print("El total a pagar por",zapatos,"zapatos es de:",total)

#Problema 2 Planilla
def Planilla():
    print("Bienvenido al programa para calcular su sueldo semanal")
    horas = float(input("Introduzca la cantidad de horas que ha trabajado en la semana: "))
    if horas<=59:
        print("Su sueldo es de: ",(horas*25))
    elif horas>59:
        print("Su sueldo es de: ",((60*25)+((horas-59)*30)))


#Problema 3 Descuento de Supermercado
def Supermercado():
    print("Bienvenido al Programa para Calcular el descuento de su compra\npara iniciar,Ingrese su tipo de Membresía")
    membresia = int(input("1 para Membresia A, 2 para Membresia B, 3 para Membresia C: "))
    costo = int(input("Ingrese el costo total de su compra: "))
    if membresia == 1:
        descuento= costo*0.10
        total= costo-descuento
        print("El total con descuento es: ",total)
    elif membresia == 2:
        descuento= costo*0.15
        total= costo-descuento
        print("El total con descuento es: ",total) 
    elif membresia == 3:
        descuento= costo*0.20
        total= costo-descuento
        print("El total con descuento es: ",total)    

#Problema 4 Salud IMC
def Salud():
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
    elif imc>25.5:
        print("\nUsted esta en sobrepeso :()...")
        print(("Su IMC es de: %.2f")%(imc))

while True:
    # Mostramos el menu
    menu()
    # solicitamos una opción al usuario
    while True:
        opcionMenu = int(input("inserta un numero valor >> "))
        
        if opcionMenu == 1:
            print("\n        Universidad Tecnológica de Panamá \nFacultad de ingeniería de sistemas computacionales \nDepartamento de computación y simulación de sistemas \n               Laboratorio 1 \n             FC-FISC-1-8-2016")
            print("Integrantes:\nSebastian Arrivillaga E-8-159257\nFernando Estribí 8-969-1399\nJosé Saavedra 8-958-1993\nAnalissa Santos 8-963-703\nAna Saa 8-964-1448\n")
            break
        elif opcionMenu == 2:
            Zapatos()
            break
        elif opcionMenu == 3:
            Planilla()
            break
        elif opcionMenu == 4:
            Supermercado()
            break
        elif opcionMenu == 5:
            Salud()
            break
        elif opcionMenu == 6:
            print("Bienvenido al problema para mostrar los numeros en orden descendente")
            for i in range (31):
                print(("%d")%(30-i))
            break
        elif opcionMenu == 7:
            print("Si desea Salir introduzca 0")
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    i = int(input("Si desea volver a ver el Menú introduzca 1 "))
    if i!=1:
        break