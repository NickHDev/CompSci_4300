#Author: Nicholas Hieb
#Date: 09/30/25
#This code is for Simulated Annealing for an OR Gate. It asks for the Cooling Schedule that the user would like to run

import random
import math


# OR GATE
data = [
    ([0,0],0),
    ([0,1],1),
    ([1,0],1),
    ([1,1],1)
]
cooling = float(input("Enter Cooling Schedule: "))
Temp = 1
# Neuron
def neuron(X,Y,Wx,Wy,b):
    valueTotal = (X * Wx + Y * Wy + b)
    return valueTotal

# Schedule
def schedule(t):
    t = t / cooling
    return t

class GateProblem:
    def inital_state(self):
        # Instantiating
        Wx = 0
        Wy = 0
        b = 0
        return [Wx, Wy, b]


    def neighbor(self, current):
        Wx, Wy, b = current
        Wx = Wx + random.uniform(-2,2)
        Wy = Wy + random.uniform(-2,2)
        b = b + random.uniform(-2,2)
        return [Wx, Wy, b]


    def value(self, current):
        Wx, Wy, b = current
        errorTotal = 0
        for (inputs, target) in data:
            valueTotal = neuron(inputs[0], inputs[1], Wx, Wy, b)
            errorTotal += abs(target - (1/(1+math.exp(-valueTotal))))       
        return errorTotal

# Function for SA
def simulated_annealing(problem):
    # Inital state
    current = problem.inital_state()
    Temp = 1
    while Temp > 0.01:
        Temp = schedule(Temp)
        
        # Pick random Successor
        next = problem.neighbor(current)
        # DeltaE = VALUE(current) – VALUE(next)
        delta_E = problem.value(current) - problem.value(next)
        
        if delta_E > 0:
            current = next
        else:
            if random.random() < math.exp(delta_E/Temp):
                current = next
    return current
        

problem = GateProblem()
solution = simulated_annealing(problem)

Wx, Wy, b = solution
print(f"Best Solution: Wx: {Wx:.1f} Wy: {Wy:.1f} b: {b:.1f}")