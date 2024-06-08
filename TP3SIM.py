import random
import tkinter as tk
from 
from tkinter import ttk
from tabulate import tabulate



class Montecarlo:
    def __init__(self, root):
        # PESTAÑA 1
        pestaña(self, root)
    def generador(self):
        tabla(self)
        
        
       

def pestaña(self, root):
    self.root = root
    self.root.title("Montecarlo")
    self.notebook = ttk.Notebook(root)
    self.notebook.pack(fill=tk.BOTH, expand=True)

    self.tab1 = ttk.Frame(self.notebook)
    self.notebook.add(self.tab1, text="Vendedor de revistas")

    self.label_N = ttk.Label(self.tab1, text="Cantidad de visitas (n):")
    self.label_N.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_N = ttk.Entry(self.tab1)
    self.entry_N.grid(row=1, column=1, padx=10, pady=5)
    
    self.label_inf = ttk.Label(self.tab1, text="Limite inferior")
    self.label_inf.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    
    
    self.entry_inf = ttk.Entry(self.tab1)
    self.entry_inf.grid(row=2, column=1, padx=10, pady=5)
    
    self.label_sup = ttk.Label(self.tab1, text="Limite superior")
    self.label_sup.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_sup = ttk.Entry(self.tab1)
    self.entry_sup.grid(row=3, column=1, padx=10, pady=5)


    self.button_generate = ttk.Button(
        self.tab1, text="Generar", command=self.generador)
    self.button_generate.grid(
        row=5, column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab1, width=400, height=600)
    self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

 


def generacion_vector(param):
    primer_vector = [0] * 11
    acu = 0
    acu_precio = 0
 
  
    for i in range(param):
        primer_vector[3] = 0
        primer_vector[4] = 0
        primer_vector[5] = 0
        primer_vector[6] = 0
        primer_vector[7] = 0
        primer_vector[8] = 0
        primer_vector[0] = i + 1
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
                
                        
                    elif primer_vector[7] < 0.50:
                        # vende 2 
                        primer_vector[8] = 2
                  
                    elif primer_vector[7] < 0.80:
                        # vende 3 
                        primer_vector[8] = 3
                   
                    else:
                        # vende 4
                        primer_vector[8] = 4
                  
                        
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
                     
                    elif primer_vector[7] < 0.90:
                        # vende 2 
                        primer_vector[8] = 2
    
                    else:
                        # vende 3 
                        primer_vector[8] = 3
                        
                
                else:
                    # no vende
                     # no vende
                    primer_vector[6] = "No vende"
                    
                    
        else:
             primer_vector[2] = "No abrio"
         
        acu += primer_vector[8]
        acu_precio = acu * 200     
        primer_vector[9] += acu
        primer_vector[10]+= acu_precio
    return primer_vector
    

def tabla(self):
    
    inf = int(self.entry_inf.get())
    sup = int(self.entry_sup.get())
    data = []

    # Agregar todos los vectores desde inf hasta sup a la lista data
    for i in range(inf, sup + 1):
        data.extend([generacion_vector(i)])
    
  

    

    table_text = tabulate(data, headers=['Numero visita', 'Random abre', 'Abre la puerta',
                                        'Random quien', 'Quien', 'Rnd atiende', 'Vende',
                                        'RND Vende', 'Cuantas vende','Acum 1', 'Acum 2'])


    root = tk.Tk()
    root.title("Tabla de Frecuencias")

    # Crear un widget Text para mostrar la tabla
    text_area = tk.Text(root, height=40, width=170)
    text_area.insert(tk.END, table_text)
    text_area.pack(expand=True, fill=tk.BOTH)

    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()
            

 
        
       
    
        


root = tk.Tk()
app = Montecarlo(root)
root.mainloop()
