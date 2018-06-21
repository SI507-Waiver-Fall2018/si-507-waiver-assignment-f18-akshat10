import tweepy
import nltk
import csv


twitter_extras = ['http', 'https','RT' ]



import sys
consumer_key = "fzTKr5UJm5JEYdtMGo4359QYJ"
consumer_secret = "aVo6QqSjjNe18n3YW2uEsjEOovNMvFlrZYpGJK3WrWjeKLrX05"

access_token = "2470112398-BdgcMHVcYLBJkMYvDTNBQWuJYhCQC223ZxUQB4S"
access_token_secret = "UB8ANuStsE6GiRkOiKBlG8QIQm6WpJhLUQ6iuuPVaGkKs"

stopWords = ['http','https','RT']

filteredTokens = []

f = open('noun_data.csv','w')
f.write('Noun,Number\n')


def printToken(verbs, writeToCsv):
    verb_dictionary = {}

    ## Python will convert \n to os.linesep


    i = 0

    for v in verbs:
        if v in verb_dictionary.keys():
            verb_dictionary[v]+=1
        else:
            verb_dictionary[v]=1

    finalString= ""
    for (word, tag) in sorted(verb_dictionary.items(), key=lambda x: (-x[1], x[0])):
        if i < 5:
            writeString = ""
            if writeToCsv:
                writeString = str(word)+","+str(tag) + "\n"
                f.write(writeString)


            finalString += (word + "(" + str(tag) + ") ")
            i+=1
        else:
            break


    return finalString


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)


    user = sys.argv[1]
    numOfTweets = sys.argv[2]

    favs = 0
    rtCount = 0

    tweets = api.user_timeline(screen_name = user,count = numOfTweets,include_rts=False)

    originalTweets = len(tweets)



    for tweet in tweets:
        rtCount += tweet.retweet_count
        favs += tweet.favorite_count
        tweet_tokens = nltk.word_tokenize(tweet.text)
        for w in tweet_tokens:
            if (w[0].isalpha()) and (w not in stopWords) and (len(w)>1):
                filteredTokens.append(w)


    verbs = []
    nouns = []
    adjectives = []


    for word,tag in nltk.pos_tag(filteredTokens):

        if tag[0] == "V" and tag[1] == "B":
            verbs.append(word)
        elif tag[0] == "N" and tag[1] == "N":
            nouns.append(word)
        elif tag[0] == "J" and tag[1] == "J":
            adjectives.append(word)



    print("USER:", user)
    if str(numOfTweets) > str(200):
        print("TWEETS ANALYZED: 200")
    else:
        print("TWEETS ANALYZED:", numOfTweets)
    print("VERBS", printToken(verbs, False))
    print("Nouns", printToken(nouns, True))
    f.close()
    print("Adjectives", printToken(adjectives,False))
    print("ORIGINAL TWEETS:", originalTweets)
    print("TIMES FAVORITED (ORIGINAL TWEETS ONLY):", favs)
    print("TIMES RETWEETED (ORIGINAL TWEETS ONLY):", rtCount)





if __name__ == '__main__':
    main()
