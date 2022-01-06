# -*- coding: UTF-8 -*-

#Resuelve el sistema de ecuaciones diferenciales de lorenz con los parametros pedidos. La función solver es un tanto redundante


from scipy.integrate import solve_ivp #import numpy as np

def Lorenz(t, X, a, b, c):
    """
    Funcion que define el lado derecho de el sistema de ec. diferenciales de lorenz
    
    Input: 
        - t: tiempo
        - X: vector de "posicion" en espacio de fase tridimensional
        - a, b, c: parametros del sistema. 
    Output:
        - Vector X punto
    """
    # Desempaquetamos las componentes del vector X
    x, y, z = X 
    # Calculamos las derivadas que definen el sistema
    dxdt = a*(y - x)
    dydt = x*(b - z) - y
    dzdt = x*y - c*z
    # Devolvemos dichas derivadas en forma de vector
    return [dxdt, dydt, dzdt]

def solver(tmax=1000, X0=(1, 0, 0), params=(10.0, 28, 8/3), paso_max=0.01):
    """
    Funcion que resuelve el sistema definido por Lorenz() utilizando solve_ivp
    
    Input: 
        - tmax: tiempo de vuelo, valor pred.= 1000
        - X0: condicion inicial, el valor predeterminado es el (0,0,0)
        - params: parametros del sistema. Poseen valores predeterminados que dan lugar a la famosa mariposa
        - paso_max: El paso mÃ¡ximo del sistema de resolucion. A pesar de ser adaptativo es mejor poner un paso pequeno para obtener puntos mas cercanos y por
        tanto figuras mas suaves
    Output: 
        - Objeto solucion proporcionado por solve_ivp
    """
    return solve_ivp(Lorenz, t_span=(0, tmax), y0=X0, args=params, max_step=paso_max)