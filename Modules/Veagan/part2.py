import numpy as np

def get_sample(mu, sigma):
    """
    Sample from the Gaussian N(mu, sigma) using the 
    re-parameterization trick

    Parameters
    ----------
    mu: float
      Mean of distribution
    sigma: float
      Standard deviation of distribution
    
    Return
    ------
    float: Sample
    """
    ## Step 1: Sample from N(0, 1)
    z = np.random.randn()
    z = sigma*z+mu # re-parameterization trick
    return z


np.random.seed(0)
res = ""
for i in range(10):
  mu = np.random.randn()
  sigma = np.random.rand()*4
  res = "{}_{:.3f}".format(res, get_sample(mu, sigma))
res = res[1::]

print(res)