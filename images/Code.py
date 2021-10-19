import math
import numpy as np
import matplotlib.pyplot as plt
import random
import pandas as pd

print('#'*40,'TASK 1','#'*40)
###1. Realice un función recursiva que permita determinar si un número entero positivo pertenece a la serie de Fibonacci. 
# A function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):
 
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    condition=isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
    if condition:
         print (n,"is a Fibonacci Number")
    else:
         print (n,"is a not Fibonacci Number ")
isFibonacci(4)
isFibonacci(5)

print('#'*40,'TASK 2','#'*40)
###2. Realice un función recursiva que permita determinar si un número entero positivo
##Function to check if  its square root is an integer
def isSquare(x):
    s=math.sqrt(x)
    if s.is_integer():
        print (x,"belongs to the square series")
    else :
        print(x,"Is not Square Number")
isSquare(25)
isSquare(27)

print('#'*40,'TASK 3','#'*40)
###3. Escriba una función recursiva que devuelva el valor de la serie de Taylor de e x para un número real dado x y un número máximo de términos en la serie N.
power = 1.0
factorial= 1.0
def Taylor(x, n):
     
    global power, factorial
    
    if (n == 0): # Base condition
        return 1
 
    
    r = Taylor(x, n - 1) #### Recursive call
 
    power = power * x  # Update the power of x
 
    factorial = factorial * n  ### Factorial
 
    return (r + power / factorial)
print(Taylor(4, 4))

print('#'*40,'TASK 4','#'*40)
###4. Escriba una función recursiva que devuelva el valor de la serie de Taylor del seno (sen(x)) para un número real dado x y un número máximo de términos en la serie N.
def calcFac(x):
    if x == 1 or x == 0: return 1
    val = 1
    for i in range(2, x+1):
        val = val * i
    return val

def sinTaylor(angle, terms):
    mult = 1
    if terms % 2 == 0: mult = -1

    power = 2*terms - 1
    val = angle ** power
    val = mult * val/calcFac(power)

    if terms == 1: 
        return val
    else: 
        return val + sinTaylor(angle, terms - 1)
print(sinTaylor(4,4))


print('#'*40,'TASK 5','#'*40)
###5. Escriba una función recursiva que devuelva el valor de la serie de Taylor del coseno (cos(x)) para un número real dado x y un número máximo de términos en la serie N. 

def cosTaylor(angle, terms):
    mult = 1
    if terms % 2 == 0: mult = -1

    power = 2*terms - 2
    val = angle ** power
    val = mult * val/calcFac(power)

    if terms == 1: 
        return 1
    else: 
        return val + cosTaylor(angle, terms - 1)

print(cosTaylor(4,4))



print('#'*40,'TASK 6','#'*40)
###6. A partir de la función realizada en el punto 3, realice una curva que presente el valor estimado de e x para valores de N desde 10 hasta 1000 con pasos de 10; realice otra curva que presente el error absoluto de la serie para los mismos valores estimados de N (10:10:1000); realice otra curva que presente el error relativo de la serie para los mismos
#valores estimados de N (10:10:1000). Tome como valor “verdadero” (más preciso) el que devuelve la función nativa e x del lenguaje de programación. 
def curve(x):
    Values=[]
    for n in range(10,1000,10):
        m=Taylor(x, n)
        Values.append(m)
    plt.plot(list(range(10,1000,10)),Values)
    plt.show()
curve(4)
print('PRINTED')

print('#'*40,'TASK 7','#'*40)
###7. Repita el punto 6 para la función realizada en el punto 4 (sen(x))
def curve(x):
    Values=[]
    for n in range(10,1000,10):
        m=sinTaylor(x, n)
        Values.append(m)
    plt.plot(list(range(10,1000,10)),Values)
    plt.show()
curve(4)
print('PRINTED')

# print('#'*40,'TASK 8','#'*40)
# ###8. Repita el punto 6 para la función realizada en el punto 5 (cos(x))
def curve(x):
    Values=[]
    for n in range(10,1000,10):
        m=cosTaylor(x,n)
        Values.append(m)
    plt.plot(list(range(10,1000,10)),Values)
    plt.show()
curve(4)
print('PRINTED')


print('#'*40,'TASK 9','#'*40)
###9. Realice un programa que genere 1000 número aleatorios enteros entre -10 y 10 y los guarde un archivo binario con formato de 16 bits (int16). El archivo se debe llamar FileBinInt16.bin


np.random.seed(1) # seed random number generator
values = np.random.randint(-10, 10, 1000) # generate some integers
values = values.astype('int16')
values=list(values)
import pickle
output_file = open("FileBinInt16.bin", "wb")
pickle.dump(values, output_file) # converts array to binary and writes to output
output_file.close()
print('PRINTED')
 


print('#'*40,'TASK 10','#'*40)
###10. Realice un programa que lea los datos guardados en el archivo creado en el punto 9 y grafique el histograma correspondiente usando 30 casillas (30 bins). 
output_file = open("FileBinInt16.bin", "rb")
numbers = pickle.load(output_file) # Reads the binary and converts back to list
print(len(numbers))
output_file.close()


plt.hist(numbers, bins=30)  # density=False would make counts
plt.ylabel('Frequency')
plt.xlabel('Data');
plt.show()
print('PRINTED')

print('#'*40,'TASK 11','#'*40)
###11. Realice un programa que genere 1000 número aleatorios reales entre -1 y 1 y los guarde un archivo binario con formato de 64 bits (double). El archivo se debe llamar FileBinDouble.bin.
np.random.seed(1) # seed random number generator
values = np.random.rand(-1, 1, 1000) # generate some integers
values = values.astype('int64')
values=list(values)
output_file = open("FileBinDouble.bin", "wb")
pickle.dump(values, output_file) # converts array to binary and writes to output
output_file.close()
print('PRINTED')



print('#'*40,'TASK 12','#'*40)
###12. Realice un programa que lea los datos guardados en el archivo creado en el punto 11 y grafique el histograma correspondiente usando 30 casillas (30 bins). En el archivo binario File-214.bin se encuentran una serie de números enteros sin signo (unsigned), cada uno almacenado en 32 bits. El promedio de todos los datos es: 64023.8381
output_file = open("FileBinDouble.bin", "rb")
numbers = pickle.load(output_file) # Reads the binary and converts back to list
print(len(numbers))
output_file.close()

plt.hist(numbers, bins=30)  # density=False would make counts
plt.ylabel('Frequency')
plt.xlabel('Data');
plt.show()
print('PRINTED')

print('#'*40,'TASK 13','#'*40)
###13. Realice un programa que lea adecuadamente todos los datos de este archivo y comprueba el valor promedio de todos los datos. 
print(np.mean(numbers))

print('#'*40,'TASK 14','#'*40)
###14. A partir de los datos leídos de en el punto 13, realice un programa que permita determinar el número de datos que pertenecen a la serie de Fibonacci y escriba el número total de datos que pertenecen a esta serie (utilice la función realizada en el punto 1). 
fib_list=[]
for num in numbers:
    if isPerfectSquare(5*num*num + 4) or isPerfectSquare(5*num*num - 4):
        fib_list.append(num)
print(len(fib_list))
# print(fib_list)

print('#'*40,'TASK 15','#'*40)
###15. A partir de los datos leídos de en el punto 13, realice un programa que permita determinar el número de datos que pertenecen a la serie cuadrada y escriba el número total de datos que pertenecen a esta serie (utilice la función realizada en el punto 2)
squre_list=[]
for num in numbers:
    
    if num >=0 and math.sqrt(num).is_integer() :
        squre_list.append(num)
print(len(squre_list))
# print(squre_list)




















































