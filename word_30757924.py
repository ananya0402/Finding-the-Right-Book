#Student ID : 30757924
#Name : Ananya Pandey
#Start Date : 30th September 2019
#last Modified : 5th October 2019

#Task 2 : Word Analyser
#Task Description : In this task we are required to define a class for analysing the number of occurrences for each word from a given cleaned text.

import codecs
class WordAnalyser:

    # This constructor is needed for creating instances of this class WordAnalyser
    def __init__(self):
        self.word_counts = dict() # instance variable

    # This method is used to present the content of the instance variable(word_counts)
    def __str__(self):
        return self.word_counts

    # This method performs a count on a given book text at the word level
    def analyse_words(self, book_text):
        file_read = codecs.open(book_text, "r", encoding='utf-8-sig') # codecs is used as this text is in UTF-8 encoding
        file = file_read.read()
        for i in file.split(): # this for loop is used to count the occurrences of each word in the file
            if i in self.word_counts:
                self.word_counts[i] += 1
            elif i not in self.word_counts:
                self.word_counts[i] = 1

    # This method is defined to return the frequency of the words found in word_counts as a dictionary
    def get_word_frequency(self):
        frequency = {} # a dictionary to store the frequency of each word
        count = sum(self.word_counts.values()) # sum of the frequencies of all the words
        for each in self.word_counts:
            frequency[each] = self.word_counts[each] / count #frequency of each word is calculated using the formula
        return (frequency)

