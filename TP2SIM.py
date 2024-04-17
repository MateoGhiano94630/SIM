import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import chi2, expon, norm
from collections import Counter
import math




class GeneradorDeRandoms:
    def __init__(self, root):
        
        # PESTAÑA 1
        interfaz_uniforme(self, root)
        
        # PESTAÑA 2
        interfaz_exponencial(self, root)

        # PESTAÑA 3
        interfaz_normal(self, root)

        # PESTAÑA 4
        interfaz_poisson(self, root)

    def generate_random_numbers(self):
        self.text_output.delete(1.0, tk.END)  # Limpiar el widget de texto
        current_tab = self.notebook.index("current")

        
        # Uniforme
        if current_tab == 0:
            uniforme(self)

        # Exponencial
        elif current_tab == 1:
            exponencial(self)
       
        # Normal
        elif current_tab == 2:
            normal(self)

        # Poisson
        elif current_tab == 3:
            pass

def uniforme(self):

            N = controlar_N(int(self.entry_N.get()))
            # Validacion que el valor de a sea menor que el valor de b y que ambos sean numeros
            try:
                A = float(self.entry_A.get())
                B = float(self.entry_B.get())
                if A >= B:
                    messagebox.showerror(
                        "Error", "El valor de A debe ser menor que B.")
                    return
            except ValueError:
                messagebox.showerror(
                    "Error", "Los valores de A y B deben ser números.")
                return

            # Genera una cantidad N de numeros randoms en el intervalo entre A y B
            random_numbers = np.random.uniform(A, B, N)

            # Mostrar la nueva serie de números aleatorios en el widget de texto
            self.text_output.insert(
                tk.END, "Nueva serie de números aleatorios uniformemente distribuidos:\n")
            for num in random_numbers:
                self.text_output.insert(tk.END, f"{num:.4f}\t")

            num_intervals = int(self.entry_intervals.get())
        
            min_num = np.min(random_numbers)
            max_num = np.max(random_numbers)
            rango = max_num - min_num
            amplitud = rango / num_intervals
            
            # primera vuelta i vale 0 entonces el inferior es el  minimo
            # luego se multiplica i por la amplitud y se le suma al minimo numero
            limites_inferiores = [min_num + i * amplitud for i in range(num_intervals)]
            
            # a cada limite inferior se le suma la amplitud
            limites_superiores = [
                lim_inf + amplitud for lim_inf in limites_inferiores]

            
            # Calcular frecuencias observadas
            # se utiliza np.histogram para calcular las FO
            # random numbers es la serie de randoms a la cual queremos obtener las FO
            # bins es la cantidad de separaciones o intervalos 
            # la funcion retorna dos valores uno es un array con las FO y el otro es ignorable
            freq_observadas, _ = np.histogram(
                random_numbers, bins=num_intervals)


            # Calcular frecuencia esperada
            # Dado que es uniforme todas las frecuencias esperadas son iguales
            # asi que dividioms la cantidad de randoms por el numero de intervalos
            freq_esperada = N / num_intervals

            

            # Calcular estadístico de Ji cuadrado
            #(O-E)^2/E
            # la funcion sum de la libreria numpy va sumando los resultados de
            # realizar la formula ingresada posteriormente en cada uno de los valores
            # de los array de la frecuencia observada y esperada
            ji_cuadrado_calculado = np.sum(
                (freq_observadas - freq_esperada) ** 2 / freq_esperada)

            # Obtener el valor crítico de la tabla de Ji cuadrado
            # los grados de libertad son el numero de intervalos menos 1
            grados_libertad = num_intervals - 1
            # la funcion chi2 es de la liberira scipy y devuelve el chi calculado con un 
            # nivel de aceptacion del 95% y un nivel de rechazo 5%
            ji_cuadrado_tabla = chi2.ppf(0.95, grados_libertad)

            # Verificar si se pasó la prueba de Ji cuadrado
            if ji_cuadrado_calculado <= ji_cuadrado_tabla:
                resultado_prueba = "Se pasó de forma exitosa la prueba del Ji cuadrado. Se acepta la H0"
            else:
                resultado_prueba = "No se pasó la prueba del Ji cuadrado. Se rechaza la H0"

            
            # Mostrar histograma con frecuencias observadas
            plt.figure()
            plt.hist(random_numbers, bins=num_intervals, edgecolor='black')
            for lim_inf, lim_sup, freq_obs in zip(limites_inferiores, limites_superiores, freq_observadas):
                plt.text((lim_inf + lim_sup) / 2, freq_obs,
                         str(freq_obs), ha='center', va='bottom')
            plt.xlabel('Valor')
            plt.ylabel('Frecuencia')
            plt.title('Histograma de Frecuencias')
            plt.grid(True)
            plt.show()
             # Mostrar resultados en el widget de texto
            messagebox.showinfo(title="Resultados del test de Ji cuadrado", message=f"Grados de libertad: {grados_libertad}\n Ji cuadrado calculado: {ji_cuadrado_calculado:.4f}\n  Ji cuadrado de tabla: {ji_cuadrado_tabla:.4f}\n {resultado_prueba}")

            # Mostrar Tabla de frecuencias
            plt.figure(figsize=(8, 4))
            columns = ('Intervalo', 'Frecuencia Observada', 'Frecuencia Esperada')
            rows = [f'{lim_inf:.2f} - {lim_sup:.2f}' for lim_inf, lim_sup in zip(limites_inferiores, limites_superiores)]
            cell_text = [[intervalo, str(freq), round(freq_esperada,4)] for intervalo, freq in zip(rows, freq_observadas)]

            plt.table(cellText=cell_text, colLabels=columns, loc='center')
            plt.axis('off')  # Ocultar ejes para que se vea solo la tabla

            plt.title('Tabla de Frecuencias')
            plt.show()
        
def exponencial(self):
            N = controlar_N(int(self.entry_N2.get()))
            
            random_numbers = np.random.exponential(scale=1/int(self.entry_L.get()), size=int(self.entry_N2.get()))
            
            num_intervals = int(self.entry_intervals2.get())  
            
            # Calcular límites de intervalos
            min_num = np.min(random_numbers)
            max_num = np.max(random_numbers)
            rango = max_num - min_num
            amplitud = rango / num_intervals
            limites_inferiores = [min_num + i *
                                  amplitud for i in range(num_intervals)]
            limites_superiores = [
                lim_inf + amplitud for lim_inf in limites_inferiores]
            

            def densidad_probabilidad_ls(LS, lambd):
                return 1 - np.exp(-lambd * LS)

            def densidad_probabilidad_li(Li, lambd):
                return 1 - np.exp(-lambd * Li)
            
            # Calcular frecuencia esperada BIEN
            freq_esperada = [(densidad_probabilidad_ls(limites_superiores[i], int(self.entry_L.get())) - densidad_probabilidad_li((limites_inferiores[i]),int(self.entry_L.get()))) * int(self.entry_N2.get()) for i in range(num_intervals)]
         
            i = 0
            while i < len(freq_esperada):
                while freq_esperada[i] < 5:
                    if i == len(freq_esperada) - 1:
                        freq_esperada[i-1] += freq_esperada[i]
                        freq_esperada.pop(i)
                        break
                    elif i+1 < len(freq_esperada):
                        freq_esperada[i] += freq_esperada[i+1]
                        freq_esperada.pop(i+1)
                i += 1

            num_intervals = len(freq_esperada)
            # Calcular frecuencias observadas IGUAL QUE EN UNIFORME
            freq_observadas, _ = np.histogram(
                random_numbers, bins=num_intervals)
            # Calcular estadístico de Ji cuadrado BIEN
            ji_cuadrado_calculado = np.sum(
                (freq_observadas - freq_esperada) ** 2 / freq_esperada)
    
            # Obtener el valor crítico de la tabla de Ji cuadrado
            grados_libertad = num_intervals - 1
            ji_cuadrado_tabla = chi2.ppf(0.95, grados_libertad)

            # Verificar si se pasó la prueba de Ji cuadrado
            if ji_cuadrado_calculado <= ji_cuadrado_tabla:
                resultado_prueba = "Se pasó de forma exitosa la prueba del Ji cuadrado. Se acepta la H0"
            else:
                resultado_prueba = "No se pasó la prueba del Ji cuadrado. Se rechaza la H0"
            
            # Mostrar histograma con frecuencias observadas
            plt.figure()
            plt.hist(random_numbers, bins=num_intervals, edgecolor='black')
            for lim_inf, lim_sup, freq_obs in zip(limites_inferiores, limites_superiores, freq_observadas):
                plt.text((lim_inf + lim_sup) / 2, freq_obs,
                         str(freq_obs), ha='center', va='bottom')
            plt.xlabel('Valor')
            plt.ylabel('Frecuencia')
            plt.title('Histograma de Frecuencias')
            plt.grid(True)
            plt.show()

              # Mostrar resultados en el widget de texto
            messagebox.showinfo(title="Resultados del test de Ji cuadrado", message=f"Grados de libertad: {grados_libertad}\n Ji cuadrado calculado: {ji_cuadrado_calculado:.4f}\n  Ji cuadrado de tabla: {ji_cuadrado_tabla:.4f}\n {resultado_prueba}")

            # Mostrar Tabla de frecuencias
            plt.figure(figsize=(8, 4))
            columns = ('Intervalo', 'Frecuencia Observada', 'Frecuencia Esperada')
            rows = [f'{lim_inf:.2f} - {lim_sup:.2f}' for lim_inf, lim_sup in zip(limites_inferiores, limites_superiores)]
            cell_text = [[intervalo, str(freq), round(freq_esp,4)] for intervalo, freq, freq_esp in zip(rows, freq_observadas, freq_esperada)]

            plt.table(cellText=cell_text, colLabels=columns, loc='center')
            plt.axis('off')  # Ocultar ejes para que se vea solo la tabla

            plt.title('Tabla de Frecuencias')
            plt.show()

def normal(self):
            N = controlar_N(int(self.entry_N3.get()))
            MED = float(self.entry_M.get())
            DS = float(self.entry_DS.get())
            num_intervals = int(self.entry_intervals3.get())
              
            NT = [0]

            N1 = np.random.normal(MED,DS,(N//2))
            N2 = np.random.normal(MED,DS,(N//2))

            NT.extend(N1)
            NT.extend(N2)

            min_num = np.min(NT)
            max_num = np.max(NT)

            rango = max_num - min_num
            amplitud = rango / num_intervals
            limites_inferiores = [min_num + i * amplitud for i in range(num_intervals)]
            limites_superiores = [
                lim_inf + amplitud for lim_inf in limites_inferiores]
            
            # Calcular frecuencias observadas
            freq_observadas, _ = np.histogram(
                NT, bins=num_intervals)
            
            def densidad_probabilidad_li(limites_inferiores,MED,DS):
               return  norm.cdf(limites_inferiores,MED,DS)
            def densidad_probabilidad_ls(limites_superiores,MED,DS):
               return  norm.cdf(limites_superiores,MED,DS)

            # Calcular frecuencia esperada 
            freq_esperada = [((densidad_probabilidad_ls(ls, MED, DS) - densidad_probabilidad_li(li, MED, DS)) * len(NT)) for li, ls in zip(limites_inferiores, limites_superiores)]
            i = 0
            while i < len(freq_esperada):
                while freq_esperada[i] < 5:
                    if i == len(freq_esperada) - 1:
                        freq_esperada[i-1] += freq_esperada[i]
                        freq_esperada.pop(i)
                        break
                    elif i+1 < len(freq_esperada):
                        freq_esperada[i] += freq_esperada[i+1]
                        freq_esperada.pop(i+1)
                i += 1
            num_intervals = len(freq_esperada) 
             
            # Calcular frecuencias observadas IGUAL QUE EN UNIFORME
            freq_observadas, _ = np.histogram(
                NT, bins=num_intervals)
            # Calcular estadístico de Ji cuadrado BIEN
            ji_cuadrado_calculado = np.sum(
                (freq_observadas - freq_esperada) ** 2 / freq_esperada)
    
            # Obtener el valor crítico de la tabla de Ji cuadrado
            grados_libertad = num_intervals - 1
            ji_cuadrado_tabla = chi2.ppf(0.95, grados_libertad)

            # Verificar si se pasó la prueba de Ji cuadrado
            if ji_cuadrado_calculado <= ji_cuadrado_tabla:
                resultado_prueba = "Se pasó de forma exitosa la prueba del Ji cuadrado."
            else:
                resultado_prueba = "No se pasó la prueba del Ji cuadrado."
            # Mostrar histograma con frecuencias observadas
            plt.figure()
            plt.hist(NT, bins=num_intervals, edgecolor='black')
            for lim_inf, lim_sup, freq_obs in zip(limites_inferiores, limites_superiores, freq_observadas):
                plt.text((lim_inf + lim_sup) / 2, freq_obs,
                         str(freq_obs), ha='center', va='bottom')
            plt.xlabel('Valor')
            plt.ylabel('Frecuencia')
            plt.title('Histograma de Frecuencias')
            plt.grid(True)
            plt.show()
               # Mostrar resultados en el widget de texto
            messagebox.showinfo(title="Resultados del test de Ji cuadrado", message=f"Grados de libertad: {grados_libertad}\n Ji cuadrado calculado: {ji_cuadrado_calculado:.4f}\n  Ji cuadrado de tabla: {ji_cuadrado_tabla:.4f}\n {resultado_prueba}")

            # Mostrar Tabla de frecuencias
            plt.figure(figsize=(8, 4))
            columns = ('Intervalo', 'Frecuencia Observada', 'Frecuencia Esperada')
            rows = [f'{lim_inf:.2f} - {lim_sup:.2f}' for lim_inf, lim_sup in zip(limites_inferiores, limites_superiores)]
            cell_text = [[intervalo, str(freq), round(freq_esp,4)] for intervalo, freq, freq_esp in zip(rows, freq_observadas, freq_esperada)]

            plt.table(cellText=cell_text, colLabels=columns, loc='center')
            plt.axis('off')  # Ocultar ejes para que se vea solo la tabla

            plt.title('Tabla de Frecuencias')
            plt.show()
            

def interfaz_uniforme(self, root):
    self.root = root
    self.root.title("Generador de Números Aleatorios")

    self.notebook = ttk.Notebook(root)
    self.notebook.pack(fill=tk.BOTH, expand=True)

    self.tab1 = ttk.Frame(self.notebook)
    self.notebook.add(self.tab1, text="Uniforme")

    self.label_N = ttk.Label(self.tab1, text="Cantidad de muestras (N):")
    self.label_N.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_N = ttk.Entry(self.tab1)
    self.entry_N.grid(row=1, column=1, padx=10, pady=5)

    self.label_A = ttk.Label(self.tab1, text="Valor de A:")
    self.label_A.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    self.entry_A = ttk.Entry(self.tab1)
    self.entry_A.grid(row=2, column=1, padx=10, pady=5)

    self.label_B = ttk.Label(self.tab1, text="Valor de B:")
    self.label_B.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    self.entry_B = ttk.Entry(self.tab1)
    self.entry_B.grid(row=3, column=1, padx=10, pady=5)

    self.label_intervals = ttk.Label(
        self.tab1, text="Número de intervalos:")
    self.label_intervals.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    
    self.entry_intervals = ttk.Combobox(self.tab1,
                                        state="redondly",
                                        values=[10,15,20,25])
    self.entry_intervals.grid(row=4, column=1, padx=10, pady=5)

    self.button_generate = ttk.Button(
        self.tab1, text="Generar", command=self.generate_random_numbers)
    self.button_generate.grid(
        row=5, column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab1, width=400, height=600)
    self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # arreglar ancho y alto
    self.text_output = tk.Text(self.tab1, width=70, height=30)
    self.text_output.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

def interfaz_exponencial(self, root):
    self.tab2 = ttk.Frame(self.notebook)
    self.notebook.add(self.tab2, text="Exponencial")

    self.label_N2 = ttk.Label(self.tab2, text="Cantidad de muestras (N):")
    self.label_N2.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_N2 = ttk.Entry(self.tab2)
    self.entry_N2.grid(row=0, column=1, padx=10, pady=5)

    self.label_L = ttk.Label(self.tab2, text="Lambda:")
    self.label_L.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    self.entry_L = ttk.Entry(self.tab2)
    self.entry_L.grid(row=1, column=1, padx=10, pady=5)

    self.label_intervalos2 = ttk.Label(self.tab2, text="Numero de intervalos")
    self.label_intervalos2.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    self.entry_intervals2 =  ttk.Combobox(self.tab2,
                                        state="redondly",
                                        values=[10,15,20,25])
    self.entry_intervals2.grid(row=2, column=1, padx=10, pady=5)

    self.button_generate = ttk.Button(
        self.tab2, text="Generar", command=self.generate_random_numbers)
    self.button_generate.grid(
        row=5, column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab2, width=400, height=600)
    self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    self.text_output2 = tk.Text(self.tab2, width=70, height=30)
    self.text_output2.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

def interfaz_normal(self, root):
    self.tab3 = ttk.Frame(self.notebook)
    self.notebook.add(self.tab3, text="Normal")

    self.label_N3 = ttk.Label(self.tab3, text="Cantidad de muestras (N):")
    self.label_N3.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    self.entry_N3 = ttk.Entry(self.tab3)
    self.entry_N3.grid(row=0, column=1, padx=10, pady=5)
    
    self.label_intervalos3 = ttk.Label(self.tab3, text="Numero de intervalos")
    self.label_intervalos3.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    self.entry_intervals3 =  ttk.Combobox(self.tab3,
                                        state="redondly",
                                        values=[10,15,20,25])
    self.entry_intervals3.grid(row=3, column=1, padx=10, pady=5)


    self.label_M = ttk.Label(self.tab3, text="Ingrese la media:")
    self.label_M.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    self.entry_M = ttk.Entry(self.tab3)
    self.entry_M.grid(row=1, column=1, padx=10, pady=5)

    self.label_DS = ttk.Label(self.tab3, text="Ingrese la desviacion estandar:")
    self.label_DS.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    self.entry_DS = ttk.Entry(self.tab3)
    self.entry_DS.grid(row=2, column=1, padx=10, pady=5)


    self.button_generate = ttk.Button(
        self.tab3, text="Generar", command=self.generate_random_numbers)
    self.button_generate.grid(
         row=5, column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab3, width=400, height=600)
    self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    self.text_output3 = tk.Text(self.tab3, width=70, height=30)
    self.text_output3.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

def interfaz_poisson(self, root):
    self.tab4 = ttk.Frame(self.notebook)
    self.notebook.add(self.tab4, text="Poisson")

    self.label_N4 = ttk.Label(self.tab4, text="Cantidad de muestras (N):")
    self.label_N4.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    self.entry_N4 = ttk.Entry(self.tab4)
    self.entry_N4.grid(row=0, column=1, padx=10, pady=5)

    self.button_generate = ttk.Button(
        self.tab4, text="Generar", command=self.generate_random_numbers)
    self.button_generate.grid(
        row=5, column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab4, width=600, height=400)
    self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    self.text_output4 = tk.Text(self.tab4, width=50, height=10)
    self.text_output4.grid(row=7, column=0, columnspan=2, padx=10, pady=10)



def controlar_N(NI):           
    # Validacion de que la cantidad de muestras sea menor a un millon y que sea un numero
    try:
        N = int(NI)
        if N > 1000000:
            messagebox.showerror(
                "Error", "La cantidad de muestras (N) no puede ser mayor a 1,000,000.")
            return
                        
    except ValueError:
            messagebox.showerror(
                "Error", "El valor de la cantidad de muestras (N) debe ser un numero.")
            return
    return N


root = tk.Tk()
app = GeneradorDeRandoms(root)
root.mainloop()
