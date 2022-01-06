# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:31:21 2021

@author: villa

Implementa las funciones necesáreas para representar una gráfica interactiva.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button
import Lorenz_solver as s

def rep_sliders(x, y, z, init_X0=(1, 0, 0), init_params=(10.0, 28, 8/3)):
    """
    Representa la solución con tres sliders, uno para cada uno de los parámetros. Esta función crea una gráfica interactiva
    """    
    
    fig = plt.figure() # Creamos la figura
    ax = fig.gca(projection='3d') # creamos los ejes tridimensionales
    
    ax.plot(x, y, z, lw=0.15) # primera representación con la solución ya suministrada
    ax.scatter(init_X0[0], init_X0[1], init_X0[2], c="black")
    
    axcolor = 'lightgoldenrodyellow' # definimos el color de los sliders que usaremos más adelante
    ax.margins(x=0)
    
    # ajustamos la posición de la representación para acomodar los sliders
    plt.subplots_adjust(left=0.25, bottom=0.25)
    
    # hacer un slider vertical para controlar "a". Los cuatro números controlan la posición, el grosor y la altura del slider
    axamp = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor=axcolor)
    a_slider = Slider(
        ax=axamp,
        label="a",
        valmin=0,
        valmax=20,
        valinit=init_params[0],
        orientation="vertical"
    )
    # uno para "b"
    axamp = plt.axes([0.15, 0.25, 0.0225, 0.63], facecolor=axcolor)
    b_slider = Slider(
        ax=axamp,
        label="b",
        valmin=18,
        valmax=38,
        valinit=init_params[1],
        orientation="vertical"
    )
    # uno para "c"
    axamp = plt.axes([0.20, 0.25, 0.0225, 0.63], facecolor=axcolor)
    c_slider = Slider(
        ax=axamp,
        label="c",
        valmin=1, # por lo que he podido ver no le gustan valores negativos
        valmax=(8/3)+15,
        valinit=init_params[2],
        orientation="vertical"
    )
    # La función que será llamada cuando se actualice el slider
    def update(val): # para cada vez que se mueve el slider recalculamos la solución
        ax.clear()
        new_params = (a_slider.val, b_slider.val, c_slider.val)
        sol = s.solver(tmax=100, X0=init_X0, params=new_params, paso_max=0.01) #tomamos menos puntos para conseguir mayor rapidez
        x, y, z = sol.y 
        ax.plot(x, y, z, lw=0.15)
        ax.scatter(init_X0[0], init_X0[1], init_X0[2], c="black")
    
    # Estas lineas registran cuando se cambia el slider
    a_slider.on_changed(update)
    b_slider.on_changed(update)
    c_slider.on_changed(update)
    
    # Creamos un boton para resetear los valores del slider
    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
    
    def reset(event): # esta función se llamará cuando se pulse el botón
        a_slider.reset()
        b_slider.reset()
        c_slider.reset()
    button.on_clicked(reset)
    
    plt.show()