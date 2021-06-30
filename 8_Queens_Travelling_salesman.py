import matplotlib.pyplot as plt
import numpy as np
import random 
import sys
import math

inf = 10
dist = [[0,inf,inf,inf,inf,inf,0.15,inf,inf,0.2,inf,0.12,inf,inf],
        [inf,0,inf,inf,inf,inf,inf,0.19,0.4,inf,inf,inf,inf,0.13],
        [inf,inf,0,0.6,0.22,0.4,inf,inf,0.2,inf,inf,inf,inf,inf],
        [inf,inf,0.6,0,inf,0.21,inf,inf,inf,inf,0.3,inf,inf,inf],
        [inf,inf,0.22,inf,0,inf,inf,inf,0.18,inf,inf,inf,inf,inf],
        [inf,inf,0.4,0.21,inf,0,inf,inf,inf,inf,0.37,0.6,0.26,0.9],
        [0.15,inf,inf,inf,inf,inf,0,inf,inf,inf,0.55,0.18,inf,inf],
        [inf,0.19,inf,inf,inf,inf,inf,0,inf,0.56,inf,inf,inf,0.17],
        [inf,0.4,0.2,inf,0.18,inf,inf,inf,0,inf,inf,inf,inf,0.6],
        [0.2,inf,inf,inf,inf, inf,inf,0.56,inf,0,inf,0.16,inf,0.5],
        [inf,inf,inf,0.3,inf,0.37,0.55,inf,inf,inf,0,inf,0.24,inf],
        [0.12,inf,inf,inf,inf,0.6,0.18,inf,inf,0.16,inf,0,0.4,inf],
        [inf,inf,inf,inf,inf,0.26,inf,inf,inf,inf,0.24,0.4,0,inf],
        [inf,0.13,inf,inf,inf,0.9,inf,0.17,0.6,0.5,inf,inf,inf,0]]

#Travelling salesman
def costFunction_tsp(state):
  path_len = 0
  cur_len = 0
  for i in range(len(state) - 1):
    cur_len = dist[state[i]-1][state[i+1]-1]
    path_len += cur_len

  path_len += dist[state[13] - 1][state[0] - 1]

  return path_len
def fitnessFunction_tsp(state):
  path_len = 0
  cur_len = 0
  for i in range(len(state) - 1):
    cur_len = dist[state[i]-1][state[i+1]-1]
    path_len += cur_len

  path_len += dist[state[13] - 1][state[0] - 1]
  fitness = 1 / path_len
  return fitness
def mutate_tsp(state): 
  pos1 = random.randint(0,13)
  pos2 = random.randint(0,13)
  temp = state[pos1]
  state[pos1] = state[pos2]
  state[pos2] = temp

  return state
def reproduce_tsp(state1, state2):
  pos1 = random.randint(0,12)
  pos2 = random.randint(pos1, 13)
  child = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  #print(pos1)
  #print(pos2)

  for i in range(pos1, pos2+1):
    child[i] = state1[i]

  i = 0
  iterator = 0
  while i < pos1:
    flag = 0
    for j in range(len(child)):
      if state2[iterator] == child[j]:
        flag = 1
        break

    if flag == 1:
      iterator += 1
    else : 
      child[i] = state2[iterator]
      iterator += 1
      i += 1

  iterator = 0
  i = pos2 + 1
  while i < 14:
    flag = 0
    for j in range(len(child)):
      if state2[iterator] == child[j]:
        flag = 1
        break

    if flag == 1:
      iterator += 1
    else : 
      child[i] = state2[iterator]
      iterator += 1
      i += 1

  return child
def randomSelection_tsp(population):
  max_1 = 0
  max_2 = 0
  state1 = 0
  state2 = 0
  for i in range(len(population)):
    temp = fitnessFunction_tsp(population[i])
    if temp >= max_1 :
      max_2 = max_1
      max_1 = temp
      state2 = state1
      state1 = i
    elif temp > max_2:
      max_2 = temp
      state2 = i
  return [population[state1], population[state2]]
def geneticAlgorithm_tsp(population) :
  n = len(population)
  new_population = []  
  for j in range(0, n):
    x = randomSelection_tsp(population)[0]
    y = randomSelection_tsp(population)[1]
    child = reproduce_tsp(x, y)
    rand = random.randrange(0,1)
    child = mutate_tsp(child)
    new_population.append(child)

  return new_population
def GA_TSP():

  population = []
  temp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

  for i in range(60):
    population.append(temp)

  iterations = 0
  max_fitness = 0
  best_cost = 100
  state = 0
  max_cur = 0

  while max_fitness < 0.25 and iterations <= 6000 :

    best = population[state]
    print( " iterations : " + str(iterations) + "        max fitness of population : " + str(max_cur))
    max_cur = 0

    new_population = geneticAlgorithm_tsp(population)

    for i in range(0, len(new_population)):
      temp = fitnessFunction_tsp(new_population[i])
      if temp > max_fitness :
        max_fitness = temp
        state = i

      max_cur = max(temp, max_cur)
    iterations += 1
    population = new_population

  if iterations > 6000 :
    print("Terminted because enough time has elapsed, try again")
    main()
  else :
    print("Best solution : " + str(population[state]))

#8 queens
def fitnessFunction_8Q(state):
  pairs = 1

  for i in range(0, 8) :
    for j in range(i, 8) :
      x_dist = j - i
      y_dist = abs(state[j] - state[i])
      if y_dist == 0 :
        continue
      elif x_dist == y_dist :
        continue
      else :
        pairs = pairs + 1 

  return (pairs)
def randomSelection_8Q(population):
  max_1 = 0
  max_2 = 0
  state1 = 0
  state2 = 0
  for i in range(len(population)):
    temp = fitnessFunction_8Q(population[i])
    if temp >= max_1 :
      max_2 = max_1
      max_1 = temp
      state2 = state1
      state1 = i
    elif temp > max_2:
      max_2 = temp
      state2 = i
  return [population[state1], population[state2]]
def reproduce_8Q(state1, state2) :
  cross_point = random.randint(0,7)
  child = [0, 0, 0, 0, 0, 0, 0, 0]

  for i in range(0, cross_point) :
    child[i] = state1[i]
  for i in range(cross_point, 8) :
    child[i] = state2[i]

  return child
def reproduce(state1, state2) :
  pos1 = random.randint(0,6)
  pos2 = random.randint(pos1, 7)
  #print(pos1)
  #print(pos2)

  child = [0,0,0,0,0,0,0,0]

  for i in range(pos1, pos2+1):
    child[i] = state1[i]

  i = 0
  iterator = 0
  while i < pos1:
    flag = 0
    for j in range(len(child)):
      if state2[iterator] == child[j]:
        flag = 1
        break

    if flag == 1:
      iterator += 1
    else : 
      child[i] = state2[iterator]
      iterator += 1
      i += 1

  iterator = 0
  i = pos2 + 1
  while i < 8:
    flag = 0
    for j in range(len(child)):
      if state2[iterator] == child[j]:
        flag = 1
        break

    if flag == 1:
      iterator += 1
    else : 
      child[i] = state2[iterator]
      iterator += 1
      i += 1
  return child
def mutate_8Q(state):
  pos1 = random.randint(0,7)
  pos2 = random.randint(0, 7)
  val1 = random.randint(1, 8)
  val2 = random.randint(1 ,8)

  state[pos1] = val1
  state[pos2] = val2

  return state
def geneticAlgorithm_8Q(population) :
  n = len(population)
  new_population = []  
  for j in range(0, n):
    x = randomSelection_8Q(population)[0]
    y = randomSelection_8Q(population)[1]
    child = reproduce_8Q(x, y)
    rand = random.randrange(0,1)
    child = mutate_8Q(child)
    new_population.append(child)
  return new_population
def GA_8Q():
  population = []
  max_fitness = 1


  for i in range(40):
    population.append([1,1,1,1,1,1,1,1])

  new_population = []
  iterations = 0
  iter_array = []
  fit_array = []
  state = 0
  max_cur = 1

  while max_fitness < 29:
    
    print( " Iterations : " + str(iterations) + "        max fitness in population : " + str(max_cur))
    max_cur = 1
    new_population = geneticAlgorithm_8Q(population)

    for i in range(len(new_population)):
      temp = fitnessFunction_8Q(new_population[i])
      if temp > max_fitness:
        max_fitness = temp
        state = i

      if temp > max_cur :
        max_cur = temp

    iterations += 1
    iter_array.append(iterations)
    fit_array.append(max_cur)
    population = new_population
  print("Best solution : " + str(population[state]))

def main():
  print("Which Algortihm should be run?")
  print("Select 1 : for 8 Queens Problem")
  print("Select 2 : for Travelling salesman Problem")

  val = input("Select 1 or 2 : ")
  if(val == "1"):
    GA_8Q()

  else:
    GA_TSP()

main()
