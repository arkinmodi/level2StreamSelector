## @file SeqADT.py
#  @author Arkin Modi, modia1
#  @brief Sequence ADT Module
#  @date 11/02/2019


## @brief An abstract data type that represents a Sequence of T
class SeqADT:
    ## @brief SeqADT constructor
    #  @param x sequence of T
    def __init__(self, x):
        self.s, self.i = x, 0

    ## @brief start() sets the current position to the beginning
    def start(self):
        self.i = 0

    ## @brief next() returns the value of the next element in the sequence
    #  @return value of the next element in the sequence
    def next(self):
        if(self.i >= len(self.s)):
            raise StopIteration
        self.i = self.i + 1
        return self.s[self.i - 1]

    ## @brief end() checks if the current index is the last element in the
    #         sequence
    #  @return a boolean indicating if the current element is the last element
    def end(self):
        return self.i >= len(self.s) - 1
