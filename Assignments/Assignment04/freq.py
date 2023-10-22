import numpy as np
from audiotools import *

def naive_freqs(all_freqs):
    """
    At each time, greedily select the frequency with the smallest
    threshold value

    Parameters
    ----------
    all_freqs: list of lists of [float, float] 
        Output from YIN:
        List of of each frequency at a different threshold for each 
        time window.  For instance, freqs[0] is a list of all 
        [freq, thresh] frequencies at different thresholds at the
        first time instant
    
    Returns
    -------
    freqs: list of float
        List of frequencies with the smallest threshold value at each time instant
    """
    freqs = np.zeros(len(all_freqs))
    for time in range(len(freqs)):
        data = all_freqs[time]
        #freqs[time] = min([(y, x) for x, y in data])[::-1][0]
        freqs[time] = data[np.argmin([y for x, y in data])][0]
    return freqs

import numpy as np

def pyin_freqs(all_freqs, fmin=100, fmax=2000, spacing=2**(1/120), df=30, ps=0.9999, mu=0.1):
    """
    Implement a slightly simplified version of the "pyin" algorithm that
    smooths out transitions for noisy frequencies

    Parameters
    ----------
    all_freqs: list of lists of [float, float] 
        Output from YIN:
        List of of each frequency at a different threshold for each 
        time window.  For instance, freqs[0] is a list of all 
        [freq, thresh] frequencies at different thresholds at the
        first time instant
    fmin: float
        Minimum frequency to consider
    fmax: float
        Maximum frequency to consider
    spacing: float
        Ratio between adjacent frequency bins in the discrete representation
        of frequency
    df: int
        Maximum frequency bin jump in either direction between two adjacent
        time instants
    ps: float
        Probability of staying in voiced or in unvoiced
    mu: float
        Threshold parameter for observation probability of a frequency
        at a particular threshold

    Returns
    -------
    freqs: list of float
        List of frequencies in the highest likelihood path
    """
    return naive_freqs(all_freqs)
