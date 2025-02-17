'''
*******************************************************************
Welcome to this handy script for checking the length of your tweet.
The script will check if it will fit the 140 char limit of Twitter.
*******************************************************************
'''
# First ask the user for his/her tweet
tweet = input('Enter your tweet: ')

# Calculate the length of the tweet
tweet_length = len(tweet)

# Condiontal statements
if tweet_length <= 140:
    print(f'That {tweet_length} char tweet will work.')
else:
    residual_value = tweet_length - 140
    print(f'Your {tweet_length} char tweet is {residual_value} chars too long.')