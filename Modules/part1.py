import numpy as np

def get_log_posterior_likelihood(counts, probs, prior):
    """
    Compute the log posterior likelihood of a set of word counts given
    probabilities in a model and a prior probability for that model.
    You can assume for simplicity that the key sets for counts and probs 
    are the same

    Parameters
    ----------
    counts: dictionary string-> int
        The counts of a particular word in a bag of words model
    probs: dictionary string-> float
        The smoothed log probability of a word in a model
    prior: float
        The prior probability of the model
    """
    res = np.log(prior)
    ## TODO: Fill this in
    for key in counts:
        res += counts[key] * probs[key]

    return res



counts = {"computer":5, "science":3, "rocks":4}
probs = {"computer":np.log(1/10), "science":np.log(5/10), "rocks":np.log(4/10)}
prior = 0.25
res = get_log_posterior_likelihood(counts, probs, prior)
res = "{:.3f}".format(res)