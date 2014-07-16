import sys, json
from operator import itemgetter

# Author Akshat Chauhan
# 07/14/2014
# The first argument to this program is a valid JSON file containing tweets from twitter.

def get_state_dict():
  states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
  }
  return states

def extract_tweet_data(file_to_parse):
  all_tweets = list()

  for line in file_to_parse:
    json_line = json.loads(line)
    all_tweets.append(json_line)

  return all_tweets

def extract_state(tweet, states):
#  print tweet
  if tweet.has_key("place"):
    place_txt = tweet["place"]
    if (place_txt is not None) and (len(place_txt) != 0) & place_txt.has_key("country_code"):
      if place_txt["country_code"] == "US":
        full_location = place_txt["full_name"]
        for part in full_location.split():
          part = part.strip()
          part = part.upper()  
          if states.has_key(part):
            return part

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
    state_score = {} # empty dict to store word count
    word_score = parse_dictinory(open(sys.argv[1]))
    states = get_state_dict()
    
    tweet_data = extract_tweet_data(open(sys.argv[2]))

    for x in tweet_data:
      if x.has_key("text"):
        tweet = x["text"]
        tweet_score = score_sentiment(tweet, word_score)
        tweet_state = extract_state(x, states)
        if states.has_key(tweet_state):
          if state_score.has_key(tweet_state):
            new_score = state_score[tweet_state] + tweet_score
            state_score[tweet_state] = new_score
          else:
            state_score[tweet_state] = tweet_score
    
    sorted_states = sorted(state_score.iteritems(), key=itemgetter(1), reverse=True)    



    print sorted_states[0][0]
        
        

if __name__ == '__main__':
    main()
