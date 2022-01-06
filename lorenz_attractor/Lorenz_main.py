# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 13:05:48 2021

@author: villa
"""

import Lorenz_solver as s
import Lorenz_representacion_simple as r
import Lorenz_representacion_sliders as r_sliders
import Lorenz_representacion_animation as r_animation
import numpy as np

# gracias a esta web: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
print("  ___   _                       _                      _         _                                    ")
print(" / _ \ | |                     | |                    | |       | |                                   ")
print("/ /_\ \| |_  _ __   __ _   ___ | |_   ___   _ __    __| |  ___  | |      ___   _ __   ___  _ __   ____")
print("|  _  || __|| '__| / _` | / __|| __| / _ \ | '__|  / _` | / _ \ | |     / _ \ | '__| / _ \| '_ \ |_  /")
print("| | | || |_ | |   | (_| || (__ | |_ | (_) || |    | (_| ||  __/ | |____| (_) || |   |  __/| | | | / / ")
print("\_| |_/ \__||_|    \__,_| \___| \__| \___/ |_|     \__,_| \___| \_____/ \___/ |_|    \___||_| |_|/___|")

control_principal = True # Esta será la variable controla el bucle while principal del programa.

Dict_Parametros = {"Coeficientes":(10.0, 28.0, 8/3), "Punto inicial":np.random.rand(3), "Tiempo de vuelo":1000, "Grosor":0.05}

Dict_Parametros_defecto = {"Coeficientes":(10.0, 28.0, 8/3), "Punto inicial":np.random.rand(3), "Tiempo de vuelo":1000, "Grosor":0.05}

print()
print("Parámetros por defecto, los coeficientes producen la forma característica del atractor de lorenz, el punto inicial es aleatorio, el grosor es de la linea y es el que funciona mejor con los parámetros por defecto: ")
for parametro, valor in Dict_Parametros.items():
    if type(valor) == int:
        print(f"{parametro} = {valor}")
    elif type(valor) == float:
        print(f"{parametro} = {valor}")
    else:
        print(parametro, "=", list([round(i, 3) for i in valor])) # hay que hacer esto porque son listas, no puedes :.3f a una lista
        
opciones = "\nOpciones: \n      0. Mostrar opciones.\n      1. Cambiar parámetros.\n      2. Imprimir valores actuales.\n      3. Imprimir gráfica (Color representa el tiempo, Tarda mucho).\n      4. Imprimir gráfica (Líneas monocromas).\n      5. Imprimir gráfica (Puntos).\n      6. Representación interactiva (Líneas). \n      7. Crear y guardar animación (Rotación alrededor de z). \n      8. Salir."
print(opciones)


while control_principal:
    opcion = input("Para selecionar una opción escriba su número correspondiente: (Introducir cero para volver a mostrar las opciones) ")

    if opcion == "0": # Esta opción muestra las opciones de nuevo
        print(opciones)
    elif opcion == "1": # Esto es lo que permite cambiar un valor. También es donde gestionamos las entradas no validas
        while True: # si el parametro no existe no dejaremos al usuario pasar al bucle, seguiremos preguntando hasta que nos de un parámetro que exista
            parametro = input("Introduce el parámetro a cambiar. Los parámetros son: Coeficientes, Punto inicial, Tiempo de vuelo y Grosor: ").capitalize()
            if parametro in ("Coeficientes", "Punto inicial"): 
                try: 
                    print("Introduzca tres números reales, pulsando enter para cada uno: ")
                    a = float(input("a = "))
                    b = float(input("b = "))
                    c = float(input("c = "))
                except ValueError: # si no lo puede convertir a un float dará un error
                    print(f"{Dict_Parametros[parametro]} debe ser un número real. ") 
                else: # Cambiamos el parámetro especificado con el valor especificado
                    Dict_Parametros[parametro] = (a, b, c)
                    break
            elif parametro in ("Tiempo de vuelo", "Grosor"):
                try: 
                    valor = float(input("Introduce su valor: "))
                except ValueError: # si no lo puede convertir a un float dará un error. Si no es positivo dará un error
                    print(f"{Dict_Parametros[parametro]} debe ser un número real. ") 
                except valor <= 0: 
                    print(f"{Dict_Parametros[parametro]} debe ser un número positivo")
                else: 
                    Dict_Parametros[parametro] = valor
                    break
            else: 
                print("Ese parámetro no existe")
    elif opcion == "2": # imprime los parámetros
        for parametro, valor in Dict_Parametros.items():
            if type(valor) == int:
                print(f"{parametro} = {valor}")
            elif type(valor) == float:
                print(f"{parametro} = {valor}")
            else:
                print(parametro, "=", list([round(i, 3) for i in valor])) # hay que hacer esto porque son listas, no puedes :.3f a una lista
    elif opcion == "3":
        # obtenemos las variables de nuestro dicctionario
        params_usuario = Dict_Parametros["Coeficientes"]
        X0_usuario = Dict_Parametros["Punto inicial"]
        tiempo_vuelo = Dict_Parametros["Tiempo de vuelo"]
        grosor_usuario = Dict_Parametros["Grosor"]
        # resolvemos
        sol_full = s.solver(tmax=tiempo_vuelo, X0=X0_usuario, params=params_usuario, paso_max=0.01, grosor=grosor_usuario)
        # obtenemos los valores de x, y, z, t
        solx, soly, solz = sol_full.y
        tiempos = sol_full.t
        # representamos
        r.rep_lineas_color(tiempos, solx, soly, solz, X0=X0_usuario, params=params_usuario, grosor=0.1)
    elif opcion == "4":
        # obtenemos las variables de nuestro dicctionario
        params_usuario = Dict_Parametros["Coeficientes"]
        X0_usuario = Dict_Parametros["Punto inicial"]
        tiempo_vuelo = Dict_Parametros["Tiempo de vuelo"]
        grosor_usuario = Dict_Parametros["Grosor"]
        # resolvemos
        sol_full = s.solver(tmax=tiempo_vuelo, X0=X0_usuario, params=params_usuario, paso_max=0.01)
        # obtenemos los valores de x, y, z
        solx, soly, solz = sol_full.y
        # representamos
        r.rep_lineas(solx, soly, solz, X0=X0_usuario, params=params_usuario, grosor=grosor_usuario)
    elif opcion == "5":
        # obtenemos las variables de nuestro dicctionario
        params_usuario = Dict_Parametros["Coeficientes"]
        X0_usuario = Dict_Parametros["Punto inicial"]
        tiempo_vuelo = Dict_Parametros["Tiempo de vuelo"]
        # resolvemos
        sol_full = s.solver(tmax=tiempo_vuelo, X0=X0_usuario, params=params_usuario, paso_max=0.01)
        # obtenemos los valores de x, y, z, t
        solx, soly, solz = sol_full.y
        tiempos = sol_full.t
        # representamos
        r.rep_puntos(tiempos, solx, soly, solz, X0=X0_usuario, params=params_usuario)
    elif opcion == "6":
        # obtenemos las variables de nuestro dicctionario
        params_usuario = Dict_Parametros["Coeficientes"]
        X0_usuario = Dict_Parametros["Punto inicial"]
        # resolvemos. tomamos menos tiempo para que valla mejor
        sol_full = s.solver(tmax=100, X0=X0_usuario, params=params_usuario, paso_max=0.01)
        # obtenemos los valores de x, y, z
        solx, soly, solz = sol_full.y
        # pasamos a la función de representación interactiva
        r_sliders.rep_sliders(solx, soly, solz, init_X0=X0_usuario, init_params=params_usuario)
    elif opcion == "7":
        # obtenemos las variables de nuestro dicctionario
        params_usuario = Dict_Parametros["Coeficientes"]
        X0_usuario = Dict_Parametros["Punto inicial"]
        tiempo_vuelo = Dict_Parametros["Tiempo de vuelo"]
        grosor_usuario = Dict_Parametros["Grosor"]
        # resolvemos
        sol_full = s.solver(tmax=tiempo_vuelo, X0=X0_usuario, params=params_usuario, paso_max=0.01)
        # obtenemos los valores de x, y, z
        solx, soly, solz = sol_full.y
        # preguntamos por un nombre para el archivo
        nombre_usuario = str(input("Introduce un nombre para la animación (Solo el nombre sin .gif, evitando espacios) "))
        # pasamos a la función 
        r_animation.rep_ani(solx, soly, solz, X0=X0_usuario, params=params_usuario, nombre=nombre_usuario, grosor=grosor_usuario)
        print('La animación se ha guardado en el directorio donde se encuentran los scripts. Muchas gracias por guardarlo')
    elif opcion == "8":
        print("Programa cerrado")
        control_principal = False
    else:
        print("Número no reconocido")


