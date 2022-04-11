import pandas as pd
import emot
df = pd.read_csv('/Users/corinnesteuk/PycharmProjects/pythonProject/Joy-11-2021.csv')

tweet_emojis = {}
emoji_meanings = {}
index = 0
for tweet in df['content']:
    # find emoji meanings
    emot_obj = emot.core.emot()
    emojis = emot_obj.emoji(tweet)
    tweet_emojis[index] = emojis['value']

    # if there are emojis in the tweet replace them with their meanings
    if len(emojis['value']) > 0:
        e = []
        for i in range(len(emojis['value'])):

            meaning = emojis['mean'][i]
            clean_meaning = meaning.replace("_", " ")
            clean_meaning = clean_meaning.replace(":", "")
            e.append(clean_meaning)
        emoji_meanings[index] = e
    else:
        emoji_meanings[index] = "Null"
    index += 1

#dictionary of the actual emoji pictures (key: index, value: list of emoji pictures)
# print(tweet_emojis)
#dictionary of the emoji meanings (key: index, value: list of cleaned string emoji meanings)
# print(emoji_meanings)

val = emoji_meanings.values()
val1 = []
for i in val:
    if i != "Null":
        for j in i:
            val1.append(j)

def check(listOfElems):
    emoji_count = {}
    ''' Check if given list contains any duplicates '''
    for elem in listOfElems:
        emoji_count[elem] = listOfElems.count(elem)
    return emoji_count

#dictionary- key: emoji textual meaning; value: number of times it shows up in data
emoji_count = check(val1)




