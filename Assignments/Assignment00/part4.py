import matplotlib.pyplot as plt
import numpy as np

# Make the results repeatable (aka "pseudorandom")
np.random.seed(0) 
num_trials = 100  
# Make a numpy array to hold the trials
trials = np.zeros(num_trials)

for i in range(num_trials):
    num_flips = 0
    heads_in_row = 0
    while heads_in_row < 10:
        if np.random.randint(2) == 1:
            heads_in_row += 1
        else:
            heads_in_row = 0
        num_flips += 1
    trials[i] = num_flips

plt.figure(figsize=(6, 4), dpi=100)
plt.hist(trials)
plt.xlabel("Number of Flips")
plt.ylabel("Counts")
plt.title("10 Heads Histogram")