# mytwitterbot.py
# IAE 101, Fall 2022
# Project 04 - Building a Twitterbot
# Name: Carolyn Do
# netid: CADO     
# Student ID: 115127441

import sys
import time, datetime, random
import simple_twit
import os


# Assign the string values that represent your developer credentials to
# each of these variables; credentials provided by the instructor.
# If you have your own developer credentials, then this is where you add
# them to the program.
# Consumer Key also known as API key
CONSUMER_KEY = "9imuzuQ6dwfTDJQXdXPipe6uP"
# Consumer Secret also known as API Key Secret
CONSUMER_SECRET = "K2KyuU7OTE8Sn9GJWyamPIpTtgaFsAJYukHMo50CbsmE6LTjbr"

### Project 04 Exercises
# Exercise 1 - Get and print 10 tweets from your home timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
##def exercise1(api):
##   tweet_list_me=simple_twit.get_home_timeline(api,10)
##   for tweet in range(len(tweet_list_me)):
##       id_num = str(tweet_list_me[tweet].id)
##       print("#" + str(tweet + 1) + " Tweet ID: " + id_num)
##       print("Author's name/screen name: " + (tweet_list_me[tweet].user.name) + "/" + tweet_list_me[tweet].user.screen_name)
##       print("Tweet create date: " + str(tweet_list_me[tweet].created_at))
##       print("Tweet full text: \n" + tweet_list_me[tweet].full_text)
##       print()
##
# Exercise 2 - Get and print 10 tweets from another user's timeline
# For each tweet, print the tweet ID, the author's name,
# the author's screen_name, the tweet creation date, and the
# tweet full_text
##def exercise2(api):
##   tweet_list_celebrity = simple_twit.get_user_timeline(api, 'taylorswift13' , 10)
##   for tweet in range(len(tweet_list_celebrity)):
##       id_num = str(tweet_list_celebrity[tweet].id)
##       print("#" + str(tweet + 1) + " Tweet ID: " + id_num)
##       print("Author's name/screen name: " + (tweet_list_celebrity[tweet].user.name) + "/" + tweet_list_celebrity[tweet].user.screen_name)
##       print("Tweet create date: " + str(tweet_list_celebrity[tweet].created_at))
##       print("Tweet full text: \n" + tweet_list_celebrity[tweet].full_text)
##       print()

# Exercise 3 - Post 1 tweet to your timeline.
##def exercise3(api):
##   simple_twit.send_tweet(api,"TEST TWEET")
##   print("Tweet Posted\n")

# Exercise 4 - Post 1 media tweet to your timeline.
##def exercise4(api):
##   simple_twit.send_media_tweet(api, "TEST MEDIA TWEET", 'test.jpg')
##   print("Media Tweet Posted\n")

# End of Project 04 Exercises


# YOUR BOT CODE GOES IN HERE
def twitterbot(api):
    localtime = time.strftime("%H:%M:%S")
    print(localtime)
    day = datetime.datetime.now()
    date_text = str(day.month) + "/" + str(day.day) + "/" + str(day.year)
    text = "Twitterbot Daily Dog Photo for " + date_text
    mydir = '/Users/carolyndo/Documents/GitHub/TwitterBot/images'
    myfile = random.choice(('gr1.png', 'gr2.png', 'c1.png', 'c2.png', 's3.png'))
    images_path = os.path.join(mydir, myfile)
    img = images_path
    
    list2 = ('tobbella.png','gr5.png', 's2.png', 'c4.png', 'gr7.png')
    list3 = ('taro.png','tobgizmo.png', 'c3.png', 'gr6.png','s1.png')
   
    if localtime >= "00:00:00" and localtime <= "07:59:59":
       tweet = simple_twit.send_media_tweet(api, text, img)
       
    if localtime >= "08:00:00" and localtime <= "15:59:59":
       myfile = random.choice(list2)
       images_path = os.path.join(mydir, myfile)
       img = images_path
       tweet = simple_twit.send_media_tweet(api, text, img)
       
    if localtime >= "16:00:00" and localtime <= "23:59:59":
       myfile = random.choice(list3)
       images_path = os.path.join(mydir, myfile)
       img = images_path
       tweet = simple_twit.send_media_tweet(api, text, img)


if __name__ == "__main__":
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    simple_twit.version()
    api = simple_twit.create_api(CONSUMER_KEY, CONSUMER_SECRET)

    # Once you are satisified that your exercises are completed correctly
    # you may comment out these function calls.
##    exercise1(api)
##    exercise2(api)
##    exercise3(api)
##    exercise4(api)

    # This is the function call that executes the code you defined above
    # for your twitterbot.
    twitterbot(api)
