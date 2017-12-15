#Clean init dataset add text features remove unused
import pandas as pd
import nltk
from nltk import word_tokenize
import os

from datetime import date
import datetime
import re
import numpy as np
import random
from random import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2



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

    dataframe = dataframe.dropna()
    return dataframe

def change_gender(dataframe):
    [rows, cols] = dataframe.shape
    genders=dataframe.gender
    print(len(genders))
    frame = np.zeros((len(genders),1))
    for i in range(0, len(genders)):
        if("male" ==genders[i]):   # if #
            frame[i][0] = 0
        elif("female" == genders[i]):   # if @
            frame[i][0] = 1
        elif("brand" == genders[i]): #if link
            frame[i][0] = 2
        elif("unknown" == genders[i]):
            frame[i][0] = randint(0,2)

    dataframe['gender']=0
    for row in range(rows):
        dataframe.at[row, 'gender'] = frame[row][0]

    return dataframe


def create_account_age(dataframe):
    [rows, cols] = dataframe.shape
    dataframe['account_age'] = 0
    for row in range(rows):
        creation_date = dataframe.iloc[row][1]
        account_age = get_account_age(creation_date)
        dataframe.at[row, 'account_age'] = account_age

    return dataframe

def clean(dataframe):

    [rows, cols] = dataframe.shape

    dataframe = create_tweet_and_bio_columns(dataframe)
    dataframe = create_account_age(dataframe)

    #print(list(dataframe))



    if dataframe.isnull().values.any():
        print("hereeeeeeeeeeeeeeerrrrrrrrrrrrr")
    print('------------------------------')
    count = 0

    #dataframe=dataframe[dataframe.gender != 'unknown']
    #print(dataframe[93])
    dataframe.ix[dataframe["gender"] != "unknown"]
    #print(dataframe)
    dataframe = change_gender(dataframe)
    dataframe = get_colour_good_and_proper(dataframe)
    scaler=MinMaxScaler()
    dataframe[['fav_number', 'tweet_count',
               'hash_in_bio', 'at_in_bio', 'link_in_bio', 'hash_in bio',
               'hash_in_tweet', 'at_in_tweet', 'link_in_tweet','account_age',
               'r_sidebar_colour', 'g_sidebar_colour','b_sidebar_colour','r_link_colour','g_link_colour','b_link_colour'
               ]]  = scaler.fit_transform(dataframe[[ 'fav_number',  'tweet_count',
                'hash_in_bio', 'at_in_bio', 'link_in_bio', 'hash_in bio', 'hash_in_tweet', 'at_in_tweet', 'link_in_tweet', 'account_age',
                'r_sidebar_colour', 'g_sidebar_colour','b_sidebar_colour','r_link_colour','g_link_colour','b_link_colour']])
    #dataframe = feature_select(dataframe)
    return dataframe

def get_account_age(date_of_creation):
    #'r_sidebar_colour', 'g_sidebar_colour','b_sidebar_colour','r_link_colour','g_link_colour','b_link_colour'

    [first,second] = re.split(' ', date_of_creation, 1)

    d = datetime.datetime.strptime(first, '%m/%d/%y')
    day,month,year = d.day,d.month,d.year


    #start:21 March 2006
    l_date = date(int(2017), int(12), int(12))
    f_date = date(int(year), int(month), int(day))
    dif = l_date - f_date

    return dif.days




def get_colour_good_and_proper(dataframe):
    [rows, cols] = dataframe.shape
    sidebar_colors=dataframe.sidebar_color
    link_colors=dataframe.link_color
    frameR = np.zeros((len(sidebar_colors),1))
    framesR = np.zeros((len(link_colors),1))
    frameG = np.zeros((len(sidebar_colors),1))
    framesG = np.zeros((len(link_colors),1))
    frameB = np.zeros((len(sidebar_colors),1))
    framesB = np.zeros((len(link_colors),1))
   
    dataframe['r_sidebar_colour'] = 0
    dataframe['g_sidebar_colour'] = 0
    dataframe['b_sidebar_colour'] = 0
    dataframe['r_link_colour'] = 0
    dataframe['g_link_colour'] = 0
    dataframe['b_link_colour'] = 0
    for row in range(rows):
        RGBs=[0]*3
        RGBs2=[0]*3
        h=sidebar_colors[row].lstrip('#')
        #print(h)
        if(h!='0'and len(h)==6):
            RGB = tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))
            frameR[row][0]=RGB[0]
            frameG[row][0]=RGB[1]
            frameB[row][0]=RGB[2]
        else:
            frameR[row][0]=0
            frameG[row][0]=0
            frameB[row][0]=0
        dataframe.at[row, 'r_sidebar_colour'] =frameR[row][0]
        dataframe.at[row, 'g_sidebar_colour'] =frameG[row][0]
        dataframe.at[row, 'b_sidebar_colour'] =frameB[row][0]
        
        hh=link_colors[row].lstrip('#')
        if(hh!='0' and len(hh)==6):
            RGB2 = tuple(int(hh[i:i+2], 16) for i in (0, 2 ,4))
            framesR[row][0]=RGB2[0]
            framesG[row][0]=RGB2[1]
            framesB[row][0]=RGB2[2]
        else:
            framesR[row][0]=0
            framesG[row][0]=0
            framesB[row][0]=0
        dataframe.at[row, 'r_link_colour'] =framesR[row][0]
        dataframe.at[row, 'g_link_colour'] =framesG[row][0]
        dataframe.at[row, 'b_link_colour'] =framesB[row][0]
    return dataframe

def feature_select_custom(X,y,k):
    X = SelectKBest(chi2, k = k).fit_transform(X,y)
    df = pd.DataFrame(X)
    #print("list", list(df))
    return df