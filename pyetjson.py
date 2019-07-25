import json
import sys

# read file
with open('Film.json', 'r') as myfile:

    
    # Method 1 :
    try:
        videos = json.load(myfile)
        myfile.close()
    except ValueError as e:
        print(e)
        sys.exit(1)

    # Method 2 :
    # data=myfile.read()
    # videos = json.loads(myfile)

    movies = []
    series = []

    for video in videos:
        if video["Type"] == "movie":
            movies.append(video)
        elif video["Type"] == "series":
            series.append(video)

    print("List of movie title : ")
    for movie in movies:
        print(movie["Title"])
    print("##############################")
    print("List of series title : ")
    for serie in series:
        print(serie["Title"])
