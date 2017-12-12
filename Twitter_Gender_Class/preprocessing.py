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
    #dataframe = dataframe.dropna()
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
        if('#' in column[i]):   # if #
            frame[i][0] = 1
        if('@' in column[i]):   # if @
            frame[i][1] = 1
        if('http' in column[i]): #if link
            frame[i][2] = 1
    return frame

def create_tweet_and_bio_columns(dataframe):
    [rows, cols] = dataframe.shape

    descriptions = dataframe.description
    tweets = dataframe.text
    desc_tokens = tokenise(descriptions)
    tweet_tokens = tokenise(tweets)

    desc_cols = create_frame(desc_tokens)
    tweet_cols = create_frame(tweet_tokens)

    dataframe['hash_in_bio'] = 0
    dataframe['at_in_bio'] = 0
    dataframe['link_in_bio'] = 0

    for row in range(rows):
        dataframe.at[row, 'hash_in bio'] = desc_cols[row][0]
        dataframe.at[row, 'at_in bio'] = desc_cols[row][1]
        dataframe.at[row, 'link_in bio'] = desc_cols[row][2]

    dataframe['hash_in_tweet'] = 0
    dataframe['at_in_tweet'] = 0
    dataframe['link_in_tweet'] = 0

    for row in range(rows):
        dataframe.at[row, 'hash_in_tweet'] = tweet_cols[row][0]
        dataframe.at[row, 'at_in_tweet'] = tweet_cols[row][1]
        dataframe.at[row, 'link_in_tweet'] = tweet_cols[row][2]

    return dataframe


def strip_nans(dataframe):
    rows = dataframe.shape[0]
    for row in range(rows):
        if dataframe[row].hasnans:
            print("hereeeeeeeeeeeeeeerrrrrrrrrrrrr ", row)
        '''if dataframe["gender"][row] == 'nan':
            print(dataframe["gender"][row])
            dataframe.drop(dataframe.index[row])
            #dataframe["gender"][row] = "NaN" '''

    dataframe = dataframe.dropna()
    return dataframe



def clean(dataframe):

    [rows, cols] = dataframe.shape
    print('rows: ', rows)
    print('cols: ', cols)

    dataframe = create_tweet_and_bio_columns(dataframe)


    '''for col in range(cols):
        for row in range(rows):
            if pd.isnull(dataframe.loc[row, col]):
                print("WE HGA A NANA")'''

    count = 0
    for row in range(rows):
        if dataframe["gender"][row] != "male" and dataframe["gender"][row] != "female" and dataframe["gender"][row] != "unknown" and dataframe["gender"][row] != "brand":
            print(dataframe["gender"][row])
            count += 1

    print(count)

    print(list(dataframe))

    dataframe['account_age'] = 0
    for row in range(rows):
        creation_date = dataframe.iloc[row][1]
        account_age = get_account_age(creation_date)
        dataframe.at[row,'account_age'] = account_age

    #dataframe = strip_nans(dataframe)
    #dataframe = dataframe.dropna()
    #dataframe = dataframe[dataframe.gender.notnull()]
    if dataframe.isnull().values.any():
        print("hereeeeeeeeeeeeeeerrrrrrrrrrrrr")
    print('------------------------------')
    count = 0
    for row in range(rows):
        #if dataframe["gender"][row] != "male" and dataframe["gender"][row] != "female" and dataframe["gender"][row] != "unknown" and dataframe["gender"][row] != "brand":
        if dataframe["gender"][row]=='nan':
            print(dataframe["gender"][row])
            count += 1
    print(count)

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
