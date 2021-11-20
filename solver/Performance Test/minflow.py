# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:08:45 2021

@author: Michael
"""

#Desde: Salazar, ingenieriaindustrialonline.com - Algoritmo de la ruta mucho más corta 
 
from __future__ import print_function 
from ortools.graph import pywrapgraph 
 
def main(): 
  """MinCostFlow amoldado a la ruta mucho más corta - plataforma de trabajo de ejemplo.""" 
 
  # Define 4 matrices paralelas: nodos_fuente, nodos_destino,  
  # habilidades, y costos_unitarios entre cada par. 
 
  nodos_fuente      = [ 0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7] 
  nodos_destino     = [ 1, 2, 2, 3, 1, 3, 4, 5, 6, 3, 6, 7, 6, 8, 5, 7, 8, 6, 8] 
  habilidades       = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
  distancia         = [ 4, 2, 2, 7, 4, 9, 6, 1, 5, 2, 3, 2, 1, 5, 4, 3, 6, 2, 6] 
 
  # Define una matriz con los recursos de cada nodo (valores positivos =  
  # recursos) y (valores negativos = solicitudes) 
 
  recursos = [1, 0, 0, 0, 0, 0, 0, 0, -1] 
 
 
  # Crea una instancia para el solucionador 
  min_cost_flow = pywrapgraph.SimpleMinCostFlow() 
 
  # Define cada arco del inconveniente 
  for i in range(0, len(nodos_fuente)): 
    min_cost_flow.AddArcWithCapacityAndUnitCost(nodos_fuente[i], nodos_destino[i], 
                                                habilidades[i], distancia[i]) 
 
  # Define los recursos para cada nodo. 
 
  for i in range(0, len(recursos)): 
    min_cost_flow.SetNodeSupply(i, recursos[i]) 
 
 
  # Halla el valor mínimo entre el nodo 0 y el nodo 8 
  if min_cost_flow.Solve() == min_cost_flow.OPTIMAL: 
    print('Distancia mínima:', min_cost_flow.OptimalCost()) 
    print('') 
    print('  Arco    Fluído / Aptitud  Distancia') 
    for i in range(min_cost_flow.NumArcs()): 
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i) 
      print('%1s -> %1s    %3s   / %3s       %3s' % ( 
          min_cost_flow.Tail(i), 
          min_cost_flow.Head(i), 
          min_cost_flow.Flow(i), 
          min_cost_flow.Capacity(i), 
          cost)) 
  else: 
    print('Hubo un inconveniente con la entrada de fluído de distancia mínima.') 
 
if __name__ == '__main__': 
  main() 