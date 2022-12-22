import sys

try:
    x= int(input("x: "))
    y= int(input("y: "))
except ValueError:
    print("Solo numeros, no letras")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
     print("No se puede dividir por Zero")
     sys.exit(1)

print(f"{x} / {y} = {result}")