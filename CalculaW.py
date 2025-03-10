import math


def Metodo1(vReal, vSuavizado):
    dividendo = math.fabs(vReal - vSuavizado)
    divisor = math.fabs(vReal) + math.fabs(vSuavizado)
    return dividendo / divisor


def Metodo2(vReal, vSuavizado, w, x):
    return w + x * (vReal - vSuavizado)