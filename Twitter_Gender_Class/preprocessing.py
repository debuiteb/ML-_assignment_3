#Clean init dataset add text features remove unused
import pandas as pd
import nltk
from nltk import word_tokenize
import os


def readFile(filepath):
    column_names = ["_unit_id","_golden", "_unit_state","_trusted_judgements","_last_judgement_at","gender","gender:confidence",
                    "profile_yn","profile_yn:confidence","created","description","fav_number","gender_gold","link_color","name",
                    "profile_yn_gold","profileimage","retweet_count","sidebar_color","text","tweet_coord","tweet_count",
                    "tweet_created","tweet_id","tweet_location","user_timezone"]
    dataframe = pd.read_csv(filepath,encoding="ISO-8859-1",
                                sep=',', header=0, names=column_names,
                                usecols=[5,9,10,11,13,18,19,21,22])
    print(dataframe)
    return dataframe

def clean(dataframe):
    descriptions = dataframe.description
    tweets = dataframe.text
    tokenise(descriptions)
    return dataframe

def tokenise(column):
    for row in column:
        print(row)
        if not(pd.isnull(row)):
            tokens = word_tokenize(row)
            print(tokens)



