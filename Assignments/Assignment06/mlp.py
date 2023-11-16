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
        self.b_derivs = []
        self.W_derivs = [] 

        #self.add_layer(self.dim, None, None)
    
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
        self.b_derivs.append(np.zeros(_b.shape))
        self.W_derivs.append(np.zeros(_W.shape))
    
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
        _start = 0
        L = len(self.layers)
        _end = L

        self.h = np.zeros(L+1, dtype=object)
        self.a = np.zeros(L+1, dtype=object)

        
        self.h[0] = x

        if start is not None:
            for k in range(L):
                if self.layers[k]["name"] == start:
                    _start = k
                    break

        if end is not None:
            for k in range(L-1, _start, -1):
                if self.layers[k]["name"] == end:
                    _end = k+1
                    break       

        k = 1
        for layer in self.layers[_start: _end]:
            
            W = layer["W"]
            b = layer["b"]
            f = layer["f"]
            #print(f"W: {W.shape}")


            h_1 = self.h[k-1]
            #print(f"h_1: {h_1.shape}")
            a = W.dot(h_1)+b
            h = f(a)
            #print(f"h: {h.shape}")
            self.a[k] = a
            self.h[k] = h

            k += 1
        #   print(f"self.h[-1]: {self.h[-1]}")
        return self.h[-1]
        
    
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
        L = len(self.layers) - 1
        self.forward(x)
        y_est = self.h[L]
        g = self.est_lossderiv(y_est, y)

        ## loop through layers in reverse order
        for k in range(L, 0, -1):
            # Step 1: Propagate gradient backwards through the nonlinear output fk of this layer
            if k < L:
                x = self.layers[k]["fderiv"](self.a[k])
                g = g*x

            # Step 2: Compute the gradients of the weights and biases at this layer
            #print(k, len(self.b_derivs))
            self.b_derivs[k] = self.b_derivs[k] + g
            x = np.outer(g, self.h[k-1].T)
            print(self.W_derivs[k])
            print(self.h[k-1].T)
            self.W_derivs[k] = self.W_derivs[k] + x

            # Step 3: Propagate the gradient backwards through the linear part of this layer to be used at the next layer back
            g += self.layers[k]["W"].T.dot(g)

        return g
        

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
        for i in range(len(self.layers)):
            self.dW[i] = np.zeros(self.layers[i]["W"].shape)
            self.db[i] = np.zeros(self.layers[i]["b"].shape)