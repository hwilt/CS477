import numpy as np

def get_closer(v, a, b):
        """
        Compute whether a vector v is closer to a vector "a" or a vector "b"

        Parameters
        ----------
        v: ndarray(d)
            Vector to test
        a: ndarray(d)
            Vector a
        b: ndarray(d)
            Vector b
        
        Return
        ------
        0 if v is closer to a and 1 if vector is closer to b
        """
        res = 0
        ## Compute the distance between v and a
        dist_a = np.linalg.norm(v - a)
        ## Compute the distance between v and b
        dist_b = np.linalg.norm(v - b)
        ## Check which distance is smaller
        if dist_a > dist_b:
            res = 1

        
        return res

np.random.seed(0)
res = ""
d = 100
for i in range(10):
  v = np.random.randn(d)
  a = np.random.randn(d)
  b = np.random.randn(d)
  res = "{}{}.".format(res, get_closer(v, a, b))
res = res[0:-1]
print(res)