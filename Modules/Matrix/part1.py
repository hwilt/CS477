import numpy as np

def get_special_vector(A):
    """
    Return a column vector v so that Axv has the effect of 
    averaging the columns of A

    Parameters
    ----------
    A: ndarray(M, N)
        An M x N matrix
    
    Returns
    -------
    ndarray(N)
        The special vector
    """
    M = A.shape[0]
    N = A.shape[1]
    v = np.ones(N)/N
    return v
    


def average_columns(A):
    """
    Compute the average of each column of a matrix using only
    matrix multiplication and no loops

    Parameters
    ----------
    A: ndarray(M, N)
    A matrix

    Returns
    -------
    ndarray(M)
    A column which is the average of all other columns
    """
    M = A.shape[0]
    N = A.shape[1]
    v = get_special_vector(A)
    return A.dot(v)

np.random.seed(0)
A = 10*np.random.rand(10, 5)
avg = average_columns(A)
avg = np.array(avg, dtype=int).flatten()