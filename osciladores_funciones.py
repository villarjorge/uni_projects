# -*- coding: utf-8 -*-
"""
Creado: 22/10/2021

Autor: Jorge San José

Este programa define dos funciones cuya descripción se puede ver en el docstring
"""
import numpy as np

def oscilador_amortiguado(t, m, k, c, A_0):
    """
    Nota: En la mayoría de parámetros no tiene un sentido físico que sean cero o negativo. Por ello no se han programado excepciones y puede 
    llegar a haber errores o resultados inesperados al introducir ese tipo de valores. Se recomienda mantener las inputs sanedas
    
    Esta función necesita de numpy
    
    Esta función utiliza la solución estandar a la ecuación diferencial de un oscilador armónico amortiguado para calcular 
    su posición, velocidad, aceleración y ratio de amortiguación función del tiempo, masa, constante de fuerza y coeficiente de amortiguación.
    
    Parámetros: 
        Input:
            - t: Un float. el tiempo en segundos 
            - m: Un float, uno negativo o cero no tiene sentido físico. la masa unida al muelle en kilogramos
            - k: Un float, uno negativo o cero no tiene sentido físico. la constante de fuerza del muelle en Newton/metro
            - c: Un float, uno negativo o cero no tiene sentido físico. el coeficiente de amortiguación del fluido en el que se encuentra en kilogramo/segundo
            - A_0: el desplazamiento inicial en metros
        Output:
            - x: Un float. la posición en metros
            - v: Un float. La velocidad en metros por segundo
            - a: Un float. la aceleración en metros por segundo por segundo
            - zeta: Un float. el ratio de amortiguación, se utiliza para determinar cómo evoluciona el sistema. (Es la letra griega dseta)
    """
    # Para entender mejor esta parte puedes ir a https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_%28OpenStax%29/Map%3A_University_Physics_I_-_Mechanics_Sound_Oscillations_and_Waves_%28OpenStax%29/15%3A_Oscillations/15.06%3A_Damped_Oscillations
    # donde se proporciona una solución cerrada
    alpha = c/(2*m)
    if k/m - alpha**2 > 0: # Si "w^2" no es un número negativo procedemos de forma normal
        w = np.sqrt(k/m - alpha**2) # La frecuencia angular
        A_t = A_0*np.exp(-alpha*t) # La amplitud, que que decae con el tiempo
        x = A_t*np.cos(w*t)
        v = -A_t*(alpha*np.cos(w*t) + w*np.sin(w*t))
        a = alpha*v - A_t*(w**2*np.cos(w*t)-alpha*w*np.sin(w*t))
        zeta =  c/(2*np.sqrt(m*k)) # Corresponde a la letra griega dseta
        return x, v, a, zeta
    elif k/m - alpha**2 == 0: # Si w es cero la parte sinusoidal se esfuma, el sistema vuelve a la posición más estable lo más rápido posible
        A_t = A_0*np.exp(-alpha*t)
        x = A_t
        v = -alpha*A_t
        a = alpha**2*A_t
        zeta =  c/(2*np.sqrt(m*k))
        return x, v, a, zeta
    else: # Si la expresión es negativa w será un número imaginário. Este es el caso de sobreamortiguación en el cual no se oscila. Para mayores parámetros de "c" más despacio volverá a la posición de equilibrio
        w = np.sqrt(alpha**2 - (k/m))**(-1)    
        A_t = A_0*np.exp(-alpha*w*t)
        x = A_t
        v = -alpha*A_t
        a = alpha**2*A_t
        zeta =  c/(2*np.sqrt(m*k))
        return x, v, a, zeta

def oscilador_amortiguado_fuerza_externa(t, m, k, c, A_0, F_0, f_f):
    """
    Nota: En la mayoría de parámetros no tiene un sentido físico que sean cero o negativo. Por ello no se han programado excepciones y puede 
    llegar a haber errores o resultados inesperados al introducir ese tipo de valores. Se recomienda mantener las inputs sanedas
        
    Esta función necesita de numpy
    
    Esta función calcula la posición, velocidad y aceleración asi como el ratio de amortiguación de un oscilador con 
    una fuerza sinusoidal en función del tiempo, masa, constante del muelle, coeficietente de amortiguación, módulo 
    de la fuerza inical y frecuencia angular de la fuerza. La fuerza aplicada es F(t) = F_0*cos(f_f*t)
    
    Parámetros: 
        Input:
            - t: Un float. el tiempo en segundos 
            - m: Un float, uno negativo o cero no tiene sentido físico. la masa unida al muelle en kilogramos
            - k: Un float, uno negativo o cero no tiene sentido físico. la constante de fuerza del muelle en Newton/metro
            - c: Un float, uno negativo o cero no tiene sentido físico. el coeficiente de amortiguación del fluido en el que se encuentra en kilogramo/segundo
            - A_0: Un float. El desplazamiento inicial en metros
            - F_0: Un float. Valor de la fuerza en el instante cero
            - f_f: Un float. la frecuencia angular de la fuerza
        Output:
            - x: Un float. la posición en metros
            - dseta: Un float. el ratio de amortiguación, se utiliza para determinar cómo evoluciona el sistema. (Es la letra griega dseta)
    """
    w_0 = np.sqrt(k/m)
    dseta = c/(2*np.sqrt(m*k))
    z_m = np.sqrt((2*w_0*dseta*f_f)**2 + (w_0**2 - f_f**2)**2)
    if type(f_f) == int: # Tnemos que considerar si es una array dado que hacemos una comparación
        if w_0**2 == f_f**2: # Si ambos son iguales entonces tendríamos una división por cero, que daría infinito. La arco tangente de infinito es pi/2
            phi = np.pi/2
            x = F_0/(m*z_m)*np.cos(f_f*t + phi)
        else: 
            phi = np.arctan((2*w_0*f_f*dseta)/(w_0**2 - f_f**2))
            x = F_0/(m*z_m)*np.cos(f_f*t + phi)
        return x, dseta
    else:
        if w_0**2 == (f_f.any())**2: # Si ambos son iguales entonces tendríamos una división por cero, que daría infinito. La arco tangente de infinito es pi/2
            phi = np.pi/2
            x = F_0/(m*z_m)*np.cos(f_f*t + phi)
        else: 
            phi = np.arctan((2*w_0*f_f*dseta)/(w_0**2 - f_f**2))
            x = F_0/(m*z_m)*np.cos(f_f*t + phi)
        return x, dseta