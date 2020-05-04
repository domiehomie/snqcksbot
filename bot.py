import tweepy
import time
import random


words = ['adaptable', 'adventurous', 'affable', 'affectionate', 'agreeable', 'ambitious', 'amiable', 'amicable', 'amusing', 'brave', 'bright', 'broad-minded', 'calm', 'careful', 'charming', 'communicative', 'compassionate', 'conscientious', 'considerate', 'convival', 'courageous', 'courteous', 'creative', 'cute', 'decisive', 'determined', 'diligent', 'diplomatic', 'discreet', 'dynamic', 'easygoing', 'emotional',  'energetic', 'enthusiastic', 'exuberant', 'fair-minded', 'faithful', 'fearless', 'forceful', 'frank', 'friendly', 'funny', 'generous', 'gentle', 'good', 'gregarious', 'hard-working', 'helpful', 'honest', 'hot', 'humorous', 'imaginative', 'impartial', 'independent', 'intellectual', 'intelligent', 'intuitive', 'inventive', 'kind', 'loving', 'loyal', 'modest', 'neat', 'nice', 'optimistic', 'passionate', 'patient', 'persistent', 'pioneering', 'philosophical', 'placid', 'plucky', 'polite', 'powerful', 'practical', 'pro-active', 'quick-witted', 'quiet', 'rational', 'reliable', 'reserved', 'resourceful', 'romantic', 'self-confident', 'self-disciplined', 'sensible', 'sensitive', 'shy', 'sincire', 'sociable', 'straightforward', 'sympathetic', 'thoughtful', 'tidy', 'tough', 'unassuming', 'understanding', 'versatile', 'warmhearted', 'willing', 'witty']

consumer_key = 'pSClwrcZD4M5zlIcE3n0Ru5zY'
consumer_secret = 'ybZuzItY1hJiJuYfqhznIKJ35Y8I6HMC6d2RMqrGzPZxMvxorr'
access_token = '1256634819502657537-SFcAPmwuJnkIrCaHDUJph4VFljJNLQ'
access_secret = 'tRtTgLDcXSi1bRO1Ee5Tg45NtYcXeE4yOoagYQ5y5i2ev'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

while len(words) > 0:
    print("Snqcksbot version 1.2:")
    print(" ")
    wordNumber = random.randint(0, len(words) - 1)
    print("- wordNumber = " + str(wordNumber) + "/" + str(len(words)))
    currentWord = words[wordNumber]
    print(" ")
    print("- Word picked: " + currentWord)
    tweet = 'Snqcks is ' + currentWord
    print(" ")
    print("- Tweet created: " + tweet)
    api.update_status(tweet)
    print(" ")
    print("- Tweet posted.")
    del words[wordNumber]
    print(" ")
    print("- Deleted " + currentWord + " from list.")
    #time_to_wait = random.randint(300, 172800)
    time_to_wait = random.randint(0, 0)
    print(" ")
    print('- Time to wait: ' + str(time_to_wait) + " seconds.")
    time.sleep(time_to_wait)
    print(" ")
    print("===============================================================================")
    print("")


print("No more words lol")


