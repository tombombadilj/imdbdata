#see http://imdbpy.sourceforge.net/docs/README.txt for instructions on installing IMDbpy
from imdb import IMDb
import csv
import re
import unicodecsv
ia = IMDb()

#Reading movie titles from a csv file and match it IMDb Movie ID
f = open('movie_titles.csv')
csv_f = csv.reader(f)
moviename = list()
for row in csv_f:
    for title in row:
        moviename.append(title)
movieid = list()
for title in moviename:
    l = ia.search_movie(title)
    movieid.append(l[0].movieID)
    print(title,l[0].movieID)

#Writing movie and movieID into a csv file
j = list()
new = open('out.csv','w')
writer = csv.writer(new)
for i in range(0,len(movieid)-1):
    t = moviename[i],str(movieid[i])
    j.append(t)
for pair in j:
    writer.writerow(pair)

#using movieID to scrap movie director, genre, user rating, runtime, and primary language
ID = open('out.csv','r')
csv_ID = csv.reader(ID)
userrating = list()
director = list()
genre1 = list()
genre2 = list()
genre3 = list()
genre4 = list()
runtime = list()
lang = list()
matchID = list()
IDlist = list()
for row in csv_ID:
    IDlist.append(row[1])
    print row
i = 1
for number in IDlist:
    print i, number
    p = ia.get_movie(number)
    if len(p['genre']) == 1:
        print p['genre'][0]
        genre1.append(p['genre'][0])
        genre2.append('NA')
        genre3.append('NA')
        genre4.append('NA')
    elif len(p['genre']) == 2:
        print p['genre'][0], p['genre'][1]
        genre1.append(p['genre'][0])
        genre2.append(p['genre'][1])
        genre3.append('NA')
        genre4.append('NA')
    elif len(p['genre']) == 3:
        print p['genre'][0], p['genre'][1], p['genre'][2]
        genre1.append(p['genre'][0])
        genre2.append(p['genre'][1])
        genre3.append(p['genre'][2])
        genre4.append('NA')
    elif len(p['genre']) >= 4:
        print p['genre'][0], p['genre'][1], p['genre'][2], p['genre'][3]
        genre1.append(p['genre'][0])
        genre2.append(p['genre'][1])
        genre3.append(p['genre'][2])
        genre4.append(p['genre'][3])
    matchID.append(number)
    userrating.append(p['user rating'])
    director.append(p['director'][0])
    runtime.append(p['runtime'][0])
    lang.append(p['lang'][0])
    i = i+1
mc = list()
charc = open('movie_info.csv','w')
writer = csv.writer(charc)
print len(matchID), len(userrating), len(director), len(lang), len(runtime), len(genre1), len(genre2), len(genre3), len(genre4)
for i in range(0, len(userrating)-1):
    t = matchID[i], userrating[i], director[i],lang[i],runtime[i], genre1[i], genre2[i], genre3[i], genre4[i]
    mc.append(t)
for info in mc:
    writer.writerow(info)
