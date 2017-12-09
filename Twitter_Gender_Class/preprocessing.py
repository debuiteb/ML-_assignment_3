#Clean init dataset add text features remove unused
import pandas as pd
import nltk
from nltk import word_tokenize
import os

from datetime import date
import datetime
import re
import numpy as np

def read_file(filepath):
    column_names = ["_unit_id","_golden", "_unit_state","_trusted_judgements","_last_judgement_at","gender","gender:confidence",
                    "profile_yn","profile_yn:confidence","created","description","fav_number","gender_gold","link_color","name",
                    "profile_yn_gold","profileimage","retweet_count","sidebar_color","text","tweet_coord","tweet_count",
                    "tweet_created","tweet_id","tweet_location","user_timezone"]
    dataframe = pd.read_csv(filepath,encoding="ISO-8859-1",
                                sep=',', header=0, names=column_names,
                                usecols=[5,9,10,11,13,18,19,21,22]) #9 cols initially
    #print(dataframe)
    return dataframe


def tokenise(column):
    samples = column.size
    tokenised = [0]*samples
    for i in range(0,samples):
        if not(pd.isnull(column[i])):
            tokenised[i] = word_tokenize(column[i])
        else:
            tokenised[i] = ['']

    return tokenised

def create_frame(column):
    frame = np.zeros((len(column),3))
    for i in range(0, len(column)):
        if('#' in column[i]):
            frame[i][0] = 1
        if('@' in column[i]):
            frame[i][1] = 1
        if('http' in column[i]):
            frame[i][2] = 1
    return frame

def clean(dataframe):

    descriptions = dataframe.description
    tweets = dataframe.text
    desc_tokens = tokenise(descriptions)
    tweet_tokens = tokenise(tweets)

    desc_cols = create_frame(desc_tokens)
    tweet_cols = create_frame(tweet_tokens)

    [rows,cols] = dataframe.shape
    print('rows: ' , rows)
    print('cols: ', cols)

    print(list(dataframe))
    dataframe['account_age'] = 0


    for row in range(rows):
        creation_date = dataframe.iloc[row][1]
        account_age = get_account_age(creation_date)
        dataframe.at[row,'account_age'] = account_age

    return dataframe

def get_account_age(date_of_creation):

    [first,second] = re.split(' ', date_of_creation, 1)

    d = datetime.datetime.strptime(first, '%m/%d/%y')
    day,month,year = d.day,d.month,d.year


    #start:21 March 2006
    l_date = date(int(2017), int(12), int(12))
    f_date = date(int(year), int(month), int(day))
    dif = l_date - f_date

    return dif.days
