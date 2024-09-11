import tkinter as tk
from tkinter import END
import re
import math

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
        expression_with_percentage = re.sub(r'(\d+)%(\d+)', r'(\1*\2/100)', expression)
        result = eval(expression_with_percentage)
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

def exp():
    global expression
    expression += "*10**("
    equation.set(expression)

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

def sin():
    global expression
    try:
        angle = float(expression)
        angle = angle * (3.141592653589793 / 180)
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
        angle = angle * (3.141592653589793 / 180)
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
        angle = angle * (3.141592653589793 / 180)
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
        if number <= 0:
            raise ValueError("Math domain error")
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
        if number <= 0:
            raise ValueError("Math domain error")
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
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def fact():
    global expression
    try:
        number = int(expression)
        if number < 0:
            raise ValueError("Math domain error")
        result = factorial(number)
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def percentage():
    global expression
    try:
        expression_with_percentage = re.sub(r'(\d+)%(\d+)', r'(\1*\2/100)', expression)
        result = eval(expression_with_percentage)
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

def absolute():
    global expression
    try:
        number = float(expression)
        result = math.fabs(number)
        equation.set(str(result))
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = ""

def Dec_Bin(numero):
    binario = ""
    while numero > 0:
        residuo = numero % 2
        numero = numero // 2
        binario = str(residuo) + binario
    return binario

def Bin_Dec(numero):
    decimal = 0
    for i, digito in enumerate(reversed(str(numero))):
        decimal += int(digito) * (2 ** i)
    return decimal

def Dec_Oct(numero):
    octal = ""
    while numero > 0:
        residuo = numero % 8
        numero = numero // 8
        octal = str(residuo) + octal
    return octal

def Oct_Dec(numero):
    decimal = 0
    for i, digito in enumerate(reversed(str(numero))):
        decimal += int(digito) * (8 ** i)
    return decimal

def Dec_Hex(numero):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        numero = numero // 16
        hexadecimal = hex_chars[residuo] + hexadecimal
    return hexadecimal

def Hex_Dec(numero):
    decimal = 0
    hex_chars = "0123456789ABCDEF"
    for i, digito in enumerate(reversed(numero)):
        decimal += hex_chars.index(digito.upper()) * (16 ** i)
    return decimal

equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right', bg='black', fg='#39FF14')
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
    'bg': '#ADD8E6',
    'fg': 'black'
}

scientific_ops_style = {
    'bg': '#90EE90',
    'fg': 'black'
}

special_buttons_style = {
    'bg': '#FF6347',
    'fg': 'white'
}

conversion_ops_style = {
    'bg': '#FFD700',  # Color dorado
    'fg': 'black'
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
        style.update({'bg': '#D3D3D3', 'fg': 'black'})
    elif text in '+-*/()^':
        style.update(basic_ops_style)
    elif text in 'C=.':
        style.update(special_buttons_style)
    button = tk.Button(root, text=text, command=action, **style)
    button.grid(row=row, column=col, sticky='nsew')
    button.config(width=1, height=1)

scientific_buttons = [
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3),
    ('log', 7, 0), ('ln', 7, 1), ('exp', 7, 2, exp), ('n!', 7, 3, fact),
    ('%', 8, 0, lambda: press('%')), ('ABS', 8, 1, absolute)
]

for (text, row, col, *cmd) in scientific_buttons:
    action = cmd[0] if cmd else globals()[text]
    style = button_style.copy()
    style.update(scientific_ops_style)
    button = tk.Button(root, text=text, command=action, **style)
    button.grid(row=row, column=col, sticky='nsew')
    button.config(width=1, height=1)

def update_expression(value):
    global expression
    expression = str(value)
    equation.set(expression)

def validate_decimal(expression):
    try:
        int(expression)
        return True
    except ValueError:
        return False

def validate_binary(expression):
    return all(char in '01' for char in expression)

def validate_hexadecimal(expression):
    try:
        int(expression, 16)
        return True
    except ValueError:
        return False

def validate_no_decimal(expression):
    return '.' not in expression

conversion_buttons = [
    ('Dec-Bin', 9, 0, lambda: update_expression(Dec_Bin(int(expression))) if validate_decimal(expression) and validate_no_decimal(expression) else equation.set("Error")),
    ('Bin-Dec', 9, 1, lambda: update_expression(Bin_Dec(expression)) if validate_binary(expression) else equation.set("Error")),
    ('Dec-Oct', 9, 2, lambda: update_expression(Dec_Oct(int(expression))) if validate_decimal(expression) and validate_no_decimal(expression) else equation.set("Error")),
    ('Oct-Dec', 9, 3, lambda: update_expression(Oct_Dec(expression)) if validate_decimal(expression) and validate_no_decimal(expression) else equation.set("Error")),
    ('Dec-Hex', 10, 0, lambda: update_expression(Dec_Hex(int(expression))) if validate_decimal(expression) and validate_no_decimal(expression) else equation.set("Error")),
    ('Hex-Dec', 10, 1, lambda: update_expression(Hex_Dec(expression)) if validate_hexadecimal(expression) else equation.set("Error"))
]

for (text, row, col, cmd) in conversion_buttons:
    style = button_style.copy()
    style.update(conversion_ops_style)
    button = tk.Button(root, text=text, command=cmd, **style)
    button.grid(row=row, column=col, sticky='nsew')
    button.config(width=1, height=1)
# Agregar botones para letras hexadecimales
hex_buttons = [
    ('A', 11, 0), ('B', 11, 1), ('C', 11, 2), ('D', 11, 3),
    ('E', 12, 0), ('F', 12, 1)
]

for (text, row, col) in hex_buttons:
    button = tk.Button(root, text=text, command=lambda t=text: press(t), **button_style)
    button.grid(row=row, column=col, sticky='nsew')
    button.config(width=1, height=1)

# Configurar las filas y columnas para que se expandan
for i in range(13):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
