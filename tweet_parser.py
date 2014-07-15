import sys
import json

    
def parse_dictinory(dict_file):
    scores = {} # initialize an empty dictionary
    for line in dict_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores

def lines(fp):
    print str(len(fp.readlines()))
    
def score_emotion(tweet, word_score):
  emo_score = 0
  for word in tweet.split():    
    if(word_score.has_key(word)):
      emo_score = emo_score + word_score[word]
  return emo_score

def main():
    dict_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    word_score = parse_dictinory(dict_file)
    tweet_data = json.load(tweet_file)
    emotion_score = {} # empty dictionary for storing result
    i = 0
    for x in tweet_data:
      i+=1
      if x.has_key("text"):
        print score_emotion(x["text"],word_score)
      else:
	emotion_score[i] = 0
        

if __name__ == '__main__':
    main()
