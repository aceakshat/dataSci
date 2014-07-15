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

def main():
    word_score = parse_dictinory(open(sys.argv[1]))
    tweet_file = open(sys.argv[2])

    tweet_data = json.load(tweet_file)
    score_List = list() # empty list for storing result

    for x in tweet_data:
      if x.has_key("text"):
   	    score_List.append(score_sentiment(x["text"], word_score))
      else:
	    score_List.append(0)
    
    for score in score_List:
 	  print score
      

if __name__ == '__main__':
    main()
