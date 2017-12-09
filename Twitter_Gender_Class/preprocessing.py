#Clean init dataset add text features remove unused
import pandas
import os


def read_file(filepath):
    column_names = ["_unit_id","_golden", "_unit_state","_trusted_judgements","_last_judgement_at","gender","gender:confidence",
                    "profile_yn","profile_yn:confidence","created","description","fav_number","gender_gold","link_color","name",
                    "profile_yn_gold","profileimage","retweet_count","sidebar_color","text","tweet_coord","tweet_count",
                    "tweet_created","tweet_id","tweet_location","user_timezone"]
    dataframe = pandas.read_csv(filepath,encoding="ISO-8859-1",
                                sep=',', header=0, names=column_names,
                                usecols=[5,9,10,11,13,18,19,21,22]) #9 cols initially
    #print(dataframe)
    return dataframe



def clean(dataframe):
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