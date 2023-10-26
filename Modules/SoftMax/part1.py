import numpy as np

def softmax(u):
    """
    Implement the softmax method

    Parameters
    ----------
    u: ndarray(N)
      Input to softmax
      
    Returns
    -------
    ndarray
        Result of softmax
    """
    ret = np.zeros(len(u))
    sum = 0
    for i in range(len(u)):
        sum += np.exp(u[i])
    for i in range(len(u)):
        ret[i] = np.exp(u[i]) / sum
    
    return ret

def softmax_fast(u):
    exp_u = np.exp(u)
    return exp_u / np.sum(exp_u)


np.random.seed(0)
u = np.random.randn(10)
res = "_".join(["{:.3f}".format(x) for x in softmax_fast(u)])
print(res)

ans = "0.182_0.046_0.083_0.293_0.202_0.012_0.081_0.027_0.028_0.047"

print(ans == res)