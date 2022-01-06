# -*- coding: utf-8 -*-
"""
Creado: 18/01/2021

Autor: Jorge San José

ESTE PROGRAMA NECESITA DE "osciladores_funciones"
Este programa modela un oscilador amortiguado. Proporciona:
    -La gráfica Tiempo-Posición, Tiempo-velocidad y Tiempo-aceleración del mismo
    -La gráfica Tiempo posición cuando existe una fuerza periódica sinusoidal
Además permite ajustar parámetros para obtener una oscilación que vuelve al equilibrio lo más rápido posible (Sin fuerza externa) y
para que se dé el fenómeno de resonancia (Con fuerza externa)
"""

import numpy as np
import matplotlib.pyplot as plt
# Necesitamos las funciones
from osciladores_funciones import oscilador_amortiguado, oscilador_amortiguado_fuerza_externa

tiempo = np.linspace(0, 20, 200)
parametros = {"Masa":1, "Constante de fuerza":10, "Coeficiente de amortiguación":0.1, "Amplitud inicial":1, "Fuerza periódica":0.1, "Frecuencia angular":2} # Creamos un diccionario con valores predeterminados para trabajar con casos sistemáticamente
control_principal = True # Esta será la variable controla el bucle while principal del programa. Cuando sea igual a cero el programa continuará ejecutandose y cuando sea igual a uno el programa se cerrará
print("*"*29)
print("* OSCILACIONES AMORTIGUADAS *")
print("*"*29)
opciones = "\nOpciones: \n      0. Mostrar opciones.\n      1. Cambiar parámetros de masa, constante de fuerza, coeficiente de amortiguación, amplitud inicial, valor inicial de la fuerza periódica o frecuencia angular de la fuerza periódica.\n      2. Imprimir valores actuales.\n      3. Crear gráficas (Sin fuerza externa). \n      4. Ajustar coeficiente de amortiguación para obtener amortiguamiento crítico.\n      5. Crear gráficas (Con fuerza externa). \n      6. Ajustar frecuencia de la fuerza para obtener resonancia. \n      7. Salir."
print(opciones)

while control_principal:
    opcion = input("Para selecionar una opción escriba su número correspondiente: (Introducir cero para volver a mostrar las opciones) ")

    if opcion == "0": # Esta opción muestra las opciones de nuevo
        print(opciones)
    elif opcion == "1": # Esto es lo que permite cambiar un valor. También es donde gestionamos las entradas no validas
        while True: # si el parametro no existe no dejaremos al usuario pasar al bucle, seguiremos preguntando hasta que nos de un parámetro que exista
            parametro = input("Introduce el parámetro a cambiar. Los parámetros son: Masa, Constante de fuerza, Coeficiente de amortiguación, Amplitud inicial, Fuerza periódica (su valor inicial) y Frecuencia angular (De la fuerza periodica): ").capitalize()
            if parametro in ("Masa", "Constante de fuerza", "Coeficiente de amortiguación"): 
                try: 
                    valor = float(input("Introduce su valor: "))
                except ValueError: # si no lo puede convertir a un float dará un error
                    print(f"{parametros[parametro]} debe ser un número real. ") 
                except valor <= 0: 
                    print(f"{parametros[parametro]} debe ser un número positivo")
                else: # Cambiamos el parámetro especificado con el valor especificado
                    parametros[parametro] = valor
                    break
            elif parametro in ("Amplitud inicial", "Fuerza periódica", "Frecuencia angular"):
                try: 
                    valor = float(input("Introduce su valor: "))
                except ValueError: # si no lo puede convertir a un float dará un error, estos si pueden ser negativos
                    print(f"{parametros[parametro]} debe ser un número real. ") 
                else: 
                    parametros[parametro] = valor
                    break
            else: 
                print("Ese parámetro no existe")
    elif opcion == "2":
        for parametro, valor in parametros.items():
            print(f"{parametro} = {valor}")
    elif opcion == "3":
        pos_vel_ac = ("Posición", "Velocidad", "Acceleración") # Para ahorrar lineas utilizaremos esta lista, accediendo a ella en cada título de cada nueva gráfica
        unidades = ("x (metros)", "v (m/s)", "a (m/s/s)")
        # Tomamos las variables de nuesto diccionario
        masa =  parametros["Masa"]
        c_f = parametros["Constante de fuerza"]
        c_a = parametros["Coeficiente de amortiguación"]
        A_ini = parametros["Amplitud inicial"]
        # Llamamos a la función con esos valores
        valores_x_v_a = oscilador_amortiguado(tiempo, masa, c_f, c_a, A_ini)
        # Calculamos el periodo 
        T = 2*np.pi*np.sqrt(masa/c_f)

        # Creamos las tres gráficas
        for i in range(len(valores_x_v_a)-1):
            plt.plot(tiempo, valores_x_v_a[i])
            plt.title(rf"{pos_vel_ac[i]} para $m$={masa}, $k$={c_f}, $c$={c_a}, $A_0$={A_ini}")
            plt.ylabel(unidades[i])
            plt.xlabel("t (segundos)")
            # Esto lo utilizaremos para colocar una etiqueta
            maximo = np.max(valores_x_v_a[i])
            plt.annotate(f"Periodo = {T}", (0, A_ini), xytext=(10, maximo))
            plt.show()
        print("Gráficas creadas")
        # Decimos como evolucionará el sistema en función del coeficiente de amortiguación, se calcula al llamar a la función
        r_a = valores_x_v_a[3]
        if parametros["Coeficiente de amortiguación"] > 2*np.sqrt(parametros["Masa"]*parametros["Constante de fuerza"]): # Te dice como evolucionará el sistema. Es equivalente a decir r_a > 0
            print(f"El ratio de amortiguación es {r_a}. Se da el fenómeno de  sobreamortiguamiento, el sistema no oscila, si no que decae exponencialmente.")
        elif parametros["Coeficiente de amortiguación"] == 2*np.sqrt(parametros["Masa"]*parametros["Constante de fuerza"]):
            print(f"El ratio de amortiguación es {r_a}. Se da el fenómeno de amortiguamiento crítico, el sistema vuelve a al equilibrio lo más rápido posible") #Es equivalente a decir r_a == 0
        elif parametros["Coeficiente de amortiguación"] < 2*np.sqrt(parametros["Masa"]*parametros["Constante de fuerza"]):
            print(f"El ratio de amortiguación es {r_a}. Se da el fenómeno de  subamortiguamiento, el sistema oscila hasta alcanzar el equilibrio") # Es equivalente a decir r_a < 0
        else:
            print("Algo a ido mal, el ratio no es un número")
    elif opcion == "4": # El amortiguamiento crítico se da cuando el coeficiente de amortiguación es dos veces la raiz de la masa por la constante de fuerza. 
        parametros["Coeficiente de amortiguación"] = 2*np.sqrt(parametros["Masa"]*parametros["Constante de fuerza"])
        c_a = parametros["Coeficiente de amortiguación"]
        print(f"Coeficiente de amortiguación ajustado a {c_a}")
    elif opcion == "5":
        # Tomamos los valores del diccionario
        masa =  parametros["Masa"]
        c_f = parametros["Constante de fuerza"]
        c_a = parametros["Coeficiente de amortiguación"]
        A_ini = parametros["Amplitud inicial"]
        F_ini = parametros["Fuerza periódica"]
        f_ang = parametros["Frecuencia angular"]
        # Llamamos a la función
        valores_x = oscilador_amortiguado_fuerza_externa(tiempo, masa, c_f, c_a, A_ini, F_ini, f_ang)[0]
        # Creamos la gráfica de posición, resulta ser una sinusoidal
        plt.plot(tiempo, valores_x)
        plt.title(rf"Posición con fuerza externa para $m$={masa}, $k$={c_f}, $c$={c_a}, $A_0$={A_ini}")
        plt.ylabel("x (metros)")
        plt.xlabel("t (segundos)")
        plt.show()
        # Creamos la gráfica de frecuencias angulares contra frecuencias iniciales 
        frecuencias = np.linspace(1, 20, 200)
        amplitudes_iniciales = oscilador_amortiguado_fuerza_externa(0, masa, c_f, c_a, A_ini, F_ini, frecuencias)[0]
        plt.plot(frecuencias, amplitudes_iniciales)
        plt.title(rf"Amplitudes para $m$={masa}, $k$={c_f}, $c$={c_a}, $A_0$={A_ini}")
        plt.ylabel("Amplitudes iniciales (metros)")
        plt.xlabel("Frecuencias angulares de la fuerza (segundos)")
        plt.show()
        print("Gráficas creadas")
    elif opcion == "6": # La resonancia se da cuando la frecuencia de la fuerza está cerca de la fecuencia natural del sistema.
        parametros["Frecuencia angular"] = np.sqrt(parametros["Constante de fuerza"]/parametros["Masa"]) + 0.001
        f_a = parametros["Frecuencia angular"]
        print(f"Frecuencia angular ajustada a {f_a}")
        parametros["Coeficiente de amortiguación"] = 0.01
        c_a = parametros["Coeficiente de amortiguación"]
        print(f"Coeficiente de amortiguación ajustado a {c_a}")
    elif opcion == "7":
        print("Programa cerrado")
        control_principal = False
    else:
        print("Número no reconocido")
