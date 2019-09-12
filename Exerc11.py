#ATIVIDADE PEDIDA: (Prof.Ronaldo)####################################################################################################################################################{
#CT0111 – Décima primeira da primeira etapa                                                                                                                                         
#Implementar o Gnome sort e imprimir os graficos conforme segue:                                                                                                                    
#                                                                                                                                                                                   
#   *Tamanho da lista de números x Tempo para ordenar pelo método - OBRIGATÓRIO!                                                                                                    
#   [Tamanho da lista x Quantidade de operações (Número de comparações)] - OPCIONAL!                                                                                                
#                                                                                                                                                                                   
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 100K, 200K, 400K, 500K, 1M, 2M. <-Devido ao algoritmo ter-se mostrado EXTREMAMENTE LENTO PARA O CASO DA LISTA RANDOMICA, A LISTA FOI DIMINUÍDA PARA ENTRADAS DE VALOR MENOR!                                                                         #
#####################################################################################################################################################################################}

#"Importação das devidas bibliotecas ;)"

import sys

import math

import random
from random import randint

import timeit

import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt

###############################################################################{
#"Declarações iniciais..."
mpl.use('Agg')
mpl.rc('axes', linewidth=2)
plt.style.use('_classic_test')
sys.setrecursionlimit(10**9)
###############################################################################}         

#"Segunda Função responsável pela criação do gráfico(x,y) para estudo do desempenho de algoritmo" *(Usada para criar o gráfico dos 3 casos apresentados juntos na mesma malha)
#Implementação do professor + implementação do aluno####################################################################################################{      
def desenhaGrafico2(x, y, yde, yce, file_name, label, label2, label3, file_title, line_color, line_color2, line_color3, line_color4, line_color5, line_color6, xl, yl):                                                                                               #
    fig = plt.figure(figsize=(20, 20))                                                                                                                                                                 
    ax = fig.add_subplot(111)                                                                                                                          
    ax.plot(x,y, color=line_color,linestyle = '-',linewidth=3,label = label)                           
    ax.plot(x,yde, color=line_color3,linestyle = '-',linewidth=2,label = label2)                     
    ax.plot(x,yce, color=line_color5,linestyle = '-',linewidth=1,label = label3)                                                                    

    plt.scatter(x[5],y[5], s=800,marker='s',facecolor='none',edgecolors= line_color, linewidths=1.5)
    plt.scatter(x[5],y[5], s=200,marker='x',facecolor=line_color2,edgecolors= line_color, linewidths=3)

    plt.scatter(x[5],yde[5], s=800,marker='o',facecolor='none',edgecolors= line_color3, linewidths=1.5)
    plt.scatter(x[5],yde[5], s=200,marker='x',facecolor=line_color4,edgecolors= line_color3, linewidths=3)

    plt.scatter(x[5],yce[5], s=800,marker='^',facecolor='none',edgecolors= line_color5, linewidths=1.5)
    plt.scatter(x[5],yce[5], s=200,marker='x',facecolor=line_color6,edgecolors= line_color5, linewidths=3) 
                                                                                                                                                                                                                                                                                            
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                              
    plt.ylabel(yl)                                                                                                                                                                                                                         
    plt.xlabel(xl)                                                                                                                                                                                                                         
    plt.title(file_title)                                                                                                                                                                                                            
    fig.savefig(file_name)                                                                                                                                                                                                          
########################################################################################################################################################}       

#"Função Gnome Sort"
#Implementação do aluno#########################################################################{
def gnomeSort(lista):                                                                                                                                                                                                                            
  pivot = 0
  num_iteracoes = 0
  
  lista_tam = len(lista)
  
  while pivot < lista_tam - 1:
    if lista[pivot] > lista[pivot + 1]:
      lista[pivot + 1], lista[pivot] = lista[pivot], lista[pivot + 1]
      num_iteracoes += 1
      
      if pivot > 0:
        pivot -= 2
        
    pivot += 1

  return num_iteracoes
################################################################################################}

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente ou em certa ordem específica(Para essa DÉCIMA PRIMEIRA ATIVIDADE será em ordem ALEATÓRIA) e retorna os devidos gráficos comparativos"
#O que estiver comentado no código da função abaixo foi usado para gerar os outros gráficos(Para os casos da lista ser DECRESCENTE ou CRESCENTE, os quais o aluno decidiu fazer apenas para fins acadêmicos).
#Implementação do aluno##########################################################################################################################################################################################################################################################################################################################################{
def cria_Graficos(lista_entrada):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #

  tempos_orden_Random = list()
  tempos_orden_Decresc = list()   
  tempos_orden_Cresc = list()

  num_iteracoes_Random = list()
  num_iteracoes_Decresc = list()   
  num_iteracoes_Cresc = list()

  j = 0
                                                                                                                                                                                                                                                                                                           
  for i in lista_entrada:                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                           
    #1) Lista Aleatória <- OBRIGATÓRIO(PEDIDO NA ATIVIDADE)                                                                                                                                                                                                                                                
    lista = list(range(0, i + 1))                                                                                                                                                                                                                                                                          
    random.shuffle(lista)
    tempos_orden_Random.append(timeit.timeit("gnomeSort({})".format(lista),setup="from __main__ import gnomeSort",number=1))
    num_iteracoes_Random.append(gnomeSort(lista))

    #2) Lista já ORDENADA em ordem DECRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO)                                                                                                                                                                                                                              
    lista = list(range(i,-1,-1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    tempos_orden_Decresc.append(timeit.timeit("gnomeSort({})".format(lista),setup="from __main__ import gnomeSort",number=1))
    num_iteracoes_Decresc.append(gnomeSort(lista))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #                                                                                                                                                                                                                                                                                                            #
    #3) Lista já ORDENADA em ordem CRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO)                                                                                                                                                                                                                               
    lista = list(range(0,i+1,1))
    tempos_orden_Cresc.append(timeit.timeit("gnomeSort({})".format(lista),setup="from __main__ import gnomeSort",number=1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    num_iteracoes_Cresc.append(gnomeSort(lista))

    j += 1
    print(">>>[",j,"]\n")#Isso serve para saber se cada elemento da "lista_teste" está sendo corretamente compilado!

  print(">>>Passou!\n")
                                                                                                                                                                                                                                                                                                  
  desenhaGrafico2(lista_entrada,tempos_orden_Random,tempos_orden_Decresc,tempos_orden_Cresc,"GraficoGnomeSort(Tamanho_Lista-X-Tempo_Ordenacoes).png", "Tempo(Lista->Aleatória[Gnome Sort])","Tempo(Lista->Decrescente[Gnome Sort])","Tempo(Lista->Crescente[Gnome Sort])",'(Gnome Sort - Listas: Aleatória/Decrescente/Crescente)Tamanho_Lista X Tempo_Ordenacoes','magenta','darkmagenta','cyan','darkcyan','red','darkred',"<Entradas/>","<Tempo-Saída/>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #                                                                                                                                                                                                                                                                                                           
  desenhaGrafico2(lista_entrada,num_iteracoes_Random,num_iteracoes_Decresc,num_iteracoes_Cresc,"GraficoGnomeSort(Tamanho_Lista-X-Numero_Iteracoes).png", "SWAPS(Lista->Aleatória[Gnome Sort])","SWAPS(Lista->Decrescente[Gnome Sort])","SWAPS(Lista->Crescente[Gnome Sort])",'(Gnome Sort - Listas: Aleatória/Decrescente/Crescente)Tamanho_Lista X SWAPS','magenta','darkmagenta','cyan','darkcyan','red','darkred',"<Entradas/>","<Tempo-Saída/>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #                                                                                                                                                                                                                                                                                                           
###################################################################################################################################################################################################################################################################################################################################################################}

#Inicialização da aplicação:
##########################################################################{
#lista_teste = [100000,200000,400000,500000,1000000,2000000]<-Para se ter ideia, levou mais de 1 Dia para rodar essa entrada no "Google Colabs" e ainda não havia compilado nem 4/6 do total direito!"

#################################################################################################
#Obs:.Essa foi a entrada que levou o menor TEMPO para mim,detalhe que ainda levou algumas horas!#
lista_teste = [10000,20000,30000,40000,50000,100000]                                            #
#################################################################################################

cria_Graficos(lista_teste)                                               
##########################################################################}
#############################
################                                                       
