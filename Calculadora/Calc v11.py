import tkinter as tk
from tkinter import END
import re

root = tk.Tk()
root.title("Calculadora Científica")
root.configure(bg='#D2B48C')  # Fondo café claro

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
    entry.icursor(len(expression))  # Mueve el cursor al final

def equalpress():
    global expression
    try:
        # Insertar '*' donde sea necesario
        expression_with_multiplication = re.sub(r'(\d)(\()', r'\1*\2', expression)
        expression_with_multiplication = re.sub(r'(\))(\d)', r'\1*\2', expression_with_multiplication)
        result = eval(expression_with_multiplication)
        equation.set(str(result))
        expression = str(result)
    except ZeroDivisionError:
        equation.set("Error")
        expression = ""
    except ValueError:
        equation.set("Error")
        expression = ""
    except SyntaxError:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Función para calcular la exponencial (e^x) manualmente
def exp():
    global expression
    try:
        number = float(expression)
        result = sum((number**n) / factorial(n) for n in range(20))
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

# Función para calcular la potencia (x^y) manualmente
def power():
    global expression
    try:
        if '**' in expression:
            base, exponent = map(float, expression.split('**'))
            result = base ** exponent
            equation.set(str(result))
            expression = str(result)
        else:
            expression += '**'
            equation.set(expression)
    except ValueError:
        equation.set("Error")
        expression = ""

# Funciones científicas manuales
def sin():
    global expression
    try:
        angle = float(expression)
        angle = angle * (3.141592653589793 / 180)  # Convertir grados a radianes
        result = sum((-1)**n * (angle**(2*n+1)) / factorial(2*n+1) for n in range(10))
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def cos():
    global expression
    try:
        angle = float(expression)
        angle = angle * (3.141592653589793 / 180)  # Convertir grados a radianes
        result = sum((-1)**n * (angle**(2*n)) / factorial(2*n) for n in range(10))
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def tan():
    global expression
    try:
        angle = float(expression)
        angle = angle * (3.141592653589793 / 180)  # Convertir grados a radianes
        sin_result = sum((-1)**n * (angle**(2*n+1)) / factorial(2*n+1) for n in range(10))
        cos_result = sum((-1)**n * (angle**(2*n)) / factorial(2*n) for n in range(10))
        result = sin_result / cos_result
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def log():
    global expression
    try:
        number = float(expression)
        result = sum(((-1)**(n+1)) * ((number-1)**n) / n for n in range(1, 20))
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def ln():
    global expression
    try:
        number = float(expression)
        result = sum(((-1)**(n+1)) * ((number-1)**n) / n for n in range(1, 20))
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def sqrt():
    global expression
    try:
        number = float(expression)
        result = number ** 0.5
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def add_fraction(num1, den1, num2, den2):
    num = num1 * den2 + num2 * den1
    den = den1 * den2
    common_divisor = gcd(num, den)
    return num // common_divisor, den // common_divisor

def subtract_fraction(num1, den1, num2, den2):
    num = num1 * den2 - num2 * den1
    den = den1 * den2
    common_divisor = gcd(num, den)
    return num // common_divisor, den // common_divisor

def multiply_fraction(num1, den1, num2, den2):
    num = num1 * num2
    den = den1 * den2
    common_divisor = gcd(num, den)
    return num // common_divisor, den // common_divisor

def divide_fraction(num1, den1, num2, den2):
    num = num1 * den2
    den = den1 * num2
    common_divisor = gcd(num, den)
    return num // common_divisor, den // common_divisor

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right', bg='black', fg='#39FF14')  # Verde neón
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

button_style = {
    'padx': 20,
    'pady': 20,
    'bd': 5,
    'relief': 'raised',
    'font': ('arial', 12, 'bold'),
    'highlightbackground': 'black',
    'highlightthickness': 2
}

basic_ops_style = {
    'bg': '#ADD8E6',  # Azul claro
    'fg': 'black'
}

scientific_ops_style = {
    'bg': '#90EE90',  # Verde claro
    'fg': 'black'
}

special_buttons_style = {
    'bg': '#FF6347',  # Rojo tomate
    'fg': 'white'
}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2, equalpress), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('^', 5, 2, power), ('C', 5, 3, clear)
]

for (text, row, col, *cmd) in buttons:
    action = cmd[0] if cmd else lambda t=text: press(t)
    style = button_style.copy()
    if text in '0123456789':
        style.update({'bg': '#D3D3D3', 'fg': 'black'})  # Gris claro
    elif text in '+-*/()^':
        style.update(basic_ops_style)
    elif text in 'C=.':
        style.update(special_buttons_style)
    button = tk.Button(root, text=text, command=action, **style)
    button.grid(row=row, column=col, sticky='nsew')
    button.config(width=1, height=1)

scientific_buttons = [
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3),
    ('log', 7, 0), ('ln', 7, 1), ('exp', 7, 2, exp)
]

for (text, row, col, *cmd) in scientific_buttons:
    action = cmd[0] if cmd else globals()[text]
    style = button_style.copy()
    style.update(scientific_ops_style)
    button = tk.Button(root, text=text, command=action, **style)
    button.grid(row=row, column=col, sticky='nsew')
    button.config(width=1, height=1)

# Hacer que la interfaz sea adaptable al tamaño de la ventana
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
