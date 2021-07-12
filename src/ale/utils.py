import math
# Escribir una funcion que basado en el radio:
#  calcule la sup de un circulo
#  calcule la circunferencia
#  calcule la sup de una esfera
#  calcule el vol de una esfera

def calcularCircunferencia(radio):
    """
    calcularCircunferencia() -> float

    radio -- radio is in float
    """

    circunferencia = math.pi * 2 * radio

    return circunferencia

def sumatoria(x):
    resultado = (x * (x + 1)) / 2
    return resultado


def calVolumenParalelepipedo(x, y, z):
    # global resultado
    resultado = x * y * z
    return resultado

# Esto sera una constante
complex_zero = {0, 0}


def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero


def useless(func):
    #inner functions
    def other(x):
        x = x * 2
        return func(x)
    return other

def factorial_decorator(func):
    def checker(x):
        if type(x) == int and x >= 0:
            return func(x)
        else:
            raise TypeError("Error, no se puede realizar operacion")
    return checker

#@useless #useless(factorial(4)) <- #reemaplaza en todas las a factorial
@factorial_decorator
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def division(x, y):
    assert y > 0
    return x / y
