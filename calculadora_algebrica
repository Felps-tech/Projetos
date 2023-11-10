from math import *
ponto1 = [0,0,0]
ponto2 = [0,0,0]
reta1 = [0,0,0]
reta2 = [0,0,0]
plano1 = [0,0,0,0]
plano2 = [0,0,0,0]
calcular = input("Qual distancia quer calcular? (Ponto = PO, Reta = RE, Plano = PL ) ").upper()
if calcular == "POPO":
    ponto1[0] = int(input("Informe a coordenada x do primeiro ponto "))
    ponto1[1] = int(input("Informe a coordenada y do primeiro ponto "))
    ponto1[2] = int(input("Informe a coordenada z do primeiro ponto "))
    ponto2[0] = int(input("Informe a coordenada x do segundo ponto "))
    ponto2[1] = int(input("Informe a coordenada y do segundo ponto "))
    ponto2[2] = int(input("Informe a coordenada z do segundo ponto "))

    distancia = sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2 + (ponto2[2] - ponto1[2])**2)
    print(f"A distancia entre os pontos é {distancia:.3} u.c")

if calcular == "PORE" or calcular == "REPO":
    ponto1[0] = int(input("Informe a coordenada x do ponto "))
    ponto1[1] = int(input("Informe a coordenada y do ponto "))
    reta1[0] = int(input("Informe a coordenada x da reta "))
    reta1[1] = int(input("Informe a coordenada y da reta "))
    reta1[2] = int(input("Informe a coordenada z da reta "))
    
    distancia = (abs((reta1[0] * ponto1[0]) + (reta1[1] * ponto1[1]) + reta1[2]))/sqrt(ponto1[0]**2 + ponto1[1]**2)
    print(f"A distancia entre o ponto e a reta é {distancia:.3} u.c")

if calcular == "POPL" or calcular == "PLPO":
    ponto1[0] = int(input("Informe a coordenada x do ponto "))
    ponto1[1] = int(input("Informe a coordenada y do ponto "))
    ponto1[2] = int(input("Informe a coordenada z do ponto "))
    plano1[0] = int(input("Informe a coordenada a do plano "))
    plano1[1] = int(input("Informe a coordenada b do plano "))
    plano1[2] = int(input("Informe a coordenada c do plano "))
    plano1[3] = int(input("Informe a coordenada d do plano "))
    
    distancia = (abs(plano1[0]*ponto1[0] + plano1[1]*ponto1[1] + plano1[2]*ponto1[2] + plano1[3]))/sqrt(plano1[0]**2 + plano1[1]**2 + plano1[2]**2)
    print(f"A distancia entre o ponto e o plano é {distancia:.3} u.c")

if calcular == "REPL" or calcular == "PLRE" :
    reta1[0] = int(input("Informe a coordenada x da reta "))
    reta1[1] = int(input("Informe a coordenada y da reta "))
    reta1[2] = int(input("Informe a coordenada z da reta "))
    plano1[0] = int(input("Informe a coordenada a do plano "))
    plano1[1] = int(input("Informe a coordenada b do plano "))
    plano1[2] = int(input("Informe a coordenada c do plano "))
    plano1[3] = int(input("Informe a coordenada d do plano "))
    
    distancia = (abs(plano1[0]*reta1[0] + plano1[1]*reta1[1] + plano1[2]*reta1[2] + plano1[3]))/sqrt(plano1[0]**2 + plano1[1]**2 + plano1[2]**2)
    print(f"A distancia entre a reta e o plano é {distancia:.3} u.c")

if calcular == "RERE":
    reta1[0] = int(input("Informe a coordenada x da primeira reta "))
    reta1[1] = int(input("Informe a coordenada y da primeira reta "))
    reta1[2] = int(input("Informe a coordenada z da primeira reta "))
    reta2[0] = int(input("Informe a coordenada x da segunda reta "))
    reta2[1] = int(input("Informe a coordenada y da segunda reta "))
    reta2[2] = int(input("Informe a coordenada z da segunda reta "))
    
    a = reta1[0]/reta2[0]
    b = reta1[1]/reta2[1]
    if a == b:
        P = (-1 * reta1[2])/reta1[0]
        distancia = abs(reta2[0] * P + reta2[2])/sqrt(reta2[0]**2 + reta2[1]**2)
        print(f"A distancia entre os planos é {distancia:.3} u.c")
    else:
        print("As retas não são paralelas")
        
if calcular == "PLPL":
    plano1[0] = int(input("Informe a coordenada a do primeiro plano "))
    plano1[1] = int(input("Informe a coordenada b do primeiro plano "))
    plano1[2] = int(input("Informe a coordenada c do primeiro plano "))
    plano1[3] = int(input("Informe a coordenada d do primeiro plano "))
    plano2[0] = int(input("Informe a coordenada a do segundo plano "))
    plano2[1] = int(input("Informe a coordenada b do segundo plano "))
    plano2[2] = int(input("Informe a coordenada c do segundo plano "))
    plano2[3] = int(input("Informe a coordenada d do segundo plano "))
    
    a = plano1[0]/plano2[0]
    b = plano1[1]/plano2[1]
    c = plano1[2]/plano2[2]
    if a == b == c:
        P = (-1 * plano1[3])/plano1[0]
        distancia = abs(plano2[0] * P + plano2[3])/sqrt(plano2[0]**2 + plano2[1]**2 + plano2[2]**2)
        print(f"A distancia entre os planos é {distancia:.3} u.c")
    else:
        print("Os planos não são paralelos.")
