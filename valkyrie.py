import tweepy
from secrets import *
from random import choice
from card import make_image, delete_image
import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
tweeted_file = os.path.join(__location__, "tweeted_users.txt")
greetings = ['Hello there', 'Hello', 'Greetings']
queries = ['"nobody likes me"',
                         '"nobody loves me"',
                         '"no one likes me"',
                         '"no one loves me"',
                         '"i hate my life"',
                         '"i hate everything"']
responses = [ 'You\'re\nloved.',
                'You\'re\nvalued.',
                           'Your support\nhas arrived.',
                           'I like\nyou',
                           'Right beside\nyou',
                           'Taking care\nof you.']



filters = re.compile(
  """(http|#nowplaying|youtube|-|"|“|”|poor boy|the way you do|hear it every ?day|that\'?s ok'|loves me better|23)""",
  re.IGNORECASE)

def get_tweet(api_, type_):
    """Get a list of tweets matching the search query."""
    query = choice(queries)
    results = api_.search(q=query, count=50)
    return results 


def get_users():
    """Get a list of users we've already tweeted at."""
    f = open(tweeted_file, 'r')
    users = [line.rstrip('\n') for line in f]
    return users


def filter_tweets(tweets_, users_):
    """Filter out tweets to avoid things like song lyrics, etc."""
    while True:
        tweet_ = tweets_.pop(0)
        text = tweet_.text
        if len(tweets) == 0:
            return
        if not (hasattr(tweet_, "retweeted_status") or
                tweet_.in_reply_to_status_id or
                tweet_.author.screen_name in users_ or
                filters.match(text) is not None):
            return tweet_


def send_reply(api_, type_, tweet_):
    """Send the reply tweet and record it."""
    f = open(tweeted_file, 'a')
    f.write(tweet_.author.screen_name + '\n')
    f.close()
    #text = '@' + tweet_.author.screen_name + ' ' + choice(responses).replace('\n', ' ') + u'\u2764'
    text = '@' + tweet_.author.screen_name + u'\u2764'
    greeting = choice(greetings)
    response = choice(responses)
    image_file = 'output/pic.png'
    make_image(greeting, tweet_.author.screen_name, response, image_file)
    media_id = api_.media_upload(image_file)
    media_ids = [media_id.media_id_string]
    api_.update_status(text, in_reply_to_status_id=tweet_.id_str, media_ids=media_ids)
    delete_image(image_file)



if __name__ == "__main__":
    """Find a tweet and reply to it."""
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweet_type = choice(queries)
    tweets = get_tweet(api, tweet_type)
    users = get_users()
    tweet = filter_tweets(tweets, users)
    send_reply(api, tweet_type, tweet)