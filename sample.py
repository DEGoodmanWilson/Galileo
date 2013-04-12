#!/usr/bin/env python

#a simple example that implements a canonical genetic algorithm
#to show how straight-forward using galileo is. feel free
#to integrate this code into your own programs.

from galileo import *

#simple fitness function that simply sums the values at each
#gene to get the fitness.
def fitness(chromo):
  fitness = 0.0
  for gene in chromo:
    fitness = fitness + gene
  return fitness

#create an initial population of 10 chromosomes
p = Population(10)
#use fitness (above) as our evaluation function
p.evalFunc = fitness
#minimum values the genes can take
p.chromoMinValues = [0,0,0,0,0]    
#maximum values the genes can take
p.chromoMaxValues = [9,9,9,9,9]
#use integers instead of floats
p.useInteger = 1
#always crossover
p.crossoverRate = 1.0
#mutate, but not very often
p.mutationRate = 0.05
#use roulette (monte carlo) selection
p.selectFunc = p.select_Roulette
#use a full replacement size
p.replacementSize = p.numChromosomes
#use one point crossover
p.crossoverFunc = p.crossover_OnePoint
#use the default mutation routines
p.mutateFunc = p.mutate_Default
#use steady-state replacement with no duplication
p.replaceFunc = p.replace_SteadyStateNoDuplicates

#finish initializing the population. THIS MUST BE CALLED after settings the
#variables above, but before actually running the GA!
p.prepPopulation()
#for 50 epochs
for i in range(50):
  #evaluate each chromosomes
  p.evaluate()
  #apply selection
  p.select()
  #apply crossover
  p.crossover()
  #apply mutation
  p.mutate()
  #apply replacement
  p.replace()
  #print the best fit individual, and its fitness
  print p.bestFitIndividual, p.bestFitIndividual.fitness
