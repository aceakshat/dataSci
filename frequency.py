import sys, json

# Author Akshat Chauhan
# 07/14/2014
# The first argument to this program is a valid JSON file containing tweets from twitter.
    
def main():
    word_count = {} # empty dict to store word count
    
    tweet_file = open(sys.argv[1])
    tweet_data = json.load(tweet_file)

    total_word_count = 0 
    for x in tweet_data:
      if x.has_key("text"):
        tweet = x["text"]
        word_list = tweet.split() 
        total_word_count = total_word_count + len(word_list)
        for word in word_list:
          lower_word = word.lower() 
          if (word_count.has_key(lower_word)):
            count = word_count[lower_word]
            word_count[lower_word] = count +1
          else:
            word_count[lower_word] = 1
    
    # frequency = [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
    for word_key in word_count.keys():
 	  print word_key + ' ' + str(float(word_count[word_key])/total_word_count)
      

if __name__ == '__main__':
    main()
