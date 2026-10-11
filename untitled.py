# Gestor de Decisión para concesión de Crédito


# 1. Definición de Variables
nombre=input("ingrese su nombre con apellidos:")
edad=int(input("ingrese su edad:"))
ingreso_mensual=int(input("ingrese su sueldo mensual:"))
monto_solicitado=int(input("ingrese cuánto crédito desea solicitar:"))
dependientes_ecónomicos=int(input("ingrese cuántas personas dependen de usted:"))
plazo_meses=3
gasto_por_dependiente=2500

#2. Operadores Aritmeticos
pago_mensual= monto_solicitado/plazo_meses
sueldo_libre= ingreso_mensual-(dependientes_ecónomicos*gasto_por_dependiente)

#3.Datos calculados con resultado
print("Solicita crédito:",nombre)
#Primera condición es  ser mayor de 18 años 
if edad >=18:
   print("Crédito en revisión")
else:
  print("No eres mayor de edad, No es posible otorgarte un crédito")
  
#Segunda condición su ingreso mensual es mayor al monto solicitado Crédito Preaprobado
if ingreso_mensual>monto_solicitado and edad>=18:
   print("Crédito Pre-aprobado, cumple edad e ingresos")
elif ingreso_mensual>monto_solicitado and edad<18:
  print("No eres mayor de edad, No es posible otorgarte un crédito")
else:
  print("Su ingreso es inferior al monto solicitado, Crédito Rechazado")
  
#Tercer condición se determina si el sueldo libre es mayor que el monto que deberá pagar mensualmente y las previas condiciones fueron cumplidas de esta manera se determina si es aprobado o no

if sueldo_libre >=pago_mensual and edad>=18 and ingreso_mensual>monto_solicitado:
  print("Crédito Aprobado")
elif sueldo_libre>=pago_mensual and edad<18 and ingreso_mensual>monto_solicitado:
  print("No eres mayor de edad, No es posible otorgarte un crédito")
else:
  print("No es posible otorgarle esa cantidad de crédito, Crédito Rechazado")
  

