#Órbitas planetarias.A partir de la 2da ley de Kepler, escriba un programa que calcule la posición y velocidad en el afelio, dada la posición y velocidad en el perihelio

from math import *
G=6.67e-11
Ms=1.98e30
MT=5.97e24
RP=float(input("Digite el valor del radio 'RP'  en el  perihelio: "))
vP=float(input("Digite el valor de la velocidad  'vP' en el  perihelio: "))
a=1
b=-((2*G*Ms)/(RP*vP))
c=-((vP)**2-((2*G*Ms)/(RP)))
DISC=(b)**2-4*a*c
t=sqrt(DISC)
vA_1=(-b+t)/(2*a)
vA_2=(-b-t)/(2*a)
rA_1=(vP)*(RP)/(vA_1)
rA_2=(vP)*(RP)/(vA_2)
a1=(0.5)*(RP+rA_1)
a2=(0.5)*(RP+rA_2)
b1=sqrt((RP)*(rA_1))
b2=sqrt((RP)*(rA_2))

T1=(2*pi*a1*b1)/(RP*vP)
T2=(2*pi*a2*b2)/(RP*vP)

e1=(rA_1-RP)/(rA_1+RP)
e2=(rA_2-RP)/(rA_2+RP)

print("Los valores de la velocidad en el afelio 'vA_1', 'vA_2' son:")
print("vA_1, vA_2:", vA_1,vA_2)
print("Los valores del radio en el afelio 'rA_1', 'rA_2' son:")
print("rA_1, rA_2:", rA_1,rA_2)
print("Los valores del semi eje mayor 'a1', 'a2' son:")
print("a1, a2:", a1,a2)
print("Los valores del semi eje menor 'b1', 'b2' son:")
print("b1, b2:", b1,b2)
print("Los valores del periodo orbital 'T1', 'T2 son:")
print("T1, T2:", T1,T2)
print("Los valores de la  excentricidad 'e1', 'e2' son:")
print("e1, e2:", e1,e2)

