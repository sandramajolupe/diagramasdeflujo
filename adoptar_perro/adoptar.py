print ("ENCONTRAR POSIBLES FUNDACIONES Y /O REFUGIOS DE GATOS.")
refugioFundacion = input().upper()
if refugioFundacion == "SI":
    print ("esta en bogota")
    estaBogota = input().upper()
    if estaBogota == "SI":
        print ("desparasitado")
    else:
       print ("no se adopta")

desparasitado =input().upper()

if desparasitado == "SI":
    print ("macho")
else:
    print ("no se adopta")
    
macho =input().upper()
if macho == "SI":
    print ("es mayor 3 meses")
else:
    print ("no se adopta")
    
mayor3meses =input().upper()
if mayor3meses == "SI":
    print ("es color gris")
else:
    print ("no se adopta")
    

colorgris =input().upper()
if colorgris == "SI":
    print ("se adopta")
else:
       print ("no se adopta")
