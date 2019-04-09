import requests
import json


def main():

    directors=['Tim Burton','Martin Scorsese','Steven Spielberg','Joe Russo','Quentin Tarantino']
    groups=['Ariana Grande','Ed Sheeran', 'Shawn Mendes','Vicetone','Melendi','Els amics de les arts','Miley Cyrus']

    for group in groups:
        printOneGroupSongs(group)

    for director in directors:
        printOneDirectorMovies(director)

def printOneGroupSongs(group):
    print("----------------"+group+"----------------")
    group=group.lower()
    group=group.replace(" ", "+")

    a = 'https://itunes.apple.com/search?entity=song&term='
    a = a + group
    b = requests.get(a).json()
    #pelis=json.dumps(b, indent=2)
    songs=b['results']
    for i in range(b['resultCount']):
        print(songs[i]['trackName']+" - ",end="")
        print(songs[i]['artistName']+" - ",end="")
        print(songs[i]['collectionName']+" - ",end="")
        print(songs[i]['releaseDate'][:10]+" - ",end="")
        print(songs[i]['primaryGenreName'])
        print("     "+songs[i]['trackViewUrl'])


def printOneDirectorMovies(director):
    print("----------------"+director+"----------------")
    director=director.lower()
    director=director.replace(" ", "+")

    a = 'https://itunes.apple.com/search?entity=movie&term='
    a = a + director
    b = requests.get(a).json()
    #pelis=json.dumps(b, indent=2)
    pelis=b['results']
    for i in range(b['resultCount']):
        print(pelis[i]['trackName']+" - ",end="")
        print(pelis[i]['releaseDate'][:10]+" - ",end="")
        print(pelis[i]['primaryGenreName'])

        if 'shortDescription' in pelis[i]:
            print("     "+pelis[i]['shortDescription'])
        print("     "+pelis[i]['trackViewUrl'])
        #print(pelis[i]['longDescription']+" - ",end="")
    print()

if __name__ == '__main__':
    main()
