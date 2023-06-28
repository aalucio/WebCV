import numpy as np


X0 = 1
X1 = [0,0,1,1]
X2 = [0,1,0,1]

AND=[0,0,0,1]
OR=[0,1,1,1]
Yesperado = AND
#Yesperado = OR



#Pesos
W0 = 0
W1 = 1
W2 = 1


 # BIAS O = (W0 * X0)

U = 0.1 


# Y0 = (W1 * X1[0] + W2 * X2[0] + W0 * X0)
etapa=1
fin=False
while etapa<100 and not fin:
    
    print("Esta es la ", etapa," etapa. ",)
    for i in range(len(X1)):
        
        Y = round(((W1 * X1[i]) + (W2 * X2[i])) + (W0 * X0),2)
        print('y',i,'=', Y)
        # comprobar si es mayor a 0
        if Y >0:
            paso = 1
            if paso != Yesperado[i]:
                AW0 = round(U * ( Yesperado[i] - paso ) * X0, 2)
                W0 = round(AW0 + W0,2)
                
                AW1 = round(U * ( Yesperado[i] - paso ) * X1[i], 2)
                W1 = round(AW1 + W1,2)
                
                AW2 = round(U * ( Yesperado[i] - paso ) * X2[i],2)
                W2 = round(AW2 + W2,2)
                
                print("se recalculan los pesos :W0=", W0, "W1: ", W1,"W2: ", W2 )
                
                break
            else:
                print("El valor de ",  "es el deseado.")
        else:
            paso = 0
            if paso != Yesperado[i]:
                AW0 = round(U * ( Yesperado[i] - paso ) * X0, 2)
                W0 = round(AW0 + W0,2)
                
                AW1 = round(U * ( Yesperado[i] - paso ) * X1[i], 2)
                W1 = round(AW1 + W1,2)
                
                AW2 = round(U * ( Yesperado[i] - paso ) * X2[i],2)
                W2 = round(AW2 + W2,2)
                
                print("se recalculan los pesos :w0=", W0, "w1: ", W1,"w2: ", W2 )
                break
            else:
                
                print("El valor de ",   "es el deseado.")
        ####
        if(i==3 and (Yesperado[i]==paso)):
            fin=True

        
    etapa+=1
        
         
            
        







