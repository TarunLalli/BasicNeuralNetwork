import numpy as np
import math


def main(dataset):
    ...


class Neural_Network:
    def __init__(self , input):
        self.input = input
    
    # Mathematical Formulae
    def sigmoid(x):
        return(1/(1+math.exp(-x)))

    def ReLU(x):
        if x>=0:
            return x
        
    def softmaxfunct(z):
        sigma_z = []
        for z_i in z:
            sigma_z.append(
                math.exp(z_i)/(math.exp(z))
            )
        return sigma_z

    def GradientDescent():
        ...

    def ForwardPropagation():
        ...

    

    def neuron():
        ...



def dummy(z):
    sigma_z = []
    for z_i in z:
        sigma_z.append(
            math.exp(z_i)/(math.exp(z))
        )

dummy(
    [1,2,3,4,5]
)