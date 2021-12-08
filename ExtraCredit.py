from textblob import Word
from textblob.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


blob = TextBlob(Path("socialmedia.txt").read_text())

print(blob)

neg = []
pos = []
neut = []
for sentence in blob.sentences:
    print(sentence)
    print(round(sentence.sentiment.polarity, 3))
    if sentence.sentiment.polarity > 0:
        pos.append(sentence)
    if sentence.sentiment.polarity <0:
         neg.append(sentence)
    if sentence.sentiment.polarity == 0:
        neut.append(sentence)

print(pos)
print(neg)
print(neut)


'''
df = pd.DataFrame(neg, columns=["Count", "negative"])

print(df)


df.plot.bar(x="word", y="count", legend=False,
            color=["y", "c", "m", "b", "g", "r"])

plt.gcf().tight_layout()
plt.show

'''

