import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import chi2
from collections import Counter


class GeneradorDeRandoms:
    def __init__(self, root):
        # PESTAÑA 1
        self.root = root
        self.root.title("Generador de Números Aleatorios")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Normal")

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

        self.entry_intervals = ttk.Entry(self.tab1)
        self.entry_intervals.grid(row=4, column=1, padx=10, pady=5)

        self.button_generate = ttk.Button(
            self.tab1, text="Generar", command=self.generate_random_numbers)
        self.button_generate.grid(
            row=5, column=0, columnspan=2, padx=10, pady=10)

        self.canvas = tk.Canvas(self.tab1, width=600, height=400)
        self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.text_output = tk.Text(self.tab1, width=50, height=10)
        self.text_output.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # PESTAÑA 2
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Exponencial")

        self.label_N = ttk.Label(self.tab2, text="Cantidad de muestras (N):")
        self.label_N.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_N = ttk.Entry(self.tab2)
        self.entry_N.grid(row=0, column=1, padx=10, pady=5)

        self.label_L = ttk.Label(self.tab2, text="Lambda:")
        self.label_L.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry_L = ttk.Entry(self.tab2)
        self.entry_L.grid(row=1, column=1, padx=10, pady=5)

        self.button_generate = ttk.Button(
            self.tab2, text="Generar", command=self.generate_random_numbers)
        self.button_generate.grid(
            row=5, column=0, columnspan=2, padx=10, pady=10)

        self.canvas = tk.Canvas(self.tab2, width=600, height=400)
        self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.text_output = tk.Text(self.tab2, width=50, height=10)
        self.text_output.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # PESTAÑA 3
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Normal")

        self.label_N = ttk.Label(self.tab3, text="Cantidad de muestras (N):")
        self.label_N.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_N = ttk.Entry(self.tab3)
        self.entry_N.grid(row=0, column=1, padx=10, pady=5)

        self.button_generate = ttk.Button(
            self.tab3, text="Generar", command=self.generate_random_numbers)
        self.button_generate.grid(
            row=5, column=0, columnspan=2, padx=10, pady=10)

        self.canvas = tk.Canvas(self.tab3, width=600, height=400)
        self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.text_output = tk.Text(self.tab3, width=50, height=10)
        self.text_output.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # PESTAÑA 4
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Poisson")

        self.label_N = ttk.Label(self.tab4, text="Cantidad de muestras (N):")
        self.label_N.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_N = ttk.Entry(self.tab4)
        self.entry_N.grid(row=0, column=1, padx=10, pady=5)

        self.button_generate = ttk.Button(
            self.tab4, text="Generar", command=self.generate_random_numbers)
        self.button_generate.grid(
            row=5, column=0, columnspan=2, padx=10, pady=10)

        self.canvas = tk.Canvas(self.tab4, width=600, height=400)
        self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.text_output = tk.Text(self.tab4, width=50, height=10)
        self.text_output.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def generate_random_numbers(self):
        self.text_output.delete(1.0, tk.END)  # Limpiar el widget de texto
        current_tab = self.notebook.index("current")
        print("El usuario está en la pestaña:", current_tab)



        N = int(self.entry_N.get())
        if N > 1000000:
            messagebox.showerror(
                "Error", "La cantidad de muestras (N) no puede ser mayor a 1,000,000.")
            return

        if current_tab == 0:
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

            random_numbers = np.random.uniform(A, B, N)

            # Mostrar la nueva serie de números aleatorios en el widget de texto
            self.text_output.insert(
                tk.END, "Nueva serie de números aleatorios uniformemente distribuidos:\n")
            for num in random_numbers:
                self.text_output.insert(tk.END, f"{num:.4f}\n")

            try:
                num_intervals = int(self.entry_intervals.get())
                if num_intervals not in [10, 15, 20, 25]:
                    messagebox.showerror(
                        "Error", "El número de intervalos debe ser 10, 15, 20 o 25.")
                    return
            except ValueError:
                messagebox.showerror(
                    "Error", "El número de intervalos debe ser un número entero.")
                return

            # Calcular límites de intervalos
            min_num = np.min(random_numbers)
            max_num = np.max(random_numbers)
            rango = max_num - min_num
            amplitud = rango / num_intervals
            limites_inferiores = [min_num + i *
                                  amplitud for i in range(num_intervals)]
            limites_superiores = [
                lim_inf + amplitud for lim_inf in limites_inferiores]

            # Calcular frecuencias observadas
            freq_observadas, _ = np.histogram(
                random_numbers, bins=num_intervals)

            # Calcular frecuencia esperada
            freq_esperada = N / num_intervals

            # Calcular estadístico de Ji cuadrado
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
            self.text_output.insert(
                tk.END, "Resultados del test de Ji cuadrado:\n")
            self.text_output.insert(
                tk.END, f"Grados de libertad: {grados_libertad}\n")
            self.text_output.insert(
                tk.END, f"Ji cuadrado calculado: {ji_cuadrado_calculado:.4f}\n")
            self.text_output.insert(
                tk.END, f"Ji cuadrado de tabla: {ji_cuadrado_tabla:.4f}\n")
            self.text_output.insert(tk.END, resultado_prueba)
        elif current_tab == 1:
            if self.entry_L.get() is ValueError:
                messagebox.showerror(
                    "Error", "Lambda debe ser entero.")
            
            random_numbers = np.random.exponential(scale=1/int(self.entry_L.get()), size=int(self.entry_N.get()))

            try:
                num_intervals = int(self.entry_intervals.get())
                if num_intervals not in [10, 15, 20, 25]:
                    messagebox.showerror(
                        "Error", "El número de intervalos debe ser 10, 15, 20 o 25.")
                    return
            except ValueError:
                messagebox.showerror(
                    "Error", "El número de intervalos debe ser un número entero.")
                return

            # Calcular límites de intervalos
            min_num = np.min(random_numbers)
            max_num = np.max(random_numbers)
            rango = max_num - min_num
            amplitud = rango / num_intervals
            limites_inferiores = [min_num + i *
                                  amplitud for i in range(num_intervals)]
            limites_superiores = [
                lim_inf + amplitud for lim_inf in limites_inferiores]
            media = np.half(random_numbers) #REVISAR

            # Calcular frecuencias observadas
            freq_observadas, _ = np.histogram(
                random_numbers, bins=num_intervals)

            # Calcular frecuencia esperada
            freq_esperada = N / num_intervals

            # Calcular estadístico de Ji cuadrado
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
            self.text_output.insert(
                tk.END, "Resultados del test de Ji cuadrado:\n")
            self.text_output.insert(
                tk.END, f"Grados de libertad: {grados_libertad}\n")
            self.text_output.insert(
                tk.END, f"Ji cuadrado calculado: {ji_cuadrado_calculado:.4f}\n")
            self.text_output.insert(
                tk.END, f"Ji cuadrado de tabla: {ji_cuadrado_tabla:.4f}\n")
            self.text_output.insert(tk.END, resultado_prueba)

        elif current_tab == 2:
            pass
        elif current_tab == 3:
            pass

root = tk.Tk()
app = GeneradorDeRandoms(root)
root.mainloop()