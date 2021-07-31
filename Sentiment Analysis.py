import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk.data
nltk.download('vader_lexicon')

df = pd.read_csv (r'D:/MyDesktop/Degree/Year 4/TM R&D/Work/EdSheeran.csv')
print(df)

negative = []
neutral = []
positive = []
compound = []
s = SentimentIntensityAnalyzer()
for i in df.index:
    scores = s.polarity_scores(df['Lyrics'].iloc[i])
    negative.append(scores['neg'])
    neutral.append(scores['neu'])
    positive.append(scores['pos'])
    compound.append(scores['compound'])
df['negative'] = negative
df['neutral'] = neutral
df['positive'] = positive
df['compound'] = compound
path = 'D:/MyDesktop/Degree/Year 4/TM R&D/Work/EdSheeran_sentiment.csv'
df.to_csv(path)
print("NEGATIVE : " + str(df['negative'].mean))
print("NEUTRAL : " + str(df['neutral'].mean))
print("POSITIVE : " + str(df['positive'].mean))
print("COMPOUND : " + str(df['compound'].mean))
# nltk.downloader.download('vader_lexicon')
# from nltk.sentiment import SentimentIntensityAnalyzer

# text = "Come on now Dry your eyes I'm sick of all your lies I've grown to despise you Already sick of what you're saying Hoping now I'm only praying My baby's gone away And I've already packed my bags You didn't know me (I've run away) You couldn't show me (What you have to say) My one and only Has gone away Far away You'll never leave me alone Now I'm off on my own I'll never ring your phone again And still you keep on crying If I said I loved you I'd be lying You need to dry your eyes And I've still gone to pack my bags You didn't know me (I've run away) You couldn't show me (What you have to say) My one and only Has gone away You didn't know me (I've run away) You couldn't show me (What you have to say) My one and only Has gone away Far away"
# print(sia.polarity_scores(text))
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# token_list = [token for token in doc]
# filtered_tokens = [token for token in doc if not token.is_stop]
# print(filtered_tokens)
# lemmas = [
# f"Token: {token}, lemma: {token.lemma_}"
# for token in filtered_tokens]
# print(lemmas)
