import numpy as np

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
        ## TODO: Setup any other member variables that might be useful
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
        Print out the prefix in a readable format
        """
        for prefix in self.markov_dict:
            print(prefix)
    
    def get_prefix(self, prefix):
        """
        Print out the prefix and it's characters in a readable format
        """
        return self.markov_dict[prefix]

    def get_prefix_count(self):
        """
        Print out the prefix count
        """
        return len(self.markov_dict)
    
    def get_log_probability(self, s):
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
        ## TODO: Fill this in
        return 0 # This is a dummy value

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