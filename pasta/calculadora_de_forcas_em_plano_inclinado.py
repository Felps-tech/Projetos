from math import *
g = 9.8
anguloPlano = float(input("Qual o angulo de inclinação do plano em graus: "))
atritoE = float(input("Informe o atrito estatico da superficie: "))
atritoC = float(input("Informe o atrito cinetico da superficie: "))
massa = float(input("Informe a massa do objeto em kilogramas: "))
moduloF = float(input("Informe o modulo da força que atua no objeto em Newtons: "))
angulof = float(input("Informe o angulo da força aplicado no objeto em graus: "))
Fx = cos(((angulof - anguloPlano) * pi)/180) * moduloF
Fy = sin(((angulof - anguloPlano) * pi)/180) * moduloF
Px = (massa * g) * sin((anguloPlano * pi)/180) 
Py = (massa * g) * cos((anguloPlano * pi)/180) 
N = Py - Fy
FatMax = N * atritoE
Aceleracao = (Fx - Px)/massa

if atritoC != 0 and atritoE != 0:
    print(f"Normal: {N:.3} N")
    print(f"Fx: {Fx:.3} N")
    print(f"Fy: {Fy:.3} ")
    print(f"Peso: {massa * g:.3} N")
    print(f"Px: {Px:.3} N")
    print(f"Py: {Py:.3} N") 
    print(f"FatMax: {FatMax:.3} N") 
    if moduloF <= FatMax:
        print("Aceleração do sistema com atrito = 0 m/s^2")
    else:
        FatC = N * atritoC
        print(f"FatC: {FatC:.3} N") 
        print(f"Aceleração do sistema com atrito = {((Fx - Px - FatC)/massa):.3} m/s^2")
else:
    print(f"Normal: {N:.3} N")
    print(f"Fx: {Fx:.3} N")
    print(f"Fy: {Fy:.3} N")
    print(f"Peso: {massa * g:.3} N")
    print(f"Px: {Px:.3} N")
    print(f"Py: {Py:.3} N")
    print(f"Aceleração do sistema = {Aceleracao:.3} m/s^2")