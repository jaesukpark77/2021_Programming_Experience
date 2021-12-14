import wikipedia

wiki = wikipedia.page('Artificial intelligence')
text = wiki.content

from wordcloud import WordCloud
# from wordcloud import WordCloud, STOPWORDS
# s_words = STOPWORDS.union( {'one', 'using', 'first', 'two', 'make', 'use'} )
wordcloud = WordCloud(width = 2000, height = 1500).generate(text)
# wordcloud = WordCloud(width = 2000, height = 1500, stopwords = s_words).generate(text)


import matplotlib.pyplot as plt

plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)
plt.show()