#Importacion librerias
import numpy as np
import matplotlib.pyplot as plt

#Clase Perceptron
class Perceptron:
  #Declaramos los pesos
  def __init__(self):
    self.pesos = np.array([0,1,1], dtype='f')
    self.pesosDefinitivos = np.array([]) 

  #Método que calcula la propagacion de las entradas
  def propagacion (self , entradas):
    #Cogemos las entradas y los guardamos en el ojeto self
    self.entradas = entradas

    #Variable bandera
    sumatorio = 0

    #Bucle para crear el sumatorio
    for i in range (0,len(self.pesos)):
      sumatorio += self.pesos[i] * self.entradas[i]
    
    #Funcion Paso
    if (sumatorio > 0):
      self.salida = 1
    else:
      self.salida = 0

    return(self.salida)



  #Método para actualizar pesos
  def actualizacion_pesos (self, alfa, salidad,error=None):
    #Bucle para actualizar pesos
    

    if error==None:
      #Bucle para actualizar pesos
      error_repartido=[(self.pesos[1]*(salidad-self.salida)),(self.pesos[2]*(salidad-self.salida))]
      for i in range(0, len(self.pesos)):
        self.pesos[i] = self.pesos[i] + (alfa * (salidad - self.salida) * self.entradas[i])

      return error_repartido
      # print("Peso sin error")
    else:
      for i in range(0, len(self.pesos)):
        self.pesos[i] = self.pesos[i] + (alfa * error * self.entradas[i])
      
      return None

  def repartir_error(self,salidad):
      errores=[]
      
      error_a_repartir=(salidad - self.salida)

      for peso in self.pesos:
        errores.append(error_a_repartir*peso)
      
      return errores


def feed_fordward(entradas,neuronas):

  #fase 1: Entrada de datos en la capa oculta.
  
    #Llamamos a la funcion propagacion
  n0=neuronas[0][0].propagacion(entradas)
  n1=neuronas[0][1].propagacion(entradas)
  resultado=neuronas[1].propagacion([1,n0,n1])
  
  return resultado

#Objeto de tipo Perceptron
# perceptron_and = Perceptron()
perceptron_xor = [[Perceptron(),Perceptron()],Perceptron()]

#Variable que guarda los pesos 
# grad_pesos = [perceptron_xor[1].pesos]

def backpropagation(neuronas):
  errores_ocultas=neuronas[1].actualizacion_pesos(0.1, ejemplosXOR[i,3])
  # grad_pesos = np.concatenate((grad_pesos, [neuronas[1].pesos]), axis = 0)
  # print("Etapa" , epoca + 1)
  # pesosXOR(neuronas[1])

  for n,e in zip(neuronas[0],errores_ocultas):
    n.actualizacion_pesos(0.1, ejemplosXOR[i,3],error=e)
    # grad_pesos = np.concatenate((grad_pesos, [n.pesos]), axis = 0)
    # print("Etapa" , epoca + 1)
    # pesosXOR(n)


#Tabla de verdad
# ejemplos = np.array([[1,0,0,0], [1,0,1,0], [1,1,0,0], [1,1,1,1]], dtype='f')

ejemplosXOR = np.array([[1,0,0,0], [1,0,1,1], [1,1,0,1], [1,1,1,0]], dtype='f')



#Convertir los pesos a tipo de datos double
# pesos_definitivos = []
# def pesos():
#     for i in range(0,3):
#       j = perceptron_and.pesos[i]
#       j = round(j , 2)
#       pesos_definitivos.append(j)
#       # print("El peso w", i , " es  ==> ", j)
    
pesos_definitivosXOR = []
def pesosXOR(neurona):
    for i in range(0,3):
      j = neurona.pesos[i]
      j = round(j , 2)
      pesos_definitivosXOR.append(j)
      # print("El peso w", i , " es  ==> ", j)


#Bucle de epocas
# for epoca in range(0,100):
#   #Bucle para las 4 entradas
#     for i in range(0,4):
#     #Llamamos a la funcion propagacion
#         perceptron_and.propagacion(ejemplos[i, 0:3])
#     #Comprobamos para actualizar o no y ademas concatenamos los valores de los pesos en la variable que hemos creado antes
#         if (perceptron_and.salida != ejemplos[i,3]):
#           perceptron_and.actualizacion_pesos(0.1, ejemplos[i,3])
#           grad_pesos = np.concatenate((grad_pesos, [perceptron_and.pesos]), axis = 0)
#           # print("Etapa" , epoca + 1)
#           pesos()
          
#           break


for epoca in range(0,100):
  #Bucle para las 4 entradas
    for i in range(0,4):
    #Llamamos a la funcion propagacion
      salida=feed_fordward(ejemplosXOR[i,0:3],perceptron_xor)

    #Comprobamos para actualizar o no y ademas concatenamos los valores de los pesos en la variable que hemos creado antes
      if (salida != ejemplosXOR[i,3]):
        backpropagation(perceptron_xor)

        break  
          
   


#Test del Modelo
for i in  range(0,4):

  resultado=feed_fordward(ejemplosXOR[i,0:3],perceptron_xor)
  print(f""" 
  Entradas:
  {ejemplosXOR[i,0:3]}
  Expected:
  {ejemplosXOR[i,3]}
  Resultado:
  {resultado}
  """)



#Pintar con matplotib la evolucion de los pesos en las diferentes etapas 
# plt.plot(grad_pesos[:,0], 'k')
# plt.plot(grad_pesos[:,1], 'r')
# plt.plot(grad_pesos[:,2], 'b')

# plt.show()