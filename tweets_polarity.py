# -*- coding: utf-8 -*-
#import csv
import re
from textblob import TextBlob
#Title + Description
file = open("tweets_30day_Apple.csv", "r")#file with scores
file_polarity = open("tweets_polarity.csv", "w")  #file we write results to
polarity_per_day = {}       #stores the sum of polarities for every date
count_per_day = {}  #counts entries per day
total = count = 0   #pretty sure this is not used 
for line in file.readlines():
    string = ""
    string += line
    if "," in line:
        ''' 
        Next two lines were used to obtain the date from my CSV File. 
        This will be different for yours 
        '''
        tweet, date = string.split(",") 
        date = date[3:10]
        
        tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        if ";" not in date:               #Used to remove some faulty entries 
            tweetBlob = TextBlob(tweet) #Create Textblob
            polarity = tweetBlob.sentiment.polarity #Get polarity
            if date == "\n" or date =="":
                pass
            else:
                if date in polarity_per_day.keys(): #Enter into dictionary
                    polarity_per_day[date] +=polarity
                    count_per_day[date] +=1
                else:
                    polarity_per_day[date] = polarity
                    count_per_day[date] = 1
            string = ""
file_polarity.write("Company,")
for key in count_per_day.keys(): #Write keys to csv(Header)
    string= key+","
    file_polarity.write(string)
file_polarity.write("\nApple,")
print("Apple")
for key in polarity_per_day.keys(): #Write polarities to CSV
    daily = polarity_per_day[key]/count_per_day[key]
    print(key, ": ", daily)
    string = str(daily) + ","
    file_polarity.write(string)
file_polarity.write("\nTesla,")
file = open("tweets_30day_Tesla.csv", "r")
polarity_per_day = {}
count_per_day = {}
for line in file.readlines():
    string = ""
    string += line
    if "," in line:
        tweet, date = string.split(",")
        date = date[3:10]
        tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        if ";" not in date:                
            tweetBlob = TextBlob(tweet)
            polarity = tweetBlob.sentiment.polarity
            if date == "\n" or date =="":
                pass
            else:
                if date in polarity_per_day.keys(): #Enter into dictionary
                    polarity_per_day[date] +=polarity
                    count_per_day[date] +=1
                else:
                    polarity_per_day[date] = polarity
                    count_per_day[date] = 1
            string = ""
print("Tesla")
for key in polarity_per_day.keys():
    daily = polarity_per_day[key]/count_per_day[key]
    print(key, ": ", daily)
    string = str(daily) + ","
    file_polarity.write(string)
file_polarity.write("\nGoldman Sachs,")
file = open("tweets_30day_GoldmanSachs.csv", "r")
polarity_per_day = {}
count_per_day = {}
total = count = 0 
for line in file.readlines():
    string = ""
    string += line
    if "," in line:
        tweet, date = string.split(",")
        date = date[3:10]
        tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        if ";" not in date:                
            tweetBlob = TextBlob(tweet)
            polarity = tweetBlob.sentiment.polarity
            if date == "\n" or date =="" or date[0] == "e":
                pass
            else:
                if date in polarity_per_day.keys(): #Enter into dictionary
                    polarity_per_day[date] +=polarity
                    count_per_day[date] +=1
                else:
                    polarity_per_day[date] = polarity
                    count_per_day[date] = 1
            string = ""
print("Goldman Sachs")
for key in polarity_per_day.keys():
    daily = polarity_per_day[key]/count_per_day[key]
    print(key, ": ", daily)
    string = str(daily) + ","
    file_polarity.write(string)
file_polarity.write("\nBritish Petroleum,")
file = open("tweets_30day_BritishPetroleum.csv", "r")
polarity_per_day = {}
count_per_day = {}
total = count = 0 
for line in file.readlines():
    string = ""
    string += line
    if "," in line:
        tweet, date = string.split(",")
        date = date[3:10]
        tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        if ";" not in date:                
            tweetBlob = TextBlob(tweet)
            polarity = tweetBlob.sentiment.polarity
            if date == "\n" or date =="":
                pass
            else:
                if date in polarity_per_day.keys(): #Enter into dictionary
                    polarity_per_day[date] +=polarity
                    count_per_day[date] +=1
                else:
                    polarity_per_day[date] = polarity
                    count_per_day[date] = 1
            string = ""
print("British Petroleum")
for key in polarity_per_day.keys():
    daily = polarity_per_day[key]/count_per_day[key]
    print(key, ": ", daily)
    string = str(daily) + ","
    file_polarity.write(string)    
file_polarity.close()
