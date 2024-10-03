from vpython import *
from math import *
angulo = int(input("Informe o valor do angulo do plano em graus "))

teta = radians(180 - angulo) # rad  (180 graus - 31 graus)

PlanoInclinado = box(pos = vector(0, 0, 0), size = vector(2, 0.02, 0.2))
PlanoInclinado.rotate(angle = teta, origin = vector(0, 0, 0), axis = vector(0, 0, 1))

Plano = box(pos = vector(1.855, -0.502, 0), size = vector(2, 0.02, 0.2), color=color.green, opacity = 0.1)

caixa = box(pos = vector(1, -0.11, 0), v = vector(0, 0, 0), size = vector(0.2, 0.2, 0.2), color=color.red)
caixa.rotate(angle = teta, origin = vector(0, 0, 0), axis = vector(0, 0, 1))

S = 2 #m
t = 0 #s
dt = 0.005

g = 9.8 # m/s^2
T = 2.2 # s

a = (2 * S) / (T ** 2) # aceleração resultante (cte)

ud = tan(angulo) - ((a) / (g * cos(angulo))) # ud (cte) e 0.541052 rad = 31 graus
print('ud =', ud)

ax = a * cos(teta) 
ay = a * sin(teta)

print('a =', a, 'm/s²')

caixa.vetora = vector(- ax, - ay, 0)
attach_arrow(caixa, 'vetora', color=color.yellow, scale = 0.5, shaftwidth = 0.05, opacity = 0.7) 

while t <= (T - dt):
    rate(100)

    caixa.v.y = caixa.v.y - ay * dt 
    caixa.v.x = caixa.v.x - ax * dt
    caixa.pos.y = caixa.pos.y + caixa.v.y * dt
    caixa.pos.x = caixa.pos.x + caixa.v.x * dt

    t = t + dt
    if caixa.pos == Plano.pos:
        print('O objeto atingiu o plano')
    

print('S =', S, 'm')
print('Vf =', mag(caixa.v), 'm/s')
print('t =', t, 's')