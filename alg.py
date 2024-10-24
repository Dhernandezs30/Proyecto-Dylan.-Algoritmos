
import tkinter as tk
from tkinter import messagebox
import numpy as np
import ast

# Funciones matemáticas
def gauss_jordan(matrix):
    try:
        matrix = np.array(matrix, dtype=float)
        rows, cols = matrix.shape
        for i in range(min(rows, cols)):
            matrix[i] = matrix[i] / matrix[i][i]  # Dividir fila por el elemento diagonal
            for j in range(rows):
                if i != j:
                    matrix[j] = matrix[j] - matrix[i] * matrix[j][i]
        return matrix
    except Exception as e:
        return f"Error en Gauss-Jordan: {e}"

def cramer(matrix, constants):
    try:
        matrix = np.array(matrix)
        constants = np.array(constants)
        det_matrix = np.linalg.det(matrix)
        if det_matrix == 0:
            return "El sistema no tiene solución única (determinante = 0)"
        solutions = []
        for i in range(matrix.shape[1]):
            matrix_copy = matrix.copy()
            matrix_copy[:, i] = constants
            solutions.append(np.linalg.det(matrix_copy) / det_matrix)
        return solutions
    except Exception as e:
        return f"Error en Cramer: {e}"

def multiply_matrices(matrix1, matrix2):
    try:
        matrix1 = np.array(matrix1)
        matrix2 = np.array(matrix2)
        return np.dot(matrix1, matrix2)
    except ValueError as e:
        return f"Error en la multiplicación: {e}"

def inverse_matrix(matrix):
    try:
        matrix = np.array(matrix)
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "La matriz no tiene inversa (determinante = 0)"
    except Exception as e:
        return f"Error al calcular la inversa: {e}"

# Función para convertir la entrada de texto en una matriz
def parse_matrix(input_str):
    try:
        matrix = ast.literal_eval(input_str)
        if isinstance(matrix, list):
            return matrix
        else:
            raise ValueError("Entrada inválida. Usa el formato: [[1,2],[3,4]]")
    except Exception as e:
        raise ValueError(f"Entrada inválida: {e}")

def perform_operation():
    method = method_var.get()
    
    try:
        matrix = parse_matrix(matrix_entry.get())
        
        if method == 'Gauss-Jordan':
            result = gauss_jordan(matrix)
        
        elif method == 'Regla de Cramer':
            constants = parse_matrix(constants_entry.get())
            result = cramer(matrix, constants)
        
        elif method == 'Multiplicación':
            matrix2 = parse_matrix(matrix2_entry.get())
            result = multiply_matrices(matrix, matrix2)
        
        elif method == 'Inversa':
            result = inverse_matrix(matrix)
        
        show_result(result)
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Función para mostrar los resultados
def show_result(result):
    result_window = tk.Toplevel()
    result_window.title("Resultado")
    result_text = tk.Text(result_window)
    result_text.insert(tk.END, str(result))
    result_text.pack()

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Calculadora Multifuncional de Matrices")

# Entradas de matriz
tk.Label(root, text="Matriz (usa formato Python, e.g. [[1,2],[3,4]])").grid(row=0, column=0)
matrix_entry = tk.Entry(root)
matrix_entry.grid(row=0, column=1)

# Entrada para constantes (solo se usa en Cramer)
tk.Label(root, text="Constantes (para Cramer)").grid(row=1, column=0)
constants_entry = tk.Entry(root)
constants_entry.grid(row=1, column=1)

# Entrada para la segunda matriz (solo se usa en multiplicación)
tk.Label(root, text="Segunda matriz (para multiplicación)").grid(row=2, column=0)
matrix2_entry = tk.Entry(root)
matrix2_entry.grid(row=2, column=1)

# Selección de método
method_var = tk.StringVar(root)
method_var.set("Gauss-Jordan")

tk.Label(root, text="Método").grid(row=3, column=0)
method_menu = tk.OptionMenu(root, method_var, "Gauss-Jordan", "Regla de Cramer", "Multiplicación", "Inversa")
method_menu.grid(row=3, column=1)

# Botón para ejecutar la operación
execute_button = tk.Button(root, text="Calcular", command=perform_operation)
execute_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
