import struct

import numpy as np
import pyaudio

from .note import Note
from .chord import Chord

class Guitar(object):
    def __init__(self, chords=Chord()):
        self._audio = pyaudio.PyAudio()
        self._stream = self._audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                output=1)

        self.chords = chords.chords

        self._guitar_notes = [
                np.array([Note('E4') + i for i in range(20)]),
                np.array([Note('B3') + i for i in range(20)]),
                np.array([Note('G3') + i for i in range(20)]),
                np.array([Note('D3') + i for i in range(20)]),
                np.array([Note('A2') + i for i in range(20)]),
                np.array([Note('E2') + i for i in range(20)]),
        ]

        self._capo_flet = 0

    def wave(self, frequency, tempo):
        points=np.arange(0, 44100 * tempo)
        sins = [
                0.118 * np.sin(1.00*2*np.pi * frequency * points / 44100),
                0.021 * np.sin(1.46*2*np.pi * frequency * points / 44100),
                0.636 * np.sin(2.00*2*np.pi * frequency * points / 44100),
                1.000 * np.sin(3.00*2*np.pi * frequency * points / 44100),
                0.560 * np.sin(4.00*2*np.pi * frequency * points / 44100),
                0.131 * np.sin(5.01*2*np.pi * frequency * points / 44100),
                0.085 * np.sin(6.01*2*np.pi * frequency * points / 44100),
                0.064 * np.sin(7.03*2*np.pi * frequency * points / 44100),
                0.032 * np.sin(8.04*2*np.pi * frequency * points / 44100),
                0.026 * np.sin(9.05*2*np.pi * frequency * points / 44100),
                0.036 * np.sin(11.10*2*np.pi * frequency * points / 44100),
                0.022 * np.sin(12.13*2*np.pi * frequency * points / 44100),
                ]
        sin = np.zeros(len(points))
        for s in sins:
            sin = sin + s
        exp = np.exp(-points / 20000)
        sin = sin / len(sins) * exp
        sin = np.array([int(s * 32767.0) for s in sin])
        return sin

    def play_chords(self, chordnames, tempo=1):
        wave = []
        for chordname in chordnames:
            try:
                chord = self.chords[chordname]
            except:
                raise ValueError('Unknown chord: {}'.format(chordname))

            chord = [self._guitar_notes[s][flet] for s, flet in enumerate(chord) if flet is not None]
            freqs = [note.frequency for note in chord]
            w = np.zeros(int(44100*tempo))
            for f in freqs:
                w = w + self.wave(f, tempo)
            w = w / len(freqs)
            w = [int(w) for w in w]
            wave = wave + w
        wave = struct.pack('h' * len(wave), *wave)

        chunk = 1024
        sp = 0
        buf = wave[sp:sp+chunk]
        while buf:
            self._stream.write(buf)
            sp = sp + chunk
            buf = wave[sp:sp+chunk]

    def tuning(self, transpose=0):
        self._guitar_notes = [
                np.array([Note('E4') + transpose + i for i in range(20)]),
                np.array([Note('B3') + transpose + i for i in range(20)]),
                np.array([Note('G3') + transpose + i for i in range(20)]),
                np.array([Note('D3') + transpose + i for i in range(20)]),
                np.array([Note('A2') + transpose + i for i in range(20)]),
                np.array([Note('E2') + transpose + i for i in range(20)]),
        ]


    def capo(self, flet):
        self._capo_flet = flet
        self._guitar_notes = [n + flet for n in self._guitar_notes]


    def capo_off(self):
        self._guitar_notes = [n - self._capo_flet for n in self._guitar_notes]


    def print_known_chords(self):
        for k in self.chords.keys():
            print(k)


    def add_chord(self, chordname, flets, force=False):
        if chordname not in self.chords.keys() or forse:
            self.chords[chordname] = flets
        else:
            print('Warning: The chord {} already exists. If you want to overwrite try force=True.')
