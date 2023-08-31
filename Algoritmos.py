#Conjetura de Collatz
def collatz():
  #Se lee el valor de "N"
  n = int(input("Ingrese un numero: "))

  while (n!=1):
    if (n % 2 == 0):
        n = n/2
    else:
        n = (3*n) + 1
    print("Valor de 'N': ",n)

#Constante de Kaprekar
def kaprekar():
  num_ord = int(0)
  num_inv = int(0)
  res = 0
  ciclo = int(1)

  def numero():
    num = int(input("Ingrese numero: "))
    if(num>999 and num<=9999):      
      arreglo = [int(x) for x in str(num)]
      print(arreglo)
      return arreglo
    else:
      print("Ingrese un numero de 4 cifras")

  def repetidos(valor):
    if(len(valor) != len(set(valor))):
      return True
    else:
      return False
      
  bandera = bool(True)
  while(bandera):
    valor = numero()
    if(valor):
      bandera = repetidos(valor)

  #guardar numero ordenado ascendente y descendente
  aux1 = sorted(valor)
  print("Ascendente: ",aux1)
  aux2 = list(reversed(aux1))
  print("Descendente: ",aux2)

  for current_digit in aux1:
    num_ord = num_ord*10 + current_digit

  for current_digit in aux2:
    num_inv = num_inv*10 + current_digit

  while(res!=6174):
    res = num_ord - num_inv
    if(res < 0):
      res = (res * (-1))
    print("Valor: ",res) 
    if(res!=6174):
      ciclo += 1
      num_ord = 0
      num_inv = 0
      aux1 = [int(x) for x in str(res)]
      print("Auxiliar: ",aux1)
      aux1 = sorted(aux1)
      aux2 = list(reversed(aux1))
      for current_digit in aux1:
        num_ord = num_ord*10 + current_digit    
      for current_digit in aux2:
        num_inv = num_inv*10 + current_digit
      print("Ordenado: ",num_ord)
      print("Invertido: ",num_inv)
      print("Ciclo: ", ciclo)


#Multiplicación Rusa
def mult_rus():
  res = int(0)
  #Ingresa multiplicador = x
  x = int(input("Ingrese multiplicador: "))
  #Ingresa multiplicando = y
  y = int(input("Ingrese multiplicando: "))

  while(x!=0):
      if (x % 2 != 0):
        res += y
      x = int(x/2)
      y = y * 2
  print("El resultado de la multiplicacion es: ",res)


#Multiplicacion Egipcia
def mult_egip():
  res = int(0)
  bandera = bool(False)
  #multiplicador = a
  a = int(input("Multiplicador: "))
  #multiplicando = b
  b = int(input("Multiplicando: "))
  #auxiliares
  aux1 = a
  aux2 = int(1)
  aux3 = int(0)

  while(aux2 < b and bandera!=True):
    if((aux2*2)>b):
      bandera = True
      break;
    else:
      aux1 = aux1 * 2
      aux2 = aux2 * 2
  suma = int(0)

  while(aux1>=a):
    if((suma+aux2)<=b):
      suma += aux2
      res += aux1
    aux1 = int(aux1/2)
    aux2 = int(aux2/2)
  print("Resultado: ",res)


#Funcion main 
opcion = int(0)
#Menu de opciones 
while(opcion!=5):
  print("1.- Collatz\n2.-Kaprekar\n3.- Multiplicacion Rusa\n4.- Multiplicacion Egipcia\n5.- Salida")
  opcion = int(input("Ingrese una opcion: "))
  if(opcion == 1):
    collatz()
  elif opcion == 2:
    kaprekar()
  elif opcion == 3:
    mult_rus()
  elif opcion == 4:
    mult_egip()
  elif opcion == 5:
    print("Fin de programa")
  else:
    print("Ingrese una opcion valida")