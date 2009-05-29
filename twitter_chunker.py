import sys
import time
import twitter

def get_tweets(words, offset):
    tweet = ""
    for word in words:
        test_tweet = ' '.join([tweet, word])
        if len(test_tweet) > 140:
            yield (tweet, offset)
            tweet = word
        else:
            tweet = test_tweet
        offset = offset + 1

def main():
    t = twitter.api.Twitter('username', 'password')
    offset = len(sys.argv) == 2 and int(sys.argv[1]) or 0
    words = open('warandpeace.txt').read().split()[offset:]

    for tweet, current_offset in get_tweets(words, offset):
        print "offset: %s\ntweet: %s\n" % (current_offset, tweet)
        print t.statuses.update(status=tweet)
        time.sleep(36)

if __name__ == "__main__":
    main()