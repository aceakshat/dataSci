import sys, json

    
def parse_dictinory(dict_file):
    scores = {} # initialize an empty dictionary
    for line in dict_file:
      term, score  = line.split("\t")
      scores[term] = int(score)  # Convert the score to an integer.
    return scores
  
def score_sentiment(tweet, word_score):
  sentiment_score = 0
  for word in tweet.split():    
    if(word_score.has_key(word)):
      sentiment_score = sentiment_score + word_score[word]
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
