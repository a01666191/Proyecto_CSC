from sympy import symbols, Eq, Point
from sympy.geometry import Circle, Ellipse, Parabola

# Definir los símbolos
x, y = symbols('x y')

# Punto para evaluar las secciones cónicas
punto = Point(3, 2)

# Definir las ecuaciones de las secciones cónicas
ecuacion_circulo = Eq(x**2 + y**2, 25)
ecuacion_elipse = Eq(x**2/9 + y**2/4, 1)
ecuacion_parabola = Eq(y, x**2)
ecuacion_hiperbola = Eq(x**2/16 - y**2/9, 1)

# Verificar si el punto pertenece a cada sección cónica
pertenece_circulo = ecuacion_circulo.subs({x: punto[0], y: punto[1]}).simplify()
pertenece_elipse = ecuacion_elipse.subs({x: punto[0], y: punto[1]}).simplify()
pertenece_parabola = ecuacion_parabola.subs({x: punto[0], y: punto[1]}).simplify()
pertenece_hiperbola = ecuacion_hiperbola.subs({x: punto[0], y: punto[1]}).simplify()

# Imprimir resultados
print(f"¿El punto {punto} pertenece al círculo?: {pertenece_circulo}")
print(f"¿El punto {punto} pertenece a la elipse?: {pertenece_elipse}")
print(f"¿El punto {punto} pertenece a la parábola?: {pertenece_parabola}")
print(f"¿El punto {punto} pertenece a la hipérbola?: {pertenece_hiperbola}")
