from particula import Particula
import matplotlib.pyplot as plt

# Criar a partícula
p = Particula(x=0, y=0, vx=10, vy=10, massa=1)

# Parâmetros físicos
dt = 0.1
g = -9.8

# Define as funções de força
fx_func = lambda p: 0
fy_func = lambda p: p.massa * g

# Evoluir a partícula
p.evoluir(fx_func=fx_func, fy_func=fy_func, dt=dt)

# Exibir número de pontos
print("Número de pontos simulados:", len(p.trajetoria_x))

# Plotar
plt.plot(p.trajetoria_x, p.trajetoria_y)
plt.title("Lançamento Oblíquo")
plt.xlabel("Posição x (m)")
plt.ylabel("Posição y (m)")
plt.grid(True)
plt.show()
