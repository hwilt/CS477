import random

next = {} # This will hold the directed graph
s = "Welcome to cs 477"
# This loops through all of the characters in s
# and keeps track of their indices
for i, c in enumerate(s): 
    if not c in next:
        # If this is the first time seeing a particular 
        # character, we need to make a new key/value pair for it
        next[c] = []
    if i < len(s)-1: # If there is a character after this
        # Record that s[i+1] is one of the following characters
        next[c].append(s[i+1])

#next['W'].append('z') # dead end



MAX_LENGTH = 100 # The maximum length of the output

output = "W"    # The output string, starting with "W"
while len(output) < MAX_LENGTH:
    # Get the last character in the output
    last_char = output[-1]
    
    # check if there is no next character
    if len(next[last_char]) == 0:
        break

    # Get a random character that could follow it
    next_char = random.choice(next[last_char])
    # Add the new character to the output
    output += next_char

print("\'" + output + "\'")