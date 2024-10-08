import tkinter as tk
from tkinter import END
import re
import math

root = tk.Tk()
root.title("Calculadora Científica")
root.geometry("400x600")

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
        result = math.sin(math.radians(angle))
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def cos():
    global expression
    try:
        angle = float(expression)
        result = math.cos(math.radians(angle))
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def tan():
    global expression
    try:
        angle = float(expression)
        result = math.tan(math.radians(angle))
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def log():
    global expression
    try:
        number = float(expression)
        result = math.log10(number)
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def ln():
    global expression
    try:
        number = float(expression)
        result = math.log(number)
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def sqrt():
    global expression
    try:
        number = float(expression)
        result = math.sqrt(number)
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
entry = tk.Entry(root, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
entry.grid(columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2, equalpress), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('^', 5, 2, power), ('C', 5, 3, clear)
]

for (text, row, col, *cmd) in buttons:
    action = cmd[0] if cmd else lambda t=text: press(t)
    tk.Button(root, text=text, padx=20, pady=20, command=action).grid(row=row, column=col)

scientific_buttons = [
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3),
    ('log', 7, 0), ('ln', 7, 1), ('exp', 7, 2, exp)
]

for (text, row, col, *cmd) in scientific_buttons:
    action = cmd[0] if cmd else globals()[text]
    tk.Button(root, text=text, padx=20, pady=20, command=action).grid(row=row, column=col)

root.mainloop()
