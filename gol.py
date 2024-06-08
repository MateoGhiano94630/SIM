import random
def gol():
    
    primer_vector = [0] * 11
    n = 100
    acu = 0
    acu_precio = 0
 
    
    for i in range(n):
        primer_vector[3] = 0
        primer_vector[4] = 0
        primer_vector[5] = 0
        primer_vector[6] = 0
        primer_vector[7] = 0
        primer_vector[8] = 0
        primer_vector[0] = i
        primer_vector[1] = random.random()
        if primer_vector[1] > 0.29:
            primer_vector[2] = "Sí abrio"
            primer_vector[3] = random.random()
            if primer_vector[3] < 0.20:
                # abre señor
                primer_vector[4] = "Señor"
                primer_vector[5] = random.random()
                if primer_vector[5] < 0.25:
                    primer_vector[6] = "Si vende"
                    primer_vector[7] = random.random()
                    if primer_vector[7] < 0.10:
                        # vende 1 
                        primer_vector[8] = 1
                        acu += primer_vector[8]
                        
                    elif primer_vector[7] < 0.50:
                        # vende 2 
                        primer_vector[8] = 2
                        acu += primer_vector[8]
                        acu_precio = acu * 200
                    elif primer_vector[7] < 0.80:
                        # vende 3 
                        primer_vector[8] = 3
                        acu += primer_vector[8]
                        acu_precio = acu * 200
                    else:
                        # vende 4
                        primer_vector[8] = 1
                        acu += primer_vector[8]
                        acu_precio = acu * 200
                        
                else:
                    # no vende
                    primer_vector[6] = "No vende"
                   
                    
                    
        
            else:
                primer_vector[4] = "Señora"
                primer_vector[5] = random.random()
                if primer_vector[5] < 0.15:
                    primer_vector[6] = "Si vende"
                    primer_vector[7] = random.random()
                    if primer_vector[7] < 0.60:
                        # vende 1 
                        primer_vector[8] = 1
                        acu += primer_vector[8]
                        acu_precio = acu * 200
                    elif primer_vector[7] < 0.90:
                        # vende 2 
                        primer_vector[8] = 2
                        acu += primer_vector[8]
                        acu_precio = acu * 200
                    else:
                        # vende 3 
                        primer_vector[8] = 3
                        acu += primer_vector[8]
                        acu_precio = acu * 200
                
                else:
                    # no vende
                     # no vende
                    primer_vector[6] = "No vende"
                    
                    
       
        else:
             primer_vector[2] = "No abrio"
         
             
        primer_vector[9] += acu
        primer_vector[10]+= acu_precio
        print(primer_vector)

 
        
       
    
    print(primer_vector)
    
    
gol()