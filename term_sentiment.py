import sys, json

# Author Akshat Chauhan
# 07/14/2014
# The first argument to this program is a tab seperated key value pair file
# where key is a word and value is the sentiment attached to it
# Second argument is a valid JSON file containing tweets from twitter.
    
def parse_dictinory(dict_file):
    scores = {} # initialize an empty dictionary
    for line in dict_file:
      term, score  = line.split("\t")
      scores[term] = int(score)  # Convert the score to an integer.
    return scores
  
def score_sentiment(tweet, word_score):
  sentiment_score = 0
  for word in tweet.split():
    lower_word = word.lower()
    if(word_score.has_key(lower_word)):
      sentiment_score = sentiment_score + word_score[lower_word]

  return sentiment_score

def extract_tweet_data(file_to_parse):
  all_tweets = list()

  for line in file_to_parse:
    json_line = json.loads(line)
    all_tweets.append(json_line)

  return all_tweets

def main():
    master_score = parse_dictinory(open(sys.argv[1]))
    calculated_score = {} # empty dict to store calculated scores

    tweet_data = extract_tweet_data(open(sys.argv[2]))

    for x in tweet_data:
      if x.has_key("text"):
        tweet = x["text"]
        word_list = tweet.split() 
        mean_tweet_score = float(score_sentiment(tweet , master_score))/len(word_list)
        for word in word_list:
          lower_word = word.lower() 
          if not (master_score.has_key(lower_word)):
            if(calculated_score.has_key(lower_word)):
              pre_score = calculated_score[lower_word]
              calculated_score[lower_word] = float(pre_score + mean_tweet_score) / 2
            else:
              calculated_score[lower_word] = mean_tweet_score

        
    
    for word_key in calculated_score.keys():
 	  print word_key + ' ' + str(calculated_score[word_key])
      

if __name__ == '__main__':
    main()
