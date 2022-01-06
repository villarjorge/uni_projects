# Newton's method in the complex plane

Reused code in notebook form for creating the newton fractals. The code originaly comes from a newton optimizer that I made for another class. This was for a complex analysis class. The tex and pdf is the final project that was handed in. The images were drawn using matplotlib.pyplot and some of the math was handled with numpy. Whenever possible, numba was used to speed up calculations.

<img title="Fig 1" alt="A polynomial fractal" src="https://github.com/villarjorge/uni_projects/blob/main/newton_fractals/Newton%20rapshon%20fractal%205%20-%205000%20por%205000.png">
The resulting fractal for the polinomial $z^4 = 1$. The by the fundamental theorem of algebra the polinomial has four zeroes, each one represented with a color. 

<img title="Fig 1" alt="An inverse gamma fractal" src="https://github.com/villarjorge/uni_projects/blob/main/newton_fractals/N-R%20para%20funci%C3%B3n%20RGamma%20con%20m%C3%A1s%20raices%20general%20-%202000%20por%202000.png">
https://github.com/villarjorge/uni_projects/blob/main/newton_fractals/N-R%20para%20funci%C3%B3n%20RGamma%20con%20m%C3%A1s%20raices%20general%20-%202000%20por%202000.png

The resulting fractal for the inverse gamma function $\frac{1}{\Gamma(z)}$. The gamma function is the extension to the reals of the factorial $n!$. The usual definitions of the gamma function do not converge for complex numbers with real part less than zero, so an analytic continuation must be used. The analytic continuation of the gamma function tends to infinity on the negative integers, which means that its multiplicative inverse has zeroes in the same places. The computation was handeled <a href = "https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.rgamma.html?highlight=rgamma#scipy.special.rgamma">by the scipy module</a>. Around 5 zeroes where considered when drawing the fractal.

# Método the Newton en el plano complejo

Codigo reutilizado en un archivo notebook para crear fractales de Newton. El código fue tomado de un optimizador con Newton que creé para otra clase. Este projecto era para una clase de variable compleja. El archivo tex y pdf son los que se entregaron finalmente. Las imagenes fueron creadas con matplotlib.pyplot y parte de la matematica se gestionó con numpy. Cuando fué posible se acceleró la computiacion precompilando funciones con el módulo numba.

<img title="Fig 1" alt="Fractal polinómico" src="https://github.com/villarjorge/uni_projects/blob/main/newton_fractals/Newton%20rapshon%20fractal%205%20-%205000%20por%205000.png">

El fractal resulante para el polinomio $z^4 = 1$. Por el teorema fundamental del algebra tiene cuatro raizes, cada una representada por un color. 

<img title="Fig 1" alt="An inverse gamma fractal" src="https://github.com/villarjorge/uni_projects/blob/main/newton_fractals/N-R%20para%20funci%C3%B3n%20RGamma%20con%20m%C3%A1s%20raices%20general%20-%202000%20por%202000.png">
https://github.com/villarjorge/uni_projects/blob/main/newton_fractals/N-R%20para%20funci%C3%B3n%20RGamma%20con%20m%C3%A1s%20raices%20general%20-%202000%20por%202000.png

El fractal resultante para la función inversa de la función Gamma $\frac{1}{\Gamma(z)}$. La función gamma es la extensión a los reales del factorial $n!$. Las definiciones normales de la función gamma no convergen para números complejos de parte real negativa, por lo que se ha utilizado una continuación analítica. Esta continuación tiende a infinito en los numeros naturales negativos, por lo que su inverso multiplicativo tiende a cero en esos puntos. La computación de la función se ha realizado con <a href = "https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.rgamma.html?highlight=rgamma#scipy.special.rgamma">el modulo scipy</a>. Se han utilizado unos cinco colores al dibujar el fractal.

