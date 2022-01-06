# -*- coding: utf-8 -*-
"""
Implementa funciones para la representación de la solución obtenida por lorenz_solver. Las funciones devolverán gráficas estáticas y no interactivas.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm # Para mapas de color, que sirver para cambiar los colores más facilmente

def rep_puntos(t, x, y, z, X0=(1, 0, 0), params=(10.0, 28, 8/3)):
    """
    Representa la solucón con puntos. Esta función crea una gráfica
    """
    fig = plt.figure() # figsize=(21, 15)
    ax = fig.gca(projection='3d') 
    
    scatterplot = ax.scatter(x, y, z, c=t, marker=".", cmap=cm.gnuplot) 
    
    # Representamos el punto inicial
    ax.scatter(X0[0], X0[1], X0[2], c="black")
    
    plt.colorbar(scatterplot) 
    
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    
    # por algun motivo esto no funciona cuando lo corres en consola
    #ax.set_title(f"Trayectoria descrita, X0=({X0[0]:.3f}, {X0[1]:.3f}, {X0[2]:.3f}), (a, b, c)=({params[0]:.3f}, {params[1]:.3f}, {params[2]:.3f})") 
    # si no lo convertimos a lista da un error: "unsupported format string passed to numpy.ndarray.__format__"
    X0 = list(X0)
    params = list(params)
    ax.set_title(f"Trayectoria descrita, X0=({X0[0]:.3f}, {X0[1]:.3f}, {X0[2]:.3f}), (a, b, c)=({params[0]:.3f}, {params[1]:.3f}, {params[2]:.3f})")
    
    plt.show()

def rep_lineas(x, y, z, X0=(1, 0, 0), params=(10.0, 28, 8/3), grosor=0.05):
    """
    Representa la solucón con una línea monocromática. Esta función crea una gráfica
    """
    fig = plt.figure() # figsize=(21, 15)
    ax = fig.gca(projection='3d') 
    
    ax.plot(x, y, z, lw=grosor) 
    
    # Representamos el punto inicial
    ax.scatter(X0[0], X0[1], X0[2], c="black")
    
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    
    X0 = list(X0)
    params = list(params)
    ax.set_title(f"Trayectoria descrita, X0=({X0[0]:.3f}, {X0[1]:.3f}, {X0[2]:.3f}), (a, b, c)=({params[0]:.3f}, {params[1]:.3f}, {params[2]:.3f})") 
    
    plt.show()

def rep_lineas_color(t, x, y, z, X0=(1, 0, 0), params=(10.0, 28, 8/3), grosor=0.05):
    """
    IMPORTANTE: ESTA FUNCIÓN TARDA 2 MINUTOS EN REPRESENTAR 100 000 PUNTOS
    Representa la solucón con una línea que cambia de color. Esta función crea una gráfica
    """
    fig = plt.figure() # figsize=(21, 15)
    ax = fig.gca(projection='3d') 
    
    m = len(t)
    for i in range(1, m): # el color es un rgb con valores 0-1. Interpola con verde.
        ax.plot(x[i-1:i+1], y[i-1:i+1], z[i-1:i+1], c=(0, i/m, 0), lw=grosor)
    
    # Representamos el punto inicial
    ax.scatter(X0[0], X0[1], X0[2], c="black")
    
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    
    X0 = list(X0)
    params = list(params)
    ax.set_title(f"Trayectoria descrita, X0=({X0[0]:.3f}, {X0[1]:.3f}, {X0[2]:.3f}), (a, b, c)=({params[0]:.3f}, {params[1]:.3f}, {params[2]:.3f})") 
    
    plt.show()
