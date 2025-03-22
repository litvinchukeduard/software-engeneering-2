import random
from copy import deepcopy
import json
'''
Потрібно реалізувати програвач музики

Зберігати інформацію про пісні та кладати плейлісти
'''

# {
#     "hello": [1, 2, 3],
#     "world": {

#     }
# }

class Song:

    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def to_dict(self):
        return {
            "title": self.title
        }
    
    @staticmethod
    def from_dict(song_dict: dict):
        return Song(song_dict['title'], song_dict['artist'])

    def __eq__(self, value) -> bool:
        if not isinstance(value, Song):
            return False
        return self.title == value.title and self.artist == value.artist

    def __str__(self):
        return f'"{self.title}" by "{self.artist}"'
    
    def __repr__(self):
        return str(self)
    
    def __hash__(self):
        return hash(self.title) + hash(self.artist)
    

class Playlist:
    def __init__(self, songs=[]):
        self.songs = songs
        self.shuffle = False

    def __iter__(self):
        if self.shuffle:
            return ShuffleIterator(self.songs)
        return PlaylistIterator(self.songs)
    
    def toggle_shuffle(self):
        self.shuffle = not self.shuffle

    def add_song(self, song: Song):
        self.songs.add(song)

    @staticmethod
    def from_dict(playlist_dict: dict):
        songs = [Song.from_dict(song) for song in playlist_dict['songs']]
        return Playlist(songs)


class PlaylistIterator:
    def __init__(self, songs: list[Song]):
        self.current_index = 0
        self.songs = songs

    def __next__(self):
        if self.current_index < len(self.songs):
            song = self.songs[self.current_index]
            self.current_index += 1
            return song
        else:
            raise StopIteration
        

class ShuffleIterator:
    def __init__(self, songs: list[Song]):
        self.current_index = 0
        self.songs = deepcopy(songs)
        random.shuffle(self.songs)

    def __next__(self):
        if self.current_index < len(self.songs):
            song = self.songs[self.current_index]
            self.current_index += 1
            return song
        else:
            raise StopIteration
# {'a': 1, 'b': 1}

# print(hash("Hello"))
# print(hash("Hello"))
# print(hash("Hello"))
    
songs = [
    Song('Thunderstruck', 'AC/DC'), # 123
    Song('Smells like teen spirit', 'Nirvana'), #321
    # Song('Thunderstruck', 'AC/DC') # 123
]

song_one = Song('Thunderstruck', 'AC/DC')
# print(dir(song_one))
# print(song_one.__dict__)
# print(json.dumps(song_one.to_dict()))

# print()

# print(Song('Thunderstruck', 'AC/DC'))
# print(Song('Thunderstruck', 'AC/DC') == 1)

# print(songs)

playlist = Playlist(songs)

with open('playlist.json', 'w') as json_file:
    json.dump(playlist, json_file, default=lambda o: o.__dict__, indent=4)

with open('playlist.json', 'r') as json_file:
    playlist_two = Playlist.from_dict(json.load(json_file))
    print(playlist_two.songs)
# print(json.dumps(playlist, default=lambda o: o.__dict__))

# playlist.toggle_shuffle()
# iterator_one = iter(playlist)
# print(next(iterator_one))

# print(playlist.songs)

# playlist.toggle_shuffle()
# iterator_two = iter(playlist)
# print(next(iterator_two))

# my_list = [1, 2, 3]
# iterator_list = iter(my_list)
# print(next(iterator_list))
# print(next(iterator_list))
# print(next(iterator_list))
# print(next(iterator_list))

# iterator_one = iter(playlist)
# iterator_two = iter(playlist)

# print(next(iterator_one))
# print(next(iterator_one))
# print(next(iterator_one))
# print(next(iterator_one))
# print(next(iterator_one))
# print(next(iterator_two))
# print(next(iterator_one))

# for song in playlist:
#     print(song)



