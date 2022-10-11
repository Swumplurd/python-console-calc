from multiplicacion import multiplicacion
from division import division
from resta import resta
from suma import suma
from menu import menu
from sys import argv
import os

def calculadora(a, b):
    while True:
        op = input(menu)

        os.system("cls")
        if op == "1":
            print(f"{a} + {b} = {suma(a, b)}")
        elif op == "2":
            print(f"{a} - {b} = {resta(a, b)}")
        elif op == "3":
            print(f"{a} * {b} = {multiplicacion(a, b)}")
        elif op == "4":
            print(f"{a} / {b} = {division(a, b)}")
        elif op == "5":
            break
        else:
            print("Opcion invalida")

if len(argv) != 3:
    print("Argumentos insufisientes o sobrepasados, por favor escribe dos argumentos validos (que sean numeros)")
elif not argv[1].isdigit() or not argv[2].isdigit():
    print("Por favor ingresa digitos en los argumentos")
elif argv[1].isdigit() and argv[2].isdigit():
    a = int(argv[1])
    b = int(argv[2])
    calculadora(a, b)