from numpy import random

#Se inicializa la matriz de tamaño 3 para valores de poisson
x = random.poisson(lam=5, size=3) 

#Se inicializan las cajas
caja1 = []
caja2 = []
caja3 = []
caja4 = []

#Se incializan los contadores de clientes en las cajas
contador_caja1 = 0
contador_caja2 = 0
contador_caja3 = 0
contador_caja4 = 0

#Se incializan las colas que servirán para mantener el sistema
queue = []
final_queue = []

#Visualización del número de clientes y llenado de la matriz "queue"
i = 1
for x in x:
    print("En la", i , "hora entran", x)
    i = i + 1
    queue.append(x)
    
#Primer ciclo for que recorre las horas
for h in range(0,3):
    if h > 0: #Si ya se simulo al menos unos valores
        for m in range (1,61): ##Pasan minutos 
            print("Minuto ", m)
            if (caja1 == []): #Si la caja esta vacía
                if (final_queue != []): #Y si la matriz de la queue de la hora no esta vacía
                    contador_caja1 = contador_caja1 + 1 #Se acumula un cliente mas
                    r1= random.randint(1,10) #Tiempo que pasara el cliente en la caja 1
                    for k in range (r1): #Por cada minuto que pasará se genera una copia del número
                        caja1.append(final_queue[0]) #Se añade a la caja 1 el número "r1" veces repetido
                    final_queue.pop(0) #Se quita el número de la matriz de la hora
                    print("El cliente", caja1[0], "se encuentra en la caja 1, le quedan ", r1, "minutos")
            else:
                r1 = r1-1 #Si la caja no esta vacía 
                print("El cliente", caja1[0], "se encuentra en la caja 1, le quedan ", r1, "minutos")
                caja1.pop(0) #Se elimina el elemento 0 de la caja, es decir, se quita una repetición
            if (caja2 == [] ):
                if (final_queue != []):
                    contador_caja2 = contador_caja2 + 1
                    r2= random.randint(1,10)
                    for k in range (r2):
                        caja2.append(final_queue[0])
                    final_queue.pop(0)
                    print("El cliente", caja2[0], "se encuentra en la caja 2, le quedan ", r2, "minutos")
            else:
                r2 = r2-1
                print("El cliente", caja2[0], "se encuentra en la caja 2, le quedan ", r2, "minutos")
                caja2.pop(0)
            if (caja3 == [] ):
                if (final_queue != []):
                    contador_caja3 = contador_caja3 + 1
                    r3= random.randint(1,10)
                    for k in range (r3):
                        caja3.append(final_queue[0])
                    final_queue.pop(0)
                    print("El cliente", caja3[0], "se encuentra en la caja 3, le quedan ", r3, "minutos")
            else:
                r3 = r3-1
                print("El cliente", caja3[0], "se encuentra en la caja 3, le quedan ", r3, "minutos")
                caja3.pop(0)
            if (caja4 == [] ):
                if (final_queue != []):
                    contador_caja4 = contador_caja4 + 1
                    r4= random.randint(1,10)
                    for k in range (r4):
                        caja4.append(final_queue[0])
                    final_queue.pop(0)
                    print("El cliente", caja4[0], "se encuentra en la caja 4, le quedan ", r4, "minutos")
            else:
                r4 = r4-1
                print("El cliente", caja4[0], "se encuentra en la caja 4, le quedan ", r4, "minutos")
                caja4.pop(0)
                
    print("Hora ", h+1) 
    for g in range(queue[h]): #Se rellena la matriz de la hora
        ##print("Entra el cliente", g+1)
        final_queue.append(g+1)
        
#Se imprimen contadores totales 
print("El total de clientes de la caja 1 fue: ", contador_caja1)
print("El total de clientes de la caja 2 fue: ", contador_caja2)
print("El total de clientes de la caja 3 fue: ", contador_caja3)
print("El total de clientes de la caja 4 fue: ", contador_caja4)

