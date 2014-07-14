import sys
import json

def parse_file(tweet_file):
    data = json.load(tweet_file)

    for x in data["results"]:
        text = x["text"]
        if text != None:
            print x["text"]
    

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    parse_file(tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
