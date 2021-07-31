import pandas as pd
import re
import string
import matplotlib.pyplot as plt
#%matplotlib inline# Define a function to plot word cloud
from wordcloud import WordCloud, STOPWORDS

def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off");




df = pd.read_csv (r'D:/MyDesktop/Degree/Year 4/TM R&D/Work/EdSheeran.csv')
All_lyrics = []
for i in df.index:
    All_lyrics.append(df['Lyrics'].iloc[i])

All_lyrics = ' '.join(All_lyrics)
All_lyrics = (''.join(word.strip(string.punctuation) for word in str(All_lyrics)))


wordcloud = WordCloud(width = 3000, height = 2000, random_state=1
                      , background_color='salmon', colormap='Pastel1', collocations=False,
                      stopwords = STOPWORDS).generate(All_lyrics)
plot_cloud(wordcloud)
plt.show()
