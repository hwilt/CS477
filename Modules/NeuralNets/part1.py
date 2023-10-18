import numpy as np

def fc(c, x):
    return np.array(x > c, dtype=float)

def loss_squared(X, Y, f):
    return np.sum((Y - f(X))**2)

def grid_search(X, Y):
    cs = np.linspace(-3, 3, 1000)
    losses = np.zeros_like(cs)
    for i in range(len(cs)):
        c = cs[i]
        f = lambda x: fc(c=c, x=X)
        losses[i] = loss_squared(X, Y, f)
    ## TODO: Return the c that minimizes the squared loss
    return cs[np.argmin(losses)]


N = 50
np.random.seed(0)
# X is data, Y is labels 
X = np.random.randn(N) - 1
Y = np.zeros(N)
X = np.concatenate((X, np.random.randn(N)+2))
Y = np.concatenate((Y, np.ones(N)))

res = grid_search(X, Y)