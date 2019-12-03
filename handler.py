
import tweepy

def TwitterServerless1(event, context):
    # Variables that contain the user credentials to access Twitter API 
    
    ACCESS_TOKEN = '1200415115151060993-rHvDGCzVH6T4IVUwfVmOtjmVZlzgMj'
    ACCESS_SECRET = 'HBfP7aMtMzkO2GCfRmmzJLqsDdA7joIiBrB72grutCc0e'
    CONSUMER_KEY = '8aKblfiUx9KZYBimQu1iUuezE'
    CONSUMER_SECRET = 'b0TSiCwbpyhs0JBxaEeA1Liv3FLp7lBPzWlVidZqdpD9MohJM2'

    # Setup tweepy to authenticate with Twitter credentials:

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Create the API to connect to twitter with your creadentials
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    lengths = []
    
    # Search tweeter for recent statuses with the term provided
    for status in tweepy.Cursor(api.search, q='\"{}\" -filter:retweets'.format(event['term']), result_type='recent', tweet_mode='extended').items(1000):
        tweet=status.full_text
        lengths.append (len(tweet))

    # If no tweets exist with the term provided return 0. Else, calculate median
    if (len(lengths) == 0):
        median = 0
    else:
        lengths.sort()
        num_of_tweets = len(lengths)
        if num_of_tweets % 2 == 1:
            median = lengths[(num_of_tweets-1)//2]
        else:
            median = (lengths[num_of_tweets//2] + lengths[num_of_tweets//2-1])/2
    
    return {
        "median": median
    }
    
