import sys, csv
import operator

sample1 = open("TED_talk_small.csv",'r')
csv1= csv.reader(sample1,delimiter=',')
next(csv1)
#ID_sorted = sorted(csv1, key=lambda x: int(x[0]))
#for eachline in ID_sorted:
#    print(eachline)

#in the itemgetter you have to write the colum number for sorting
sortedlist = sorted(csv1, key=lambda row: row[1], reverse=False)
#for eachline in sortedlist:
#    print(eachline)


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

    #whatID= input('Enter the name to find its video? ')
    #speakerdex=speaker.index(whatID)
    #theID=ID[speakerdex]
    ##theviews=views[speakerdex]
    #thetags=tags[speakerdex]
    #print("For speaker",whatID,"the ID is",theID,"and number of views is",theviews,"and tags are",thetags)
ID1=int(ID1)+1
ID.append(str(ID1))
print(ID)


