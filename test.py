import sys, csv
import operator

sample1 = open("TED_talk_small.csv",'r')
csv1= csv.reader(sample1,delimiter=',')

#in the itemgetter you have to write the colum number for sorting
sort=sorted(csv1,key=operator.itemgetter(2),reverse=True)
for eachline in sort:
    print(eachline)


ID = []
speaker=[]
views=[]
tags=[]
with open('TED_talk_small.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    for row in readCSV:
        ID1 = row[0]
        speaker1=row[1]
        views1 = row[2]
        tags1=row[3]
        ID.append(ID1)
        speaker.append(speaker1)
        tags.append(tags1)
        views.append(views1)

  #  whatID= input('Enter the ID of speaker to know its name and tags and number of views ? ')
  #  IDdex=ID.index(whatID)
 ##   thespeaker=speaker[IDdex]
  #theviews=views[IDdex]
   # thetags=tags[IDdex]
 #   print("For ID",whatID,"the speaker is",thespeaker,"and number of views is",theviews,"and tags are",thetags)





