#Student ID : 30757924
#Name : Ananya Pandey
#Start Date : 5th October 2019
#last Modified : 11th October 2019

#Task 3 : Calculating Inverse Document Frequency (IDF)
#Task decription : In this task we have to implement IDF calculations.


import pandas as pd
import math

class IDFAnalyser:

   # This constructor is required for creating instances of this class IDFAnalyser
    def __init__(self):
        self.data = pd.DataFrame() # instance variable(a pandas dataframe)

    # This function loads the frequency of a cleaned text into data with a title that corresponds to the text the frequency was generated from
    def load_frequency(self, book_frequency, book_title):
        x = pd.DataFrame(book_frequency, index = [book_title]) # constructing data frame(x) from the dictionary(book_frequency)
        self.data = self.data.append(x,ignore_index=False, sort=True) # the dataframe is appended to the instance variable (data)
        pd.set_option('display.max_columns', len(book_frequency)) # to expand the output display to see more columns



# Obtains the IDF for the term provided and the documents loaded into data.
    def get_IDF(self,term):
        D = self.data.__len__() # length of the data frame i.e. the number of documents
        N = self.data[term].count() # the count of the number of documents containing the term
        IDF = 1 + math.log(D / (1 + N))
        return IDF




