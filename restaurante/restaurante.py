print ("Entrar a la pagina, si o no")
ingresarALaPagina = input().upper()
if ingresarALaPagina == "SI":
   print ("llenar formulario")
   print ("Número de documento")
   cedula = input()
   print ("Nombre completo")
   nombre = input()
   
   print ("recordar, si o no")
   recordar =input().upper()
   if recordar == "SI":
      print ("Recordar usuario")
      print ("Escoger día y hora de la reserva")
      dia_hora = input()
      print ("confirmar reserva")
      print ("reserva exitosa")
   
   else:
       print ("Escoger día y hora de la reserva")
       dia_hora = input()
       dia_hora = input()
       print ("confirmar reserva")
       print ("reserva exitosa")
else :
    print("Nose hace reserva")


