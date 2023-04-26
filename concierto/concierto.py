print ("Ingresar a Tuboleta\nVerificar conciertos en Bogota\nConcierto es de salsa ")
concierto= input()
if concierto == "si" :
    print("selecciona el concierto\nBuscar sillas en platea\nVerifica el precio, supera los 2 millones de pesos")
    precio = input()
    if precio == "si" :
        print ("No compra")
    else:
        print ("Elige el servicio de bebidas")
        print ("Elige metodo de pago")
        print ("comprar")
else :
    print ("Aviso: No hay disponibles")
