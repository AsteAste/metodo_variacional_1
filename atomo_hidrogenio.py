import numpy as np 
import matplotlib.pyplot 
import scipy as sp  
import random
import time 

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
#def  laplaciano(r, psi, dr):
  # d2_psi = np.gradient(np.gradiente(r,psi,dr)
 #  return d2_psi




#Definindo a função tentativa do sistema
#def psi_trial(r, a)
 #    a * np.ex(-a * r**2 )
 #   return psi_trial 


# Definindo a plotagem dos gráficos















# Plotagem dos gráficos


def plotagem(r, todos_psi, D, incluir_V=False, V= None, escala_V=1):
  
  # Esse método contém várias formas de plotar o psi e o potencial do sistema
  # r: As coordenadas da grade
  # d: o número de eixos no sistema
  #incluir V: Se deseja plotar o potencial ou não
  # incluir_V: O potencial a ser plotado, se aplicável
  #escala V: A quantidade para escalar a função de onda ao plotá-la com o potencial
 
  #  Para o sistema 1D plota-se uma linha

  if D == 1:

    # O número de estados de psi a serem plotados
    num_states = len(all_psi)



 






  elif  D ==2: 

      if incluir_V:




# Compute 
        



# A derivada da Matriz de segunda ordem usando diferenças finitas

global DEV2 


def normalizacao(psi: np.ndarray, dr: float) -> np.ndarray

  # Normaliza a função de onda psi, primeiro ele vai pegar uma função não-normalizada, e retornar a função normalizada
  # psi: A função de onda a ser normalizada
  # dr: O espaçamento da grade (tamanho) no sistema 
  # return: A função de onda normalizada psi
  
  #Calculando a normalização #sum é usado para somar todos os elementos do array resultante de psi * psi
  # Isso calcula a integral discreta da densidade de probabilidade ao longo de todas as posições representados no array
  # dr é o espaçamento da grade, que é usado para converter a soma em uma integral, multiplicar a soma pela diferencial dr
  # Ajusta a soma para representar a integral contínua da densidade de probabilidade 



   norm = (psi * psi).sum() * dr
   
   # A função mostrada é a densidade de probabilidade, que é a função de onda ao quadrado
  
   norma_psi = psi / np.sqrt(norm) # Normaliza a função de onda psi
   return norma_psi 


def energia(psi: np.ndarray, V: np.ndarray, dr: float) -> float:
  

   # Calcular o auto valor da energia para uma função de onda dada psi em um sistema com potencial V 
   # psi: A função de onda do sistema
   # V: O potencial do sistema
   # dr: O espaçamento da grade no sistema
   # return: Retorna o auto valor da energia E 


   # 
  
   # Calcula a energia cinética do sistema 
   # DEV2 A derivada da Matriz de segunda ordem usando diferenças finitas
   # 
   