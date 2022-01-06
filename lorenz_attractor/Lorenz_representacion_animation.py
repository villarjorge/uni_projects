# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:15:26 2021

Implementa funciones que devuelven animaciones

a = input('¿Le gustaría guardarse la grafica como un gif?; escriba si si quiere y no si no quiere: ')
print('¡El archivo se le guardara en la misma carpeta donde tenga el notebook!')
print('Muchas gracias por guardarlo')
print('Ha decidido no guardarse el gif en su dispositivo,')
print('siga ejecutando el codigo para poder disfrutar de las animaciones que le quedan por descubrir')
print('lo siento, no ha introducido una de las dos opciones dadas')
print('vuelva a ejecutar la celda si quiere guardarse la imagen')
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation 
from matplotlib.animation import PillowWriter 

def rep_ani(x, y, z, X0=(1, 0, 0), params=(10.0, 28, 8/3), nombre="Lorenz-Rotar angulo azimutal", grosor=0.05):
    """
    Devuelve una animacion en la que se rota la solucion entorno a el eje z
    """  
    def init():
        # Función que inicializa la gráfica que queremos animar
        # representación con líneas
        ax.plot(x, y, z, lw=grosor)
        # Representamos el punto inicial
        ax.scatter(X0[0], X0[1], X0[2], c="black")

        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.set_zlabel("Eje Z")

        #X0 = list(X0)
        #params = list(params)
        ax.set_title(f"Trayectoria descrita, X0=({X0[0]:.3f}, {X0[1]:.3f}, {X0[2]:.3f}), (a, b, c)=({params[0]:.3f}, {params[1]:.3f}, {params[2]:.3f})")

        return fig,
    
    def animate(i):
        # Función que controla lo que animaremos, en este caso giramos el angulo azimutal
        ax.view_init(elev=30, azim=2*i)
        return fig,
    
    # Creamos la figura sobre la que vamos a hacer al animación
    fig = plt.figure(figsize=(21, 15))
    ax = fig.gca(projection='3d')
    # Creamos la animación. Como puedes ver utilizamos las funciones definidas antes y especificamos el número de fotogramas
    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=180, interval=50)
    
    nombre += ".gif"
    
    ani.save(nombre, writer='pillow', fps=20)
   