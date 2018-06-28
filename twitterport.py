from keys import Consumer_key,Consumer_secret,Access_secret,Access_Token
import tweepy

oauth = tweepy.OAuthHandler(Consumer_key,Consumer_secret)
oauth.set_access_token(Access_Token, Access_secret)
api=tweepy.API(oauth)
print(api.search("#sanju"))


user = api.get_user('@megha06000906')
print (user.screen_name)
print (user.followers_count)