from scipy.optimize import fsolve
from scipy.misc import derivative
import random
#Definimos la funcion f(x) y g(x)
def f(x):
    return 2*x**3-3*x**2+4*x-6
def g(x):
    return x**4-5*x**3+5*x**2+12
#Definimos la funcion que nos calcula la altura del trapecio
#toma los dos puntos, los divide en el numero de trapecios
#y retorna un float con el resultado
def h(a,b,n):
    numerador = float(b-a)
    denominador = float(n)
    return float(numerador/denominador)
#Definimos la h para aplicarla a la formula final
def h_sobre(h):
    return float(h/2)
#funcion que calculara la sumatoria de areas evaluadas en la funcion
#es decir sumatoria de f(a+kh) desde k=1 hasta k-1
#retorna una lista con todos los calculos de la sumatoria y 
# el ultimo dato de la lista es la suma de estos.
#ui es la variable para saber que area se esta buscando si de la funcion
#1 o funcion 2, estas serian f(x) y g(x) respectivamente.
def calcular_area(n,ui):
    aData = []
    #este es el h con el que se multiplicara el k
    h_trapecios = h(resultado,resultado2,n)
    if ui ==1:
        for k in range(1,n):
            #recorremos y metemos dentro de la lista la funcion evaluada
            # en el punto a+kh
            aData.append(f(float(resultado)+(float(k)*h_trapecios)))
        aData.append(sum(aData))
    if ui ==2:
        for k in range(1,n):
            aData.append(g(float(resultado)+(float(k)*h_trapecios)))
        aData.append(sum(aData))
    return aData
#Definimos la funcion general que es 
# h_sobre*((f(a)+f(b)+datos_retornados_de_calcular_area*2)
def ecuacion(resultado,resultado2,h_final,aData,ui):
    if ui ==1:
        area = h_final*(f(resultado)+(2*(aData[-1]))+f(resultado2))
    if ui == 2:
        area = h_final*(g(resultado)+(2*(aData[-1]))+g(resultado2))
    return area
#Definimos la funcion error que nos entrega el error del metodo
def error(resultado2,resultado,ui):
    #utilizo el metodo derivate de la libreria scipy que evalua la derivada
    #en un punto, en este caso la formula del error nos permite evaluar
    #la derivada en el punto [a,b] por ende entre [2.08,5.59] por ende elegi
    #los puntos 3 y 4 que estan en el intervalo.
    #la funcion derivate recibe como parametro 
    #derivate(funcion,x0,n=numero de orden de la derivada)
    ran1 = derivative(f,3,n=2)
    ran2 = derivative(g,4,n=2)
    if ui ==1:
        #calculamos el error con respecto a la formula
        res = (ran1*(resultado2-resultado)**3/12)/n_trapecios**2
    if ui ==2:
        res = (ran2*(resultado2-resultado)**3/12)/n_trapecios**2
    return res
#Funcion BuscaInterseccion que buscara la interseccion
#entre 2 funciones
#Recibe como parametro dos funciones y una x inicial(estimado)
#entonces la funcion fsolve de scipy busca y devuelve
#las raices de f(x) - g(x) = 0
#es decir f(x) = g(x)
#       f(x) - g(x) = 0
#    resultado(x) = f(x) - g(x)
#busca las raices de la funcion resultado que son las
#intersecciones de las funciones
def BuscaInterseccion(fun1,fun2,x0):
    return fsolve(lambda x : fun1(x) - fun2(x),x0)
#Guardamos resultado, redondeamos con 4 digitos y imprimimos
resultado = round(BuscaInterseccion(f,g,0.0),4)
resultado2 = round(BuscaInterseccion(f,g,5.0),4)
n_trapecios = 4
h_final = h_sobre(h(resultado,resultado2,n_trapecios))
#Area para f(x)
aData1 = calcular_area(n_trapecios,1)
area1 = ecuacion(resultado,resultado2,h_final,aData1,1)
error1 = error(resultado2,resultado,1)
#Area para g(x)
aData2 = calcular_area(n_trapecios,2)
area2 = ecuacion(resultado,resultado2,h_final,aData2,2)
error2 = error(resultado2,resultado,2)
#Como con este metodo no es posible medir el area 
#para la cruza entre curvas, lo unico que habria que hacer es 
#restar las areas que dan cada curva por separado 
#en el intervalo [a,b]
print "Intersecciones entre las funciones f(x) y g(x)"
print "x1:",resultado
print "x2:",resultado2
print "Area de cada funcion f(x) y g(x)"
print "Area f(x)",area1-error1
print "Area2 g(x)",area2-error2
print "Area total aproximada entre las curvas f(x) y g(x) es"
print  round((area1-error1)-(area2-error2),4)
print



