import numpy as np
import math

class MarkovModel:
    def __init__(self, k):
        """
        Initialize a Markov model with a particular prefix length
        
        Parameters
        ----------
        k: int
            Length of prefix to use
        """
        self.k = k
        self.unique_chars = set()
        self.markov_dict = {}
    
    def load_file(self, filename, lower=False):
        """
        Load in an entire file as one string and add
        it to the model

        Parameters
        ----------
        filename: string
            Path to file to load
        lower: boolean
            If true, convert to lowercase
        """
        fin = open(filename, encoding='utf8')
        s = fin.read()
        if lower:
            s = s.lower()
        self.add_string(s)
        fin.close()
    
    def load_file_lines(self, filename, lower=False):
        """
        Load in an entire file as one string and add
        it to the model

        Parameters
        ----------
        filename: string
            Path to file to load
        """
        fin = open(filename, encoding='utf8')
        for line in fin.readlines():
            line = line.rstrip()
            if len(line) > 0:
                if lower:
                    line = line.lower()
                self.add_string(line)
        fin.close()
    
    def add_string(self, s):
        """
        Incorporate a particular string into your model by adding any prefixes
        if they don't exist and by updating counts
        """
        # check if the string is long enough
        if len(s) < self.k:
            return
        # add [0:k] to end of string
        s += s[0:self.k+1]
        # example: {' you ': {'s':1, 't':1, 'r':1, 'i':1, 'n':1, 'g':1}}
        for i in range(len(s)- (self.k+1)):
            # add unique characters to unique_chars
            self.unique_chars.add(s[i])
            prefix = s[i:i+self.k]
            character = s[i+self.k]
            # if prefix is not in markov_dict, add it
            if prefix not in self.markov_dict:
                self.markov_dict[prefix] = {}
            # if character is not in markov_dict[prefix], add it
            if character not in self.markov_dict[prefix]:
                self.markov_dict[prefix][character] = 0
            # increment the character count
            self.markov_dict[prefix][character] += 1
        
    def get_prefixs(self):
        """
        Print out the prefixs in a readable format
        """
        for prefix in self.markov_dict:
            print(prefix)
    
    def get_prefix(self, prefix):
        """
        return the prefix and it's characters
        """
        return self.markov_dict[prefix]

    def get_prefix_count(self):
        """
        return the prefix count of the ditcionary
        """
        return len(self.markov_dict)

    def get_unique_chars(self):
        """
        return the unique characters variable
        """
        return self.unique_chars

    def __str__(self):
        """
        Print out the model in a readable format
        """
        for prefix in self.markov_dict:
            print(prefix, self.markov_dict[prefix])
        return "This is a Markov model with prefix length " + str(self.k) + "."
    
    def get_log_probability(self, s, debug=False):
        """
        Compute the log probability of a particular string according to the model

        Parameters
        ----------
        s: string
            String for which to compute the probability
        
        Returns
        -------
        float: Log probability
        """
        prob = 0
        # log(N(p.c)+1/N(p)+S)
        # N(p.c) = number of times character c follows prefix p
        # N(p) = number of times prefix p appears
        # S = number of unique characters in model

        S = len(self.unique_chars)
        for start in range(len(s) - (self.k)):
            end = start+self.k
            prefix = s[start:end]
            character = s[end]
            if debug:
                print("prefix: {}. character {}".format(prefix, character), end='. ')
            if prefix in self.markov_dict:
                Np = sum(self.markov_dict[prefix].values())
                Npc = 0
                if character in self.markov_dict[prefix]:
                    Npc = self.markov_dict[prefix][character]
                    curr = (Npc+1)/(Np+S)
                else:
                    curr = (Npc+1)/(Np+S)
                if debug:
                    print("np: {}. npc: {}. curr prob: {}".format(Np, Npc, curr), end='.\n')
            else:
                curr = 1/S
            prob += math.log(curr)
        return prob



    def synthesize_text(self, length):
        """
        Synthesize random text of a particular length in the style captured
        by this model

        Parameters
        ----------
        length: int
            How many characters are in the string to synthesize
        
        Returns
        -------
        string: The synthesized text
        """
        ## TODO: Fill this in
        return "" # This does nothing