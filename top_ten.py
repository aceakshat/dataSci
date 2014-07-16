import sys, json
from operator import itemgetter

# Author Akshat Chauhan
# 07/14/2014
# The first argument to this program is a valid JSON file containing tweets from twitter.
    
def main():
    hashtag_count = {} # empty dict to store word count
    
    tweet_file = open(sys.argv[1])
    tweet_data = json.load(tweet_file)

    for x in tweet_data:      
      if x.has_key("entities"):
        hashtag_txt = x["entities"]["hashtags"]

        for item in hashtag_txt:
          if item.has_key("text"):
            hashtag = item["text"]
            if (hashtag_count.has_key(hashtag)):
              count = hashtag_count[hashtag]
              hashtag_count[hashtag] = count + 1
            else:
              hashtag_count[hashtag] = 1
            
    sorted_hashtag_count = sorted(hashtag_count.iteritems(), key=itemgetter(1), reverse=True)    
    
    rank_counter = 0
    for word_key in sorted_hashtag_count:
      rank_counter = rank_counter + 1
      print word_key[0]+ ' ' + str(word_key[1])
      if(rank_counter >= 10):
        break;
        

if __name__ == '__main__':
    main()
