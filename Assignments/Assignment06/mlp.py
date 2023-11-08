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
        self.dim = d
        self.est_lossderiv = est_lossderiv
        #
        ## list of dictionary (name, m, f, fderiv, W, b)
        self.layers = []

        ## forward pass variables
        self.a = []
        self.h = []

        ## backpropagation variables
        self.dW = []
        self.db = [] 
    
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
        ## create weights and biases for this layer and store them as instance variables
        if self.layers:
            _W = np.random.randn(m, self.layers[-1]["m"])
        else:
            _W = np.random.randn(m, self.dim)
        #print(f"w shape: {_W.shape}")
        _b = np.random.randn(m)
        #print(f"b: {_b}")
        ## multiply by 0.1 to avoid exploding gradients
        _W *= 0.1
        self.layers.append({"name": name, "m": m, "f": f, "fderiv": fderiv, "W": _W, "b": _b})
        self.a.append(-1)
        self.h.append(-1)
    
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
        y = x.T
        i = 0
        j = len(self.layers)
        # if start is specified, start at that layer
        # if end is specified, stop at that layer
        # otherwise, go through all layers
        if start is not None:
            for k in range(len(self.layers)):
                if self.layers[k]["name"] == start:
                    i = k
                if self.layers[k]["name"] == end:
                    j = k+1
        # store a and h for each layer as instance variables
        for layer in self.layers[i:j]:
            W = layer["W"]
            b = layer["b"]
            f = layer["f"]

            a = W.dot(y)+b
            h = f(a)
            self.a[i] = a
            self.h[i] = h

            y = h
            i += 1

        return y
        
    
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
        self.forward(x)
        y_est = self.h[-1]
        g = self.est_lossderiv(y_est, y)
        for layer in reversed(self.layers):
            W = layer["W"]
            a = self.a.pop()
            h = self.h.pop()
            
            g = g*fderiv(a)
            self.dW.append(np.outer(g, h))
            self.db.append(g)
            g = W.T.dot(g)

            self.step(0.01)
            self.zero_grad()
        
        return y_est

        

    def step(self, alpha):
        """
        Apply the gradient and take a step back

        Parameters
        ----------
        alpha: float
            Learning rate
        """
        for i in range(len(self.layers)):
            self.layers[i]["W"] -= alpha*self.dW.pop()
            self.layers[i]["b"] -= alpha*self.db.pop()

    def zero_grad(self):
        """
        Reset all gradients to zero
        """
        self.dW = []
        self.db = []