
import sys, csv
import operator

speaker = []
views = []
tags = []
ID = []



with open('TED_talk_small.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    ID_sorted = sorted(readCSV, key=lambda x: int(x[0]))
    views_sorted = sorted(readCSV, key=lambda x: float(x[2]), reverse=True)
    speaker_sorted =

    for row in readCSV:
        ID1 = row[0]
        speaker1 = row[1]
        views1 = row[2]
        tags1 = row[3]
        ID.append(ID1)
        speaker.append(speaker1)
        tags.append(tags1)
        views.append(views1)

def csv_find_ID(X):
    IDdex = ID.index(X)
    thespeaker = speaker[IDdex]
    theviews = views[IDdex]
    thetags = tags[IDdex]
    print("\n")
    print("For ID", X, "the speaker is", thespeaker, "and number of views is", theviews, "and tags are", thetags)
    print("\n")

def csv_find_speaker(X):
    speaker_list=[]

def csv_sorted_ID():
    for eachline in ID_sorted:
        print(eachline)


def csv_sorted_speaker():
    pass

def csv_sorted_views():
    print("a")
    print(views_sorted)
    for eachline in views_sorted:
        print(eachline)



def main():
    #print("1. Load the CSV file")
    print("\n")
    print("2. Find the properties with ID")
    print("3. Find the properties with speaker")
    print("4. Find the tags for video")
    print("5. Enter new video with speaker name, views and tags")
    print("6. Cluster the video related with tags")
    print("7. See the list sorted by ID")
    print("8. See the list sorted by Speaker")
    print("9. See the list sorted by number of views")
    print("1. Quit")
    print("\n")
    choice=input("Enter your selection (1-9) ?")

    if (choice == "2"):
        X = input(" Enter the ID number ? ")
        csv_find_ID(X)

    if (choice == "3"):
        X = input(" Enter the speaker name ? ")
        csv_find_speaker(X)


    if (choice == "4"):
        pass
    if (choice == "5"):
        pass
    if (choice == "6"):
        pass
    if (choice == "7"):
        csv_sorted_ID()

    if (choice == "8"):
        csv_sorted_speaker()

    if (choice == "9"):
        csv_sorted_views()

    if (choice=="1"):
        quit()


while True:
    main()