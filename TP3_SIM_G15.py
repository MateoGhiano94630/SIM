import random
import tkinter as tk
from tkinter import ttk, messagebox
from tabulate import tabulate


class Montecarlo:
    def __init__(self, root):
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
    
    self.label_inf = ttk.Label(self.tab1, text="Ingrese desde que visita desea visualizar (inf):")
    self.label_inf.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_inf = ttk.Entry(self.tab1)
    self.entry_inf.grid(row=2, column=1, padx=10, pady=5)
    
    self.label_sup = ttk.Label(self.tab1, text="Ingrese hasta que visita desea visualizar (sup):")
    self.label_sup.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_sup = ttk.Entry(self.tab1)
    self.entry_sup.grid(row=3, column=1, padx=10, pady=5)

    self.label_prob_v = ttk.Label(self.tab1, text="Probabilidad de realizar la venta si atiende señora:")
    self.label_prob_v.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_prob_v = ttk.Entry(self.tab1)
    self.entry_prob_v.grid(row=4, column=1, padx=10, pady=5)
    
    self.label_prob1Sra = ttk.Label(self.tab1, text="\t Probabilidad de que venda una suscripcion:")
    self.label_prob1Sra.grid(row=5, column=0, padx=10, pady=5, sticky="w")

    self.entry_prob_1Sra = ttk.Entry(self.tab1)
    self.entry_prob_1Sra.grid(row=5, column=1, padx=10, pady=5)
    
    self.label_prob2Sra = ttk.Label(self.tab1, text="\t Probabilidad de que venda dos suscripciones:") 
    self.label_prob2Sra.grid(row=7, column=0, padx=10, pady=5,sticky="w")

    self.entry_prob_2Sra = ttk.Entry(self.tab1)
    self.entry_prob_2Sra.grid(row=7, column=1, padx=10, pady=5)
    
    self.label_prob3Sra = ttk.Label(self.tab1, text="\t Probabilidad de que venda tres suscripciones:")
    self.label_prob3Sra.grid(row=8, column=0, padx=10, pady=5, sticky="w")

    self.entry_prob_3Sra = ttk.Entry(self.tab1)
    self.entry_prob_3Sra.grid(row=8, column=1, padx=10, pady=5)

    self.label_Sr = ttk.Label(self.tab1, text="Probabilidades de realizar la venta si atiende señor:")
    self.label_Sr.grid(row=9, column=0, padx=10, pady=5, sticky="w")
    
  
    self.label_prob1Sr = ttk.Label(self.tab1, text="\t Probabilidad de que venda una suscripcion:")
    self.label_prob1Sr.grid(row=10, column=0, padx=10, pady=5, sticky="w")

    self.entry_prob_1Sr = ttk.Entry(self.tab1)
    self.entry_prob_1Sr.grid(row=10, column=1, padx=10, pady=5)
    
    self.label_prob2Sr = ttk.Label(self.tab1, text="\t Probabilidad de que venda dos suscripciones:") 
    self.label_prob2Sr.grid(row=11, column=0, padx=10, pady=5,sticky="w")

    self.entry_prob_2Sr = ttk.Entry(self.tab1)
    self.entry_prob_2Sr.grid(row=11, column=1, padx=10, pady=5)
    
    self.label_prob3Sr = ttk.Label(self.tab1, text="\t Probabilidad de que venda tres suscripciones:")
    self.label_prob3Sr.grid(row=12, column=0, padx=10, pady=5, sticky="w")

    self.entry_prob_3Sr = ttk.Entry(self.tab1)
    self.entry_prob_3Sr.grid(row=12, column=1, padx=10, pady=5)

    self.label_prob4Sr = ttk.Label(self.tab1, text="\t Probabilidad de que venda cuatro suscripciones:")
    self.label_prob4Sr.grid(row=13, column=0, padx=10, pady=5, sticky="w")

    self.entry_prob_4Sr = ttk.Entry(self.tab1)
    self.entry_prob_4Sr.grid(row=13, column=1, padx=10, pady=5)

    self.label_prob_genero = ttk.Label(self.tab1, text="Probabilidad de que un hombre abra la puerta:")
    self.label_prob_genero.grid(row=14, column=0, padx=10, pady=5, sticky="w")

    self.entry_prob_genero = ttk.Entry(self.tab1)
    self.entry_prob_genero.grid(row=14, column=1, padx=10, pady=5)

    self.label_utilidad = ttk.Label(self.tab1, text="Valor de la utilidad:")
    self.label_utilidad.grid(row=15, column=0, padx=10, pady=5, sticky="w")

    self.entry_utilidad  = ttk.Entry(self.tab1)
    self.entry_utilidad.grid(row=15, column=1, padx=10, pady=5)

    self.button_generate = ttk.Button(
        self.tab1, text="Generar", command=self.generador)
    self.button_generate.grid(
        row=17 , column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab1, width=400, height=600)
    self.canvas.grid(row=20, column=0, columnspan=2, padx=10, pady=10)

 
def generacion_vector(self,i, acu1, acu2):
    primer_vector = [0] * 11
    primer_vector[0] = i + 1
    primer_vector[1] = round(random.random(),4)
   
                 
    if primer_vector[1] > 0.29:
        primer_vector[2] = "Sí abrió"
        primer_vector[3] = round(random.random(),4)
        if primer_vector[3] < float(self.entry_prob_genero.get()):
            # abre señor
            primer_vector[4] = "Señor"
            primer_vector[5] = round(random.random(),4)
            if primer_vector[5] < 0.25:
                primer_vector[6] = "Sí vende"
                primer_vector[7] = round(random.random(),4)
                if primer_vector[7] < float(self.entry_prob_1Sr.get()):
                    # vende 1 
                    primer_vector[8] = 1
            
                    
                elif primer_vector[7] < float(self.entry_prob_2Sr.get()):
                    # vende 2 
                    primer_vector[8] = 2
                
                elif primer_vector[7] < float(self.entry_prob_3Sr.get()):
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
            primer_vector[5] = round(random.random(),4)
            if primer_vector[5] < float(self.entry_prob_v.get()):
                primer_vector[6] = "Sí vende"
                primer_vector[7] = round(random.random(),4)
                if primer_vector[7] < float(self.entry_prob_1Sra.get()):
                    # vende 1 
                    primer_vector[8] = 1
                    
                elif primer_vector[7] < float(self.entry_prob_2Sra.get()):
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
            primer_vector[2] = "No abrió"
        
    cant_ventas = primer_vector[8]
    monto_ventas = cant_ventas * float(self.entry_utilidad.get())    
    primer_vector[9] = cant_ventas + acu1
    primer_vector[10] = monto_ventas + acu2
    return primer_vector
    

def tabla(self):
    validacion_1(float(self.entry_prob_1Sr.get()),float(self.entry_prob_2Sr.get()), float(self.entry_prob_3Sr.get()), float(self.entry_prob_4Sr.get()))
    validacion_2(float(self.entry_prob_1Sra.get()),float(self.entry_prob_2Sra.get()), float(self.entry_prob_3Sra.get()))
    validacion_3(float(self.entry_prob_genero.get()))
    validacion_3(float(self.entry_prob_v.get()))
    validacion_4(float(self.entry_utilidad.get()))
    inf = int(self.entry_inf.get())
    sup = int(self.entry_sup.get())
    validar_lim(inf, sup)
    N = controlar_N(int(self.entry_N.get()))
    data = []
    acu1, acu2, contador1 = 0, 0, 0

    for i in range(N):
        vector = generacion_vector(self,i,acu1,acu2)
        acu1 = vector[9]
        acu2 = vector[10]
        if vector[8] >= 2:
            contador1 += 1
        if (i +1) >= inf and (i+1) <= sup:
            data.extend([vector])
        if i == (N - 1):
            data.extend([["","","","","","","","","Total:",acu1,acu2]])
            data.extend([["","","","","","","","","Probabilidad de vender dos o mas suscripciones:",(contador1/N) * 100,"%"]])

  

    table_text = tabulate(data, headers=['Número de visita', 'RND Abre', 'Abre la puerta?',
                                        'RND género', 'Quién?', 'RND Vende', 'Vende?',
                                        'RND cúantas', 'Cuántas vende?','Acumulador vendidas', 'Acumulador monto por vendidas'])

    root = tk.Tk()
    root.title("Tabla de visitas")
    
    text_area = tk.Text(root, height=40, width=170)
    text_area.insert(tk.END, table_text)
    text_area.pack(expand=True, fill=tk.BOTH)
    
    root.mainloop()

            

def controlar_N(n):           

    try:
        if n > 100000:
            messagebox.showerror(
                "Error", "La cantidad de visitas (n) no puede ser mayor a 100,000.")
            return
        elif n < 1:
            messagebox.showerror(
                "Error", "La cantidad de visitas (n) debe ser mayor a 1.")
            return
                        
    except ValueError:
            messagebox.showerror(
                "Error", "El valor de la cantidad de visitas (n) debe ser un numero.")
            return
    return n

def validacion_1(prob1, prob2, prob3, prob4):
    sum = prob1 + prob2 + prob3 + prob4
    try:
        if sum != 1:
            messagebox.showerror(
                "Error", "La suma de las probabilidades debe ser 1.")
            return
        if  1 < prob1 < 0 or 1 < prob2 < 0 or 1 < prob3 < 0 or 1 < prob4 < 0:
            messagebox.showerror(
                    "Error", "Las probabilidades deben ser un numero entre 0 y 1.")
            return
        
       
                        
    except ValueError:
            messagebox.showerror(
                "Error", "Las probabilidades deben ser un numero entre 0 y 1.")
            return
     

def validacion_2(prob1, prob2, prob3):
    sum = prob1 + prob2 + prob3 
    try:
        if sum != 1:
            messagebox.showerror(
                "Error", "La suma de las probabilidades debe ser 1.")
            return
        if   prob1 < 0 or prob1 > 1 or  prob2 > 1 or prob2 < 0 or  prob3 > 1 or prob3 < 0:
            messagebox.showerror(
                    "Error", "Las probabilidades deben ser un numero entre 0 y 1.")
            return
 
                     
    except ValueError:
            messagebox.showerror(
                "Error", "Las probabilidades deben ser un numero entre 0 y 1.")
            return
     

def validacion_3(prob1):
    try:    
        if prob1 > 1 or prob1 < 0:
            messagebox.showerror(
                            "Error", "Las probabilidades deben ser un numero entre 0 y 1.")
            return
    except ValueError:
            messagebox.showerror(
                "Error", "Las probabilidades deben ser un numero entre 0 y 1.")
            return

def validacion_4(valor):
        try:
            if valor < 0:
                messagebox.showerror(
                                "Error", "El valor de cada suscripcion debe ser mayor a cero.")
                return
                        
        except ValueError:
                messagebox.showerror(
                    "Error", "Debe ingresar un numero.")
                return
     

def validar_lim(inf, sup):
    try:
        if inf < 0 or sup < 0:
            messagebox.showerror(
                            "Error", "El numero ingresado debe ser mayor a cero.")
            return
        if sup < inf:
            messagebox.showerror(
                            "Error", "El limite superior debe ser mayor al limite inferior.")
            return
        
           
    except ValueError:
            messagebox.showerror(
                "Error", "Debe ingresar un numero.")
            return


root = tk.Tk()
app = Montecarlo(root)
root.mainloop()
