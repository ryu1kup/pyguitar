import re

class Note(object):
    def __init__(self, note):
        self.note = note
        self._base_frequencies = {
                'C': 32.7,
                'C#': 34.6,
                'Db': 34.6,
                'D': 36.7,
                'D#': 38.9,
                'Eb': 38.9,
                'E': 41.2,
                'F': 43.7,
                'F#': 46.2,
                'Gb': 46.2,
                'G': 49.0,
                'G#': 51.9,
                'Ab': 51.9,
                'A': 55.0,
                'A#': 58.3,
                'Bb': 58.3,
                'B': 61.7,
        }
        self.base = re.sub('\d', '', note)
        self.scale = re.sub('\D', '', note)
        self.frequency = self._base_frequencies[self.base] * 2**(int(self.scale) - 1)


    def __add__(self, other):
        for i in range(other):
            if self.base == 'C':
                self.base = 'C#'
            elif self.base == 'C#':
                self.base = 'D'
            elif self.base == 'Db':
                self.base = 'D'
            elif self.base == 'D':
                self.base = 'D#'
            elif self.base == 'D#':
                self.base = 'E'
            elif self.base == 'Eb':
                self.base = 'E'
            elif self.base == 'E':
                self.base = 'F'
            elif self.base == 'F':
                self.base = 'F#'
            elif self.base == 'F#':
                self.base = 'G'
            elif self.base == 'Gb':
                self.base = 'G'
            elif self.base == 'G':
                self.base = 'G#'
            elif self.base == 'G#':
                self.base = 'A'
            elif self.base == 'Ab':
                self.base = 'A'
            elif self.base == 'A':
                self.base = 'A#'
            elif self.base == 'A#':
                self.base = 'B'
            elif self.base == 'Bb':
                self.base = 'B'
            elif self.base == 'B':
                self.base = 'C'
                self.scale = str(int(self.scale) + 1)
        return self.__class__(self.base + self.scale)

    def __sub__(self, other):
        for i in range(other):
            if self.base == 'C':
                self.base = 'B'
                self.scale = str(int(self.scale) - 1)
            elif self.base == 'C#':
                self.base = 'C'
            elif self.base == 'Db':
                self.base = 'C'
            elif self.base == 'D':
                self.base = 'Db'
            elif self.base == 'D#':
                self.base = 'D'
            elif self.base == 'Eb':
                self.base = 'D'
            elif self.base == 'E':
                self.base = 'Eb'
            elif self.base == 'F':
                self.base = 'E'
            elif self.base == 'F#':
                self.base = 'F'
            elif self.base == 'Gb':
                self.base = 'F'
            elif self.base == 'G':
                self.base = 'Gb'
            elif self.base == 'G#':
                self.base = 'G'
            elif self.base == 'Ab':
                self.base = 'G'
            elif self.base == 'A':
                self.base = 'Ab'
            elif self.base == 'A#':
                self.base = 'A'
            elif self.base == 'Bb':
                self.base = 'A'
            elif self.base == 'B':
                self.base = 'Bb'
        return self.__class__(self.base + self.scale)
