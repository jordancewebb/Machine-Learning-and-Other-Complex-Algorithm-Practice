import pandas as pd
import random
import numpy

def initialization(p_zero, N):
    vmap = numpy.zeros((N,N))
    for i in range(0,N):
        for j in range(0,i):
            if random.random() > p_zero:
                vmap[i][j] = random.random() * 100
                vmap[j][i] = vmap[i][j]
    return vmap


#Distance of a root
def fitness(member):
    return 1

#Take 2 solutions and breed them. Take a piece of a and a piece of b and mix them
def crossover(a,b):
    return a

#Introduce random noise. Let's turn a different direction if need by
def mutate(member):
    return number

#Create a random member of the population
def create_new_member(max_route_length, N):

    route_length = random.randint(0, max_route_length)
    route = numpy.zeros(route_length)

    for i in range(0, route_length):
        route[i] = random.randint(0, N-1)
    return route

#run a loop to create new members
def create_next_generation(population):
    return population

def main(number_of_iterations):
    return True

if __name__ == '__main__':
    print(create_new_member(10, 20))
