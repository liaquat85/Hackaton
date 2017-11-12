

import sys, csv
import operator

def csv_file(X):
    ID = []
    speaker = []
    views = []
    tags = []

    with open(X) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            ID1 = row[0]
            speaker1=row[1]
            views1 = row[2]
            tags1=row[3]
            ID.append(ID1)
            speaker.append(speaker1)
            tags.append(tags1)
            views.append(views1)
    #print(ID)

def csv_find_ID(X):
    IDdex = ID.index(X)
    thespeaker = speaker[IDdex]
    theviews = views[IDdex]
    thetags = tags[IDdex]
    print("For ID", whatID, "the speaker is", thespeaker, "and number of views is", theviews, "and tags are", thetags)


def main():
    print("1. Load the CSV file")
    print("2. Find the properties with ID")
    print("3. Find the properties with speaker")
    print("4. Find the tags for video")
    print("5. Enter new video with speaker name, views and tags")
    print("6. Cluster the video related tags")
    print("9. Quit")
    choice=input("\nEnter your selection (1-9)")


    if (choice=="1"):
        X=input("\n Enter the file name with .csv ? ")
        X=str(X)
        csv_file(X)

    if (choice == "2"):
        X = input("\n Enter the ID number")
        csv_find_ID(X)

    if (choice == "3"):
        pass

    if (choice == "4"):
        pass
    if (choice == "5"):
        pass
    if (choice == "6"):
        pass

    if (choice=="9"):
        quit()


while True:
    main()