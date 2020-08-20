# Shahriyar Mammadli
# Obtaining articles from wikipedia
# Import required libraries
import time
from random import randrange
import wikipedia
import os
# Set language
# Use ISO 639-1 to specify desired language's two letter code e.g. fr for French, de for Deutsch etc.
wikipedia.set_lang('az')
articleList = []
# Look for already scraped articles
for filename in os.listdir("wikipedia"):
    if filename.endswith(".txt"):
        articleList.append(filename[0:len(filename)-4])
while(True):
    try:
        # Randomly get an article name
        articleName = wikipedia.random()
        # Be sure that article is not already downloaded
        while(articleName in articleList):
            articleName = wikipedia.random()
        articleList.append(articleName)
        # Write article in to the folder
        with open("wikipedia/" + str(articleName) + ".txt", "w", encoding="utf-8") as f:
            f.write(wikipedia.summary(articleName).rstrip("\n"))
            f.close()
    except:
        print("An exception occured")
    # put random sleeper to avoid ip's banning
    # time.sleep(randrange(1,2))
    print(articleName)

