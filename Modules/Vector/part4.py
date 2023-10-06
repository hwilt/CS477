import numpy as np

def get_dotproduct(a, b):
        """
        Compute the dot product between two high dimensional vectors

        Parameters
        ----------
        a: ndarray(d)
            Vector a
        b: ndarray(d)
            Vector b
        
        Return
        ------
        0 if v is closer to a and 1 if vector is closer to b
        """
        res = 0
        ## Compute the dot product between a and b
        res = np.dot(a, b)
        
        
        return res

np.random.seed(0)
res = ""
d = 100
for i in range(10):
  a = np.random.randn(d)
  b = np.random.randn(d)
  res = "{}{}_".format(res, int(100*get_dotproduct(a, b)))
res = res[0:-1]
print(res)