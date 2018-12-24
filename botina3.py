import tweepy
import time
import random


consumer_key = 'k9fBjSaeDyfS5K5TyZZj3Dkag'
consumer_secret = 'rc49vW2wJpfe76zVBC4jyijecW27cBfrQCyW2KlDUdPGoP4sF0'
access_token = '1057934032443453440-cp7ieui1vFUz3GciAY48DWDsPRDR1h'
access_token_secret = 'dvbqG7XE2atrrR3BPMrsfd4BxSiyrtf0ItsCeQBqZIfTD'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def RandomTekst():
    filename = open('tvitovi.txt', 'r')
    tweettext = filename.readlines()
    filename.close()
    randomChoice = random.randrange(len(tweettext))
    return str((tweettext[randomChoice]))
    #api.update_status(status=tweettext[randomChoice])

def reply_to_tweets():
    print('odgovaram na jebene tvitove...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    rdmtkt = RandomTekst()
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.home_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '##RockovaBotinaSavet' in mention.full_text.lower():
            print('found #RockovaBotinaSavet!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name + '#proba', mention.id)


def reply_to_tweets2():
    print('odgovaram na jebene tvitove.......', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    twts = api.search(q="#RockovaBotinaSavet", since_id=last_seen_id)
    rand_message = ['ubij se', 'obrisi tvit', 'obrisi nalog',
                    'ne smaraj', 'nema ti spasa' ]


    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    trt = ['hello #rockovabotina',
         '#RockovaBotinaSavet',]
    for s in twts:
        last_seen_id = s.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        for i in trt:
            if i == s.text:
                sn = s.user.screen_name
                n = "@% s Savet:  " %  (sn) + random.choice(rand_message)
                s = api.update_status(n, s.id)



while True:
    reply_to_tweets2()
    time.sleep(15)


