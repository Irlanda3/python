msg = ("Hello World")


print(msg)
print("rat")
# shift + enter para correrlo y alparecer usa python 3.7 con jupiter
# to change python version go to the upper bar and choose version
# otra cosa que hice fue poner py -3 en la terminal para cambiar

print("hola")
2+3
#shift + ctrl +p

x = 2
x = 5
x = 7

# shift+alt+f para identar

# type format document into the window shift+crtl+p para identar
#------------
#intale ext code runner para correr y ver resultados del programa en terminal
#ctrl+alt+n para run y ver lo que imprime

#puedo usar el siguiente comando en la terminal:
#conda activate base
#MetroStateToken es el token para entrar a grupo de universidad
#Your new API Token: 6a45b93581624d019bf73f55a86b834c
#raton35@ es mi contrasenia para la clase
#THE FOLLOWING CODE IS TO RUN CELLS 
#%% 
msg = "Hello Word"

print = msg


#%%
'''
class 8-27-2019
henc function. input: x as a float, v as an integer

list
ndaarray
string
'''
9.4-9.0-0.4

x=2.1
type(x)

y=7
type(y) 

str_1 = "Hello world"
type(str_1)

z=(1,2)
type(z)

a=[1,2]
type(a)

b=2+3j
type(b)

#tengo que decir: from math import sqrt

from math import *
from cmath import *
print(sqrt(2))

x1=( 4 + sqrt(16-4*1*7))/2
x2=( 4 - sqrt(16-4*1*7))/2


#%%
#para importar de una manera especifca para poder usar despues
import math as m
import cmath as cmath

m.sqrt(2)
cm.sqrt(2)

#%%
expand(-(x-2)**2+3)


#%%
from sympy import exp, symbols
t = symbols('t')
f = exp(t)
f.series(t, 0, 4)
#package for nice eqtions; math jax
#vscode-okpy to grade assignments

#%%
#use the following code to output equations in LaTex format
from sympy.interactive import printing
printing.init_printing(use_latex = True)

x = 2
x^2 + x + 2
#%%
#class 8-29-19

F = -40
C = (5.0 / 9.0)*(F -32.0) 
F = (5.0 / 9.0)*(F - 32.0); print("{C:5.1f} {F:5.1f}".format(C=C,F=F))

#try while loops
#while F <=212 compute c and then print c and f. increment f by 8
'''
if i do not use a increment  the while loop will run forever and will need to stop the program
es necesario el c=c por que dice cuando veas c es igual a celcius
'''
F = -40
while F <= 212:
    C = (5.0 / 9.0)*(F -32.0)
    print("{C:5.1f} {F:5.1f}".format(C=C,F=F))
    F = F + 8

#%%
#class 8-29-19
F = -40
while F <= 212:
    C = (5.0 / 9.0)*(F -32.0)
    print("{C:5.1f} {F:5.1f}".format(C=C,F=F), end=", ")
    F = F + 8


#%%
#lab print a list of endponts

#let n = 10  and the interval be[0,10]

#print a multiplication table
# print() or print("\n")

num = 1
while num <= 9:
    print(1 * num, end = " ")
    num = num + 1
    num2 = 2
    num2 = num 
    print("\n")
    print(num2*2)
    num2+=1
    
    #print(2 * num, end = " ")

    


#%%
'''  LAB 01 PART B  08/09/19
la tabla de dos 1x1=1,1x2=2,1x3=3
                2x1=2,2x2=4,2x3=6
                3x1=3,3x2=6,3x3=9
temp va  aser la tabla osea el mismo en una iteracion
'''
num = 1
temp = 1
temp2 = 2
temp3 = 3
temp4 = 4
while num <= 9:
    
    print(temp * num," ")# put a space on the next line.       
    print(" ",temp2 * num)#second line of code
    print("   ", temp3 * num)#tercera line
    print("    ", temp4 * num)
    print("     ", 5 * num)
    print("      ", 6 * num)
    print("       ", 7 * num)
    print("        ", 8 * num)
    print("         ", 9 * num)
    num = num + 1 
   

#%%
#SEPTEMBER 3, 2019
''' in this problem we will explore different ways to produce lists of equallay spaced nuumbers
.For each method create a list of floats from zero to one with spacing of one-tenth and print
 put each value in the list using 16 digist behibd the decimal

 a. while loop
 b. for loop
 c. linspace from numpy

 '''
from numpy import linspace

#vamos a cambiar un ejemplo de clase multiplication table:

n = 9
j = 1

for j in range(10):#range nos da una lista de numeros del 0 al 9
    k = 1
    for k in range(10):
        print("{r:2d}".format(r=j*k, end = " "))
        k += 1
    print()
    j += 1


    #####my table using for loops***

    N = range(1,10)
    for j in N:
        for k in N:
            print(j*k, end = " ")
        print()

        # y si quieres un formato bonito entonces:
        print("{r:2d}".format(r=j*k, end = " "))









#%%
#9/3/2019
a = -1.0
b =5.0
n = 17
delta = (b-a)/n
k = 0
while k <=n:  #while loops son buenos para unknown repetitions
    print(a+k*delta)
    k = k+1

    #now use a for loop

    for k in range(n+1):
        print(a+k*delta)