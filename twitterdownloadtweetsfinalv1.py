import tweepy
import datetime
import pytz
import csv

#Three inputs
#1.  Input Twitter user handle
twitterUserHandle = ""

#2.  Input Twitter credentials
accesstoken = ""
accesstokensecret = ""
consumerkey = ""
consumersecret = ""
authenticate = tweepy.OAuthHandler(consumerkey, consumersecret)
authenticate.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(authenticate)

#3.  Input number of Tweets downloaded.  Maximum is 3,200.
numberTweetsDownload = 1000

#API
#Function convert UTC time to user's time zone
def convertUTCTimeToLocalTime(twitterCreateDate):
    localTimeZone = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
    twitterCreateDateStrpTime = datetime.datetime.strptime(twitterCreateDate, "%a %b %d %H:%M:%S %z %Y")
    localDateTime = twitterCreateDateStrpTime.replace(tzinfo=pytz.utc).astimezone(localTimeZone)
    dateLocal = datetime.datetime.strftime(localDateTime, "%m/%d/%Y")
    timeLocal = datetime.datetime.strftime(localDateTime, "%I:%M:%S %p")
    return dateLocal, timeLocal
#Function combine multiple urls separate by comma
def joinURLs(links):
    if len(links) == 0:
        return None
    elif len(links) == 1:
        return "".join(links)
    else:
        return ", ".join(links)


#Create CSV file
with open(twitterUserHandle + "tweets.csv", "w", newline="") as tweetsHeader:
    writeHeader = csv.writer(tweetsHeader, delimiter="\t")
    writeHeader.writerow(["Tweet ID", "Tweet Type", "Tweet Date", "Tweet Time", "Tweet Text", "Tweet URL", "Tweet Pic URL", "Origin Tweet ID", "Origin Tweet Date", "Origin Tweet Time", "Origin Tweet Handle", "Origin Tweet Text", "Origin Tweet URL", "Origin Tweet Pic URL"])

#Download tweets
for status in tweepy.Cursor(api.user_timeline, id=twitterUserHandle, tweet_mode="extended").items(numberTweetsDownload):
    [tweetID, tweetType, tweetDate, tweetTime, tweetText, tweetURL, tweetPicURL, originTweetID, originTweetDate, originTweetTime, originTweetHandle, originTweetText, originTweetURL, originTweetPicURL] = [""] * 14
    tweetID = "ID-" + str(status._json["id"])
    tweetLocalDateTime = convertUTCTimeToLocalTime(status._json["created_at"])
    tweetDate, tweetTime = tweetLocalDateTime[0], tweetLocalDateTime[1]
    #User retweet with quote
    if status._json["is_quote_status"] == True:
        tweetType = "Quote Tweet"
        tweetText = status._json["full_text"].encode("unicode-escape").decode("utf-8")
        retweetMyselfMyURL = [eachTweetURL["expanded_url"] for eachTweetURL in status._json["entities"]["urls"][:-1]]
        if retweetMyselfMyURL:
            tweetURL = joinURLs(retweetMyselfMyURL)
        try:
            retweetMyselfMyPictureURL = [eachTweetURL["media_url_https"] for eachTweetURL in status._json["extended_entities"]["media"]]
            tweetPicURL = joinURLs(retweetMyselfMyPictureURL)
        except KeyError:
            pass
        try:
            originTweetID = "ID-" + str(status._json["quoted_status"]["id"])
            originTweetLocalDateTime = convertUTCTimeToLocalTime(status._json["quoted_status"]["created_at"])
            originTweetDate, originTweetTime = originTweetLocalDateTime[0], originTweetLocalDateTime[1]
            originTweetHandle = status._json["quoted_status"]["user"]["screen_name"]
            originTweetText = status._json["quoted_status"]["full_text"].encode("unicode-escape").decode("utf-8")
        except:
            originTweetID = "ID-" + str(status._json["retweeted_status"]["id"])
            originTweetLocalDateTime = convertUTCTimeToLocalTime(status._json["retweeted_status"]["created_at"])
            originTweetDate, originTweetTime = originTweetLocalDateTime[0], originTweetLocalDateTime[1]
            originTweetHandle = status._json["retweeted_status"]["user"]["screen_name"]
            originTweetText = status._json["retweeted_status"]["full_text"].encode("unicode-escape").decode("utf-8")
        try:
            retweetMyselfOriginURL = [eachTweetURL["expanded_url"] for eachTweetURL in status._json["quoted_status"]["entities"]["urls"]]
            if retweetMyselfOriginURL:
                originTweetURL = joinURLs(retweetMyselfOriginURL)
        except KeyError:
            pass
        try:
            retweetOriginURL = [eachTweetURL["expanded_url"] for eachTweetURL in status._json["retweeted_status"]["quoted_status"]["entities"]["urls"]]
            if retweetOriginURL:
                originTweetURL = joinURLs(retweetOriginURL)
        except KeyError:
            pass
        try:
            retweetMyselfOriginVideoURL = [eachTweetURL["video_info"]["variants"][0]["url"] for eachTweetURL in status._json["quoted_status"]["extended_entities"]["media"]]
            if retweetMyselfOriginVideoURL:
                originTweetURL = joinURLs(retweetMyselfOriginVideoURL)
        except KeyError:
            pass
        try:
            retweetOriginVideoURL = [eachTweetURL["video_info"]["variants"][0]["url"] for eachTweetURL in status._json["retweeted_status"]["quoted_status"]["extended_entities"]["media"]]
            if retweetOriginVideoURL:
                originTweetURL = joinURLs(retweetOriginVideoURL)
        except:
            pass
        try:
            retweetMyselfOriginPicURL = [eachTweetURL["media_url_https"] for eachTweetURL in status._json["quoted_status"]["extended_entities"]["media"]]
            originTweetPicURL = joinURLs(retweetMyselfOriginPicURL)
        except KeyError:
            pass
        try:
            retweetOriginPicURL = [eachTweetURL["media_url_https"] for eachTweetURL in status._json["retweeted_status"]["quoted_status"]["extended_entities"]["media"]]
            originTweetPicURL = joinURLs(retweetOriginPicURL)
        except KeyError:
            pass
    #User tweet
    elif status._json["retweeted"] == False:
        tweetType = "Tweet"
        tweetText = status._json["full_text"].encode("unicode-escape").decode("utf-8")
        try:
            tweetURL = [eachTweetURL["expanded_url"] for eachTweetURL in status._json["entities"]["urls"]]
            tweetURL = joinURLs(tweetURL)
        except:
            pass
        try:
            tweetURLVideo = [eachTweetURL["video_info"]["variants"][0]["url"] for eachTweetURL in status._json["extended_entities"]["media"]]
            tweetURL = joinURLs(tweetURLVideo)
        except KeyError:
            pass
        try:
            tweetPicURL = [eachTweetURL["media_url_https"] for eachTweetURL in status._json["extended_entities"]["media"]]
            tweetPicURL = joinURLs(tweetPicURL)
        except KeyError:
            pass
    #User retweet
    elif status._json["retweeted"] == True:
        tweetType = "Retweet"
        try:
            originTweetID = "ID-" + str(status._json["retweeted_status"]["id"])
        except KeyError:
            #User retweet own tweet
            originTweetID = "ID-" + str(status._json["id"])
        try:
            originRetweetLocalDateTime = convertUTCTimeToLocalTime(status._json["retweeted_status"]["created_at"])
            originTweetDate, originTweetTime = originRetweetLocalDateTime[0], originRetweetLocalDateTime[1]
        except KeyError:
            #User retweet own tweet
            originRetweetOwnLocalDateTime = convertUTCTimeToLocalTime(status._json["created_at"])
            originTweetDate, originTweetTime = originRetweetOwnLocalDateTime[0], originRetweetOwnLocalDateTime[1]
        try:
            originTweetHandle = status._json["retweeted_status"]["user"]["screen_name"]
        except KeyError:
            #User retweet own tweet
            originTweetHandle = status._json["user"]["screen_name"]
        try:
            originTweetText = status._json["retweeted_status"]["full_text"].encode("unicode-escape").decode("utf-8")
        except KeyError:
            #User retweet own tweet
            originTweetText = status._json["full_text"].encode("unicode-escape").decode("utf-8")
        try:
            originTweetURLRetweetVideoURL = [eachTweetURL["url"] for eachTweetURL in status._json["retweeted_status"]["extended_entities"]["media"][0]["video_info"]["variants"]]
            originTweetURL = joinURLs(originTweetURLRetweetVideoURL)

            if originTweetURLRetweetVideoURL:
                originTweetURL = joinURLs(originTweetURLRetweetVideoURL)
        except:
            pass
        try:
            originTweetURLRetweetURL = [eachTweetURL["expanded_url"] for eachTweetURL in status._json["retweeted_status"]["entities"]["urls"]]
            if originTweetURLRetweetURL:
                originTweetURL = joinURLs(originTweetURLRetweetURL)
        except KeyError:
            #User retweet own tweet
            originTweetURLRetweetYourOwnURL = [eachTweetURL["expanded_url"] for eachTweetURL in status._json["entities"]["urls"]]
            if originTweetURLRetweetYourOwnURL:
                originTweetURL = joinURLs(originTweetURLRetweetYourOwnURL)
        try:
            originTweetPicURLRetweetPicURL = [eachTweetURL["media_url_https"] for eachTweetURL in status._json["retweeted_status"]["extended_entities"]["media"]]
            originTweetPicURL = joinURLs(originTweetPicURLRetweetPicURL)
        except:
            pass
        try:
            originTweetPicURLRetweetYourOwnPicURL = [eachTweetURL["media_url_https"] for eachTweetURL in status._json["extended_entities"]["media"]]
            originTweetPicURL = joinURLs(originTweetPicURLRetweetYourOwnPicURL)
        except KeyError:
            pass
    else:
        print("Problem")
    #Write to CSV file
    with open(twitterUserHandle + "tweets.csv", "a", newline="") as tweets:
        writetweets = csv.writer(tweets, delimiter="\t")
        writetweets.writerow([tweetID, tweetType, tweetDate, tweetTime, tweetText, tweetURL, tweetPicURL, originTweetID, originTweetDate, originTweetTime, originTweetHandle, originTweetText, originTweetURL, originTweetPicURL])
