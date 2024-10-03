from math import *
gravidade = 9.8
inclinacao_plano = float(input("Informe a inclinação do plano em graus "))
coef_E = float(input("Informe o coeficiente estático "))
coef_C = float(input("Informe o coeficiente cinético "))
massa = float(input("Informe a massa do objeto em kilogramas "))
forca = float(input("Informe a força no objeto em Newtons "))
inclinacao_forca = float(input("Informe a inclinação da força no objeto em graus "))

Peso_x = massa * gravidade * sin((inclinacao_plano * pi)/180)
Peso_y = massa * gravidade * cos((inclinacao_plano * pi)/180)
Forca_x = forca * cos(((inclinacao_forca - inclinacao_plano) * pi)/180)
Forca_y = forca * sin(((inclinacao_forca - inclinacao_plano) * pi)/180)
Normal = Peso_y - Forca_y
Fat_Max = coef_E * Normal
Fat_Cin = coef_C * Normal
print(f"Peso = {massa * gravidade:.2f} N")
print(f"Peso X = {Peso_x:.2f} N")
print(f"Peso Y = {Peso_y:.2f} N")
print(f"Forca X = {Forca_x:.2f} N")
print(f"Forca Y = {Forca_y:.2f} N")
print(f"Normal = {Normal:.2f} N")
print(f"Força de atrito máximo = {Fat_Max:.2f} N")
print(f"Força de atrito cinético = {Fat_Cin:.2f} N")
if Fat_Max >= abs(Forca_x):
    print("Aceleração = 0.0 m/s^2")
else:
    Aceleracao = (Forca_x - Fat_Cin - Peso_x)/ massa 
    print(f"Aceleração = {Aceleracao:.3f} m/s^2")