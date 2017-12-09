#Clean init dataset add text features remove unused
import pandas as pd
import nltk
from nltk import word_tokenize
import os
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


    '''
   [rows,cols] = dataframe.shape
    print('rows: ' , rows)
    print('cols: ', cols)

    #print(dataframe.iterrows)

    print(list(dataframe))
    #dataframe.assign(morning = 0)
    dataframe['morning'] = 0
    dataframe['afternoon'] = 0
    dataframe['evening'] = 0
    print(list(dataframe))
    print(dataframe.iloc[9])



    for row in range(rows):
        #print(dataframe.iloc[row][8])
        tweet_date = dataframe.iloc[row][8]
        tweet_time  = get_tweet_time(tweet_date)

        if(tweet_time<12):
            dataframe.at[row, 'morning'] = 1
        elif(tweet_time>=12 and tweet_time<19):
            dataframe.at[row, 'afternoon'] = 1
        else:
            dataframe.at[row, 'evening'] = 1

    print("----------------------------")
    print(list(dataframe))
    print(dataframe.iloc[9])
'''
    return dataframe

def get_tweet_time(date):
    char_array = list(date)
    on_time = False
    time = ""
    for c in char_array:
        if(c == '' or c==' '):
            on_time = True
        if(on_time):
            if c == ':':
                return int(time)
            time = time + c
    return int(time)
