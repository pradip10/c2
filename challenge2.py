import requests
import itertools
from prettytable import PrettyTable

#Fetching list of top article IDs
topStories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
#print(topStories.json())

storiesScore = {} #Initialising dict for score of each URL.

#Fetching data for each article id. We need the score for each URL
for id in topStories.json():
    storyURL = "https://hacker-news.firebaseio.com/v0/item/" + str(id) + ".json"
    storyMeta = requests.get(storyURL)
    print(storyMeta.json()['title'],storyMeta.json()['score'])
    storiesScore[storyMeta.json()['score']] = storyMeta.json()['title']


# Sorting articles by score in descending order of score
sortedStories = dict(sorted(storiesScore.items(), reverse=True))
print("Sorted Stories")
print(sortedStories)

#Print top 20 articles
N = 20
topStories = dict(itertools.islice(sortedStories.items(), N))
print("\nTop 20 stories")
#print(topStories) 

t = PrettyTable(['Score', 'Story'])
for i in topStories:
   t.add_row([i, topStories[i]])

print(t)