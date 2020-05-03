import tweepy
import time



words = ['adaptable', 'adventurous', 'affable', 'affectionate', 'agreeable', 'ambitious', 'amiable', 'amicable', 'amusing', 'brave', 'bright', 'broad-minded', 'calm', 'careful', 'charming', 'communicative', 'compassionate', 'conscientious', 'considerate', 'convival', 'courageous', 'courteous', 'creative', 'cute', 'decisive', 'determined', 'diligent', 'diplomatic', 'discreet', 'dynamic', 'easygoing', 'emotional',  'energetic', 'enthusiastic', 'exuberant', 'fair-minded', 'faithful', 'fearless', 'forceful', 'frank', 'friendly', 'funny', 'generous', 'gentle', 'good', 'gregarious', 'hard-working', 'helpful', 'honest', 'hot', 'humorous', 'imaginative', 'impartial', 'independent', 'intellectual', 'intelligent', 'intuitive', 'inventive', 'kind', 'loving', 'loyal', 'modest', 'neat', 'nice', 'optimistic', 'passionate', 'patient', 'persistent', 'pioneering', 'philosophical', 'placid', 'plucky', 'polite', 'powerful', 'practical', 'pro-active', 'quick-witted', 'quiet', 'rational', 'reliable', 'reserved', 'resourceful', 'romantic', 'self-confident', 'self-disciplined', 'sensible', 'sensitive', 'shy', 'sincire', 'sociable', 'straightforward', 'sympathetic', 'thoughtful', 'tidy', 'tough', 'unassuming', 'understanding', 'versatile', 'warmhearted', 'willing', 'witty']

consumer_key = 'o3Dwud8FxUb0mgnJwkMsQeopR'
consumer_secret = 'MudMF3EZJw7hubgzJK9M463632dCVBJvLjWMUT2DjqjWqMy0oC'
access_token = '1256634819502657537-qGRayBwOqEvofottljGEMpW110zR6g'
access_secret = 'EvhsnAYg8SVRegPMQb8wvI5yhhsrEMd513oGcOrO1WtFa'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

while len(words) > 0:
    currentWord = words[0]
    tweet = '@Snqcks is ' + currentWord
    #api.update_status(tweet)
    print(tweet)
    del words[0]
    time.sleep(0.1)


print(len(words))


