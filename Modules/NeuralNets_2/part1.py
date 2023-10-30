import numpy as np

logistic = lambda u: 1/(1+np.exp(-u))

def nn_forward(Ws, bs, x):
    """
    Evaluate a feedforward neural network

    Parameters
    ----------
    Ws: list of ndarray(N_{i+1}, Ni)
        Weight matrices for each layer
    bs: list of ndarray(N_{i+1})
        Bias vectors for each layer
    x: ndarray(N_0)
        Input
      
    Returns
    -------
    ndarray
        Result of neural network evaluation
    """
    ## TODO: Evaluate the neural network on an input x
    res = x
    for W, b in zip(Ws, bs):
        z = np.dot(W, res) + b
        res = logistic(z)
    return res


np.random.seed(0)
As = [np.random.randn(4, 3), np.random.randn(5, 4), np.random.randn(1, 5)]
bs = [np.random.randn(4), np.random.randn(5), np.random.randn(1)]
x = np.random.randn(3)
res = nn_forward(As, bs, x)[0]

print("Result: ", res)