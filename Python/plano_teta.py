from vpython import *
from math import *

# Ask for user input
mass = float(input("Informe a massa do objeto em kilos: "))
force_magnitude = float(input("Informe a magnitude da força aplicada em Newtons: "))
plano_angulo = int(input("Informe o valor do angulo do plano em graus: "))
forca_angulo = int(input("Informe o valor do angulo da força em graus: "))

# Convert angles to radians
plano_teta = radians(180 - plano_angulo)
forca_teta = radians(180 - forca_angulo)

# Set up scene
PlanoInclinado = box(pos=vector(0, 0, 0), size=vector(2, 0.02, 0.2))
PlanoInclinado.rotate(angle=plano_teta, origin=vector(0, 0, 0), axis=vector(0, 0, 1))

Plano = box(pos=vector(1.855, -0.502, 0), size=vector(2, 0.02, 0.2), color=color.green, opacity=0.1)

caixa = box(pos=vector(1, -0.11, 0), v=vector(0, 0, 0), size=vector(0.2, 0.2, 0.2), color=color.red)
caixa.rotate(angle=plano_teta, origin=vector(0, 0, 0), axis=vector(0, 0, 1))

# Calculate acceleration and force components
g = 9.8  # m/s^2
a = force_magnitude / mass
force_x = force_magnitude * cos(forca_teta)
force_y = force_magnitude * sin(forca_teta)

# Print ud
ud = tan(plano_angulo) - (a / (g * cos(plano_angulo)))
print('Atrito =', ud)

# Set initial velocity and attach arrow
ax = a * cos(plano_teta)
ay = a * sin(plano_teta)
caixa.vetora = vector(-ax, -ay, 0)
attach_arrow(caixa, 'vetora', color=color.yellow, scale=0.5, shaftwidth=0.05, opacity=0.7)

# Simulation parameters
S = 2  # m
t = 0  # s
dt = 0.005
T = 5  # s

# Simulation loop
while t <= (T - dt):
    rate(100)

    caixa.v.y = caixa.v.y - ay * dt
    caixa.v.x = caixa.v.x - ax * dt
    caixa.pos.y = caixa.pos.y + caixa.v.y * dt
    caixa.pos.x = caixa.pos.x + caixa.v.x * dt

    t = t + dt
    if caixa.pos == Plano.pos:
        print('O objeto atingiu o plano')

# Calculate and print forces
normal_force = mass * g * cos(plano_angulo)
weight_force = mass * g * sin(plano_angulo)
resultant_force_x = force_x
resultant_force_y = force_y - weight_force  # Subtract weight force as it acts in the opposite direction of the applied force

print('Força Normal =', normal_force, 'N')
print('Força Peso =', weight_force, 'N')
print('Força Resultante em x =', resultant_force_x, 'N')
print('Força Resultante em y =', resultant_force_y, 'N')
