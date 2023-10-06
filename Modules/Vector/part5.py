import numpy as np

def get_projection(u, v):
    """
    Project a vector u onto a vector v

    Parameters
    ----------
    u: ndarray(d)
      Vector u
    b: ndarray(d)
      Vector v
    
    Return
    ------
    ndarray(d): uprojv, the projection of u onto v
    """
    d = u.size
    res = np.zeros(d) # This is a dummy value
    ## TODO: Fill this in
    dot = np.dot(u, v)
    dot_v = np.dot(v, v)
    res = (dot/dot_v)*v
    return res


np.random.seed(0)
res = ""
d = 100
for i in range(10):
  a = np.random.randn(d)
  b = np.random.randn(d)
  p = [int(x*100) for x in get_projection(a, b)]
  res = "{}{}_".format(res, p)
res = res[0:-1].replace("\n", "")
print(res)