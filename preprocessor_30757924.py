#Student ID : 30757924
#Name : Ananya Pandey
#Start Date : 25th September 2019
#last Modified : 2nd October 2019

#Task 1 : Setting up the preprocessor
#Task Description : In this task we are required to define a class that will perform the basic preprocessing on each input text.

import codecs
class Preprocessor:

    # This constructor is required for creating instances of this class Preprocessor
    def __init__(self):
        self.book_content = "" # instance variable

    # This method is used to present the content of the instance variable book_content
    def __str__(self):
        return str(self.book_content)

    # This method removes undesirable characters from text present in book_content and stores it back in book_content.
    def clean(self):
        book = "" # a string to store the clean text in lower case
        if self.book_content == "": # to check if there is no text read in this variable book_content, the functions returns 1.
            return 1
        else:
            for word in self.book_content:
                if str(word) == "_" or str(word) == "-": # checks if the word is a "_" or a "-", it converts it into a blank space(" ")
                    word = " "
                    book += str(word) # the word is then concatenated in the string called book
                elif str(word).isalnum() or str(word) == " " : # checks if the word is alphanumeric or a blank space(" ") it is concatenated in the string as it is
                    book += str(word).lower()
            self.book_content = book # the contents of the book are stored back in book_content
            return None

    # This function reads the content of the file into the string instance variable(book_content) of this class
    def read_text(self, text_name):
        file_read = codecs.open(text_name, "r", encoding='utf-8' ) # codecs is used as this text is in UTF-8 encoding
        self.book_content = file_read.read() # the contents of the file which is read is stored in book_content
        return self.book_content

