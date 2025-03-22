import random
from copy import deepcopy
import json
import pickle

class Song:

    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist

    def __getstate__(self):
        state = self.__dict__.copy()
        state['hello'] = 'world'
        # return {
        #     "title": self.title
        # }
        return state
    
    def __setstate__(self, state: dict):
        # self.__dict__.update(state)
        self.__dict__ = {
            'title': 'Hello',
            'artist': 'World'
        }

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
        self.example = 1

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
