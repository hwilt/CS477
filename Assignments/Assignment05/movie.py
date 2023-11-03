import numpy as np
import math
import random

logistic_fn = lambda x: 1 / (1 + math.exp(-x))

class MovieModel:

    def __init__(self):
        self.word_dict = {}


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
        posNeg = filename.split('/')[2]
        fin = open(filename, encoding='utf8')
        s = fin.read()
        if lower:
            s = s.lower()
        self.add_string(s, posNeg)
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
        posNeg = filename.split('/')[2]
        fin = open(filename, encoding='utf8')
        for line in fin.readlines():
            line = line.rstrip()
            if len(line) > 0:
                if lower:
                    line = line.lower()
                self.add_string(line, posNeg)
        fin.close()


    def add_string(self, s, posNeg):
        """
        Incorporate a particular string into your model by adding any prefixes
        if they don't exist and by updating counts
        """
        words = s.split()
        for word in words:
            if not word in self.word_dict:
                if posNeg == 'pos':
                    self.word_dict[word] = 1
                else:
                    self.word_dict[word] = 0
            #print(word)


    def get_wordDict(self):
        return self.word_dict
        

model = MovieModel()
model.load_file_lines('text/movies/pos/1.txt', lower=True)
print(model.get_wordDict())