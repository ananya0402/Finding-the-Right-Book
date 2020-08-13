#Student ID : 30757924
#Name : Ananya Pandey
#Start Date : 9th October 2019
#last Modified : 17th October 2019

#Task 4 : Presenting Your Results
#Task description : In this task we have to use Term Frequency-Inverse Document Frequency (TF-IDF) to determine the most suitable document for a given term.


# This function returns the document with the highest TF-IDF score for the query term
def choice(term, documents):
    tfidf = dict()
    for index, row in documents.data.iterrows(): # loops through each row of the data frame
        x = row[term] # term frequency of the term
        tf_idf = x * documents.get_IDF(term)
        tfidf[index] = tf_idf # the dictionary(tfidf) stores the tf_idf of each document

    # This for loop is used to find the maximum tf_idf value and then returns the document with the highest tf_idf score
    for k, v in tfidf.items():
        if v == max(tfidf.values()):
            return k


