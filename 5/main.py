import random
from copy import deepcopy
import json
import pickle

from song_classes import Song, Playlist, PlaylistIterator, ShuffleIterator
'''
Потрібно реалізувати програвач музики

Зберігати інформацію про пісні та кладати плейлісти
'''

# {
#     "hello": [1, 2, 3],
#     "world": {

#     }
# }

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
    # print(playlist_two.songs)

# with open('playlist.pkl', 'wb') as pickle_file:
#     pickle.dump(playlist, pickle_file)

with open('playlist.pkl', 'rb') as pickle_file:
    playlist_three = pickle.load(pickle_file)
    print(playlist_three.songs)
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



