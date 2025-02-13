# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

# processing
if a + b > c and a + c > b and b + c > a:
    resultado = "Los lados pueden formar un triángulo."
else:
    resultado = "Los lados no pueden formar un triángulo."

# prueba

# output
print(resultado)