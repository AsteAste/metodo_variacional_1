import numpy as np 
import matplotlib.pyplot 
import scipy as sp  

#Constantes universais 

h_barra = 1.0545718e-34 # Constante de Planck Reduzida
e_0 = 8.854187817e-12  # Permissividade do vácuo 
e = 1.60217662e-19  # Carga elétrica
m = 9.10938356e-31 # Massa do elétron 
r_0 = 5.2917721067e-11 # Raio de Bohr
 

#Definindo o Hamiltoniano 

#Definindo a energia potencial para o átomo de Hidrogênio 

def V(r):
    - (e**2)/(4* np.pi * e_0 * x)
    return 

# Definindo o Laplaciano do sistema (Derivada segunda da função de onda)
def  laplaciano(r, psi, dr):
   d2_psi = np.gradient(np.gradiente(r,psi,dr)
   return d2_psi

#Definindo a função tentativa do sistema
def psi_trial(r, a)
     a * np.ex(-a * r**2 )
    return psi_trial 



# Definindo a energia cinética do sistema


# Definindo o Hamiltoniano


# Plotando o gráfico da função trial e exibindo a energia fundamental do sistema