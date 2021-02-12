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
api = tweepy.API(authenticate, wait_on_rate_limit=True)

#3.  Input number of favorite tweets downloaded.  Maximum is 3,200.
numberFavoritesDownload = 100

#API
#Function convert UTC time to user's time zone
def convertUTCTimeToLocalTime(twitterFavoriteDate):
    localTimeZone = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
    twitterFavoriteDateStrpTime = datetime.datetime.strptime(twitterFavoriteDate, "%a %b %d %H:%M:%S %z %Y")
    localDateTime = twitterFavoriteDateStrpTime.replace(tzinfo=pytz.utc).astimezone(localTimeZone)
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
with open(twitterUserHandle + "favoritetweets.csv", "w", newline="") as favoriteTweetsHeader:
    writeHeader = csv.writer(favoriteTweetsHeader, delimiter="\t")
    writeHeader.writerow(["Tweet ID", "Tweet Date", "Tweet Time", "Favorite Tweet Handle", "Tweet Text", "Tweet URL", "Tweet Pic URL", "Tweet Video URL"])

#Download favorite tweets
for eachfavoritetweets in tweepy.Cursor(api.favorites, id=twitterUserHandle, tweet_mode="extended").items(numberFavoritesDownload):
    tweetID = "ID-" + str(eachfavoritetweets._json["id"])
    tweetDate, tweetTime = convertUTCTimeToLocalTime(eachfavoritetweets._json["created_at"])[0], convertUTCTimeToLocalTime(eachfavoritetweets._json["created_at"])[1]
    favoriteTweetHandle = eachfavoritetweets._json["user"]["screen_name"]
    tweetText = eachfavoritetweets._json["full_text"].encode("unicode-escape").decode("utf-8")
    try:
        tweetURL = eachfavoritetweets._json["entities"]["urls"][0]["expanded_url"]
    except:
        tweetURL = ""
    try:
        numberofpicslinks = len((eachfavoritetweets._json["extended_entities"]["media"]))
        piclinks = [eachfavoritetweets._json["extended_entities"]["media"][x]["media_url_https"] for x in range(0, numberofpicslinks)]
        tweetPicURL = joinURLs(piclinks)
    except:
        tweetPicURL = ""
    try:
        videolinks = [eachlist["url"] for eachlist in eachfavoritetweets._json["extended_entities"]["media"][0]["video_info"]["variants"] if ".mp4" in eachlist["url"]]
        tweetVideoURL = joinURLs(videolinks)
    except:
        tweetVideoURL = ""
    #Write to CSV file
    with open(twitterUserHandle + "favoritetweets.csv", "a", newline="") as favoriteTweets:
        writefavoriteTweets = csv.writer(favoriteTweets, delimiter="\t")
        writefavoriteTweets.writerow([tweetID, tweetDate, tweetTime, favoriteTweetHandle, tweetText, tweetURL, tweetPicURL, tweetVideoURL])
