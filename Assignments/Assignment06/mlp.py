import numpy as np
from losses import *
from layers import *

class MLP:
    """
    A class for representing MLPs, which is amenable to performing
    backpropagation quickly using numpy operations

    Parameters
    ----------
    d: int
        Dimensions of the input
    est_lossderiv: function ndarray(N) -> ndarray(N)
        Gradient of the loss function with respect to the inputs
        to the last layer, using the output of the last layer
    """
    def __init__(self, d, est_lossderiv):
        ## TODO: Fill this in
        pass
        
    
    def add_layer(self, m, f, fderiv, name=None):
        """
        Parameters
        ----------
        m: int
            Number of neurons in the layer
        f: function ndarray(N) -> ndarray(N)
            Activation function, which is applied element-wise
        fderiv: function ndarray(N) -> ndarray(N)
            Derivative of activation function, which is applied element-wise
        name: string
            If specified, store the name of this layer
        """
        ## TODO: Fill this in
        pass

    
    def forward(self, x, start=None, end=None):
        """
        Do a forward pass on the network, remembering the intermediate outputs
        
        Parameters
        ----------
        x: ndarray(d)
            Input to feed through
        start: string
            If specified, start by feeding x to the input of this layer
        end: string
            If specified, stop and return the output of this layer
        
        Returns
        -------
        ndarray(m)
            Output of the network
        """
        ## TODO: Fill this in
        pass
    
    def backward(self, x, y):
        """
        Do backpropagation to accumulate the gradient of
        all parameters on a single example
        
        Parameters
        ----------
        x: ndarray(d)
            Input to feed through
        y: float or ndarray(k)
            Goal output.  Dimensionality should match dimensionality
            of the last output layer
        """
        ## TODO: Fill this in to complete backpropagation and accumulate derivatives
        pass
        

    def step(self, alpha):
        """
        Apply the gradient and take a step back

        Parameters
        ----------
        alpha: float
            Learning rate
        """
        ## TODO: Fill this in
        pass

    def zero_grad(self):
        """
        Reset all gradients to zero
        """
        ## TODO: Fill this in
        pass