import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

##inicializar variables
num_muestras = 10000
muestras_por_frame = 1
num_frames = num_muestras // muestras_por_frame
x_dentro_total, y_dentro_total, x_fuera_total, y_fuera_total = [], [], [], []
dentro_del_circulo = 0  # contador acumulativo

#algoritmo montecarlo
def montecarlo_pi(num_muestras, frame):
    global dentro_del_circulo
    puntos_x_dentro = []
    puntos_y_dentro = []
    puntos_x_fuera = []
    puntos_y_fuera = []
    for _ in range(num_muestras):
        x, y = 2*np.random.random()-1, 2*np.random.random()-1  # Coordenadas entre -1 y 1
        distancia_al_centro = x**2 + y**2
        if distancia_al_centro <= 1:
            dentro_del_circulo += 1
            puntos_x_dentro.append(x)
            puntos_y_dentro.append(y)
        else:
            puntos_x_fuera.append(x)
            puntos_y_fuera.append(y)
    pi_estimado = 4 * (dentro_del_circulo / (num_muestras * (frame + 1)))
    return puntos_x_dentro, puntos_y_dentro, puntos_x_fuera, puntos_y_fuera, pi_estimado



fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_title("Estimación de π usando Montecarlo")
circle = plt.Circle((0, 0), 1, color='black', fill=False)
ax.add_patch(circle)
scatter_dentro, = ax.plot([], [], 'bo', ms=2)
scatter_fuera, = ax.plot([], [], 'ro', ms=2)
text_pi = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    scatter_dentro.set_data([], [])
    scatter_fuera.set_data([], [])
    text_pi.set_text('')
    return scatter_dentro, scatter_fuera, text_pi


def update(frame):
    global x_dentro_total, y_dentro_total, x_fuera_total, y_fuera_total
    x_dentro, y_dentro, x_fuera, y_fuera, pi_est = montecarlo_pi(muestras_por_frame, frame)
    x_dentro_total += x_dentro
    y_dentro_total += y_dentro
    x_fuera_total += x_fuera
    y_fuera_total += y_fuera
    scatter_dentro.set_data(x_dentro_total, y_dentro_total)
    scatter_fuera.set_data(x_fuera_total, y_fuera_total)
    total_dardos = muestras_por_frame * (frame + 1)
    text_pi.set_text(f'π ≈ {pi_est:.4f} con {total_dardos} dardos')
    return scatter_dentro, scatter_fuera, text_pi

ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=False, interval = 1)
plt.show()
