import requests
from bs4 import BeautifulSoup
import pandas as pd

link = requests.get('https://www.azlyrics.com/e/edsheeran.html')
soup = BeautifulSoup(link.text, 'lxml')

#for i in k:
songs = soup.find_all("div",class_ = 'listalbum-item')
urls = []
for th in songs:
    urls.extend(th.find_all('a'))
#for i in range(len(urls)):
#    if 'https:' in urls[i]['href']:
#        print(i)
#urls.pop(97)
#urls.pop(156)
#urls.pop(171)


for i in range(len(urls)):
    urls[i]['href'] = 'https://www.azlyrics.com/' + urls[i]['href']

# for url in urls:
#     print(url['href'])

urls = urls[64:]

#print(songs.find('a'))
#for song in songs:
#urls.append(songs.find('a'))
song_name = []
song_lyrics = []
#
u = 0
for url in urls:

    try:
        u+=1
        print(u)
        a = requests.get(url['href'])
        soup = BeautifulSoup(a.text, 'lxml')
        lyrics = soup.find(class_ ="col-xs-12 col-lg-8 text-center")
        lyrics = lyrics.text.strip()
        lyrics = lyrics[lyrics.find('\n\n\n\n')+5:lyrics.find('Submit Corrections')]
        lyrics = lyrics.splitlines()

        j = 0
        for i in range(len(lyrics)):
            if lyrics[i] == '':
                j += 1
        for i in range(j):
            lyrics.remove('')
        lyrics.pop()
        name = lyrics[0]
        lyrics.pop(0)
        lyrics = ' '.join(lyrics)
        song_name.append(name)
        song_lyrics.append(lyrics)
        print(song_name)
    except:
        continue



final_list = pd.DataFrame()
final_list['Name'] = pd.Series(song_name)
final_list['Lyrics'] = pd.Series(song_lyrics)
path = 'D:/MyDesktop/Degree/Year 4/TM R&D/Work/EdSheeran2.csv'
final_list.to_csv(path)


