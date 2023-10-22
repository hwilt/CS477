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

def pyin_freqs(all_freqs, fmin=100, fmax=2000, spacing=2**(1/120), df=30, ps=0.99, mu=0.1):
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
    ## Figure out how many frequency states there are
    K = int(np.log(fmax/fmin)/np.log(spacing))+2
    T = len(all_freqs)
    ## Setup L and B
    L = -np.inf*np.ones((2*K, T))
    B = np.zeros((2*K, T), dtype=int)
    L_Last = np.zeros(2*K)
    ## Setup transition probabilities
    pix = np.arange(K)
    ptrans = 1.0*np.abs(pix[:, None] - pix[None, :])
    valid_idx = ptrans < df
    ptrans[valid_idx] = np.log(1/df - ptrans[valid_idx]/df**2)
    ptrans[~valid_idx] = -np.inf

    for t in range(T):
        ## Step 1: Do voiced states
        N = len(all_freqs[t])
        ## Step 1a: Figure out observation probabilities and the state indices
        js = []
        p_obs = []
        for (f, thresh) in all_freqs[t]:
            js.append(min(K-1, int(np.log2(f/fmin)/np.log2(spacing))))
            p_obs.append(2**(-thresh/mu)/N)
        js = np.array(js, dtype=int)
        ## Step 1b: Voiced to voiced transitions
        LVV = L_Last[0:K][:, None] + ptrans[:, js] + np.log(ps)
        BVV = np.argmax(LVV, axis=0)
        LVV = np.max(LVV, axis=0)
        ## Step 1c: Unvoiced to voiced transitions
        LUV = L_Last[K::][:, None] + ptrans[:, js] + np.log(1-ps)
        BUV = np.argmax(LUV, axis=0) + K
        LUV = np.max(LUV, axis=0)
        L[js, t] = np.maximum(LVV, LUV) + np.log(p_obs)
        idx = BVV
        idx[LUV > LVV] = BUV[LUV > LVV]
        B[js, t] = idx

        ## Step 2: Do unvoiced states
        p_obs = (1-np.sum(p_obs))/K
        ## Step 2a: Unvoiced to unvoiced
        LUU = L_Last[K::][:, None] + ptrans + np.log(ps)
        BUU = K + np.argmax(LUU, axis=0)
        LUU = np.max(LUU, axis=0)
        ## Step 2b: Voiced to unvoiced
        LVU = L_Last[0:K][:, None] + ptrans + np.log(1-ps)
        BVU = np.argmax(LVU, axis=0)
        LVU = np.max(LVU, axis=0)
        L[K::, t] = np.maximum(LUU, LVU) + np.log(p_obs)
        idx = BUU
        idx[LVU > LUU] = BVU[LVU > LUU]
        B[K::, t] = idx

        L_Last = L[:, t]
            
    ## Step 3: Do backtracing
    idx = np.argmax(L[:, -1])
    t = L.shape[1]-1
    freqs = []
    while t >= 0:
        if idx >= K:
            freqs.append(np.nan)
        else:
            freqs.append(fmin*spacing**idx)
        idx = B[idx, t]
        t -= 1
    freqs.reverse()
    return np.array(freqs)
