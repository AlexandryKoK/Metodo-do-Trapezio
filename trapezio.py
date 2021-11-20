import numpy as np
import math
import matplotlib.pyplot as plt
import sys


#Integracao Numerica (Metodo do Trapezio)




def placa(R,x):
    return np.sqrt(R**2 - x**2)

def placaxy(R,x):
    return x*np.sqrt(R**2 - x**2)

x = np.zeros((1, 10000000))

def integral(a,b,n):
    h = (float)(b-a)/n
    soma =0
    somaxy = 0
    for i in range(0,n):
        x[0][i] = a + i*h
        soma = soma + placa(50,x[0][i])
    integral = h/2*(placa(50,a) + placa(50,b) + 2*soma)
    return integral

# massa = densidade(rho) * area
def massa(rho):
    area = integral(-50,50,100000)
    massa = rho * area
    return massa

def integralxy(a,b,n):
    h = (float)(b-a)/n
    soma =0
    somaxy = 0
    for i in range(0,n):
        x[0][i] = a + i*h
        soma = soma + placaxy(50,x[0][i])
    integral = h/2*(placaxy(50,a) + placaxy(50,b) + 2*soma)
    return integral

def cm(rho):
    cmx = rho*integralxy(-50,50,1000) / massa(rho)
    #print(int(cmx))
    cmy = rho*integralxy(0,50,1000) / massa(rho)
    #print(cmy)
    raio = [round(cmx,5),round(cmy,5)]
    return raio

print(cm(3.5))


