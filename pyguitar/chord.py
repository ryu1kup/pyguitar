class Chord(object):
    def __init__(self):
            self.chords = {
                'C': [0, 1, 0, 2, 3, None],
                'CM7': [0, 0, 0, 2, 3, None],
                'C7': [0, 1, 3, 2, 3, None],
                'C6': [0, 1, 2, 2, 3, None],
                'Caug': [None, 1, 1, 2, 3, None],
                'Cm': [3, 4, 5, 5, 3, None],
                'CmM7': [3, 4, 4, 5, 3, None],
                'Cm7': [3, 4, 3, 5, 3, None],
                'Cm6': [3, 1, 2, 1, 3, None],
                'Cm7-5': [None, 4, 3, 4,3, None],
                'Cadd9': [0, 3, 0, 2, 3, None],
                'Csus4': [1, 1, 0, 3, 3, None],
                'C7sus4': [3, 6, 3, 5, 3, None],
                'Cdim7': [None, 4, 2, 4, 3, None],
                'C#': [4, 6, 6, 6, 4, None],
                'C#M7': [4, 6, 5, 6, 4, None],
                'C#7': [4, 6, 4, 6, 4, None],
                'C#6': [6, 6, 6, 6, 4, None],
                'C#aug': [None, 2, 2, 3, 4, None],
                'C#m': [4, 5, 6, 6, 4, None],
                'C#mM7': [4, 5, 5, 6, 4, None],
                'C#m7': [4, 5, 4, 6, 4, None],
                'C#m6': [4, 2, 3, 2, 4, None],
                'C#m7-5': [None, 5, 4, 5, 4, None],
                'C#add9': [4, 4, 6, 6, 4, None],
                'C#sus4': [4, 7, 6, 6, 4, None],
                'C#7sus4': [4, 7, 4, 6, 4, None],
                'C#dim7': [None, 5, 3, 5, 4, None],
                'Db': [4, 6, 6, 6, 4, None],
                'DbM7': [4, 6, 5, 6, 4, None],
                'Db7': [4, 6, 4, 6, 4, None],
                'Db6': [6, 6, 6, 6, 4, None],
                'Dbaug': [None, 2, 2, 3, 4, None],
                'Dbm': [4, 5, 6, 6, 4, None],
                'DbmM7': [4, 5, 5, 6, 4, None],
                'Dbm7': [4, 5, 4, 6, 4, None],
                'Dbm6': [4, 2, 3, 2, 4, None],
                'Dbm7-5': [None, 5, 4, 5, 4, None],
                'Dbadd9': [4, 4, 6, 6, 4, None],
                'Dbsus4': [4, 7, 6, 6, 4, None],
                'Db7sus4': [4, 7, 4, 6, 4, None],
                'Dbdim7': [None, 5, 3, 5, 4, None],
                'D': [2, 3, 2, 0, None, None],
                'DM7': [2, 2, 2, 0, None, None],
                'D7': [2, 1, 2, 0, None, None],
                'D6': [2, 0, 2, 0, None, None],
                'Daug': [2, 3, 3, 0, None, None],
                'Dm': [1, 3, 2, 0, None, None],
                'DmM7': [1, 2, 2, 0, None, None],
                'Dm7': [1, 1, 2, 0, None, None],
                'Dm6': [1, 0, 2, 0, None, None],
                'Dm7-5': [1, 1, 1, 0, None, None],
                'Dadd9': [0, 3, 2, 0, None, None],
                'Dsus4': [3, 3, 2, 0, None, None],
                'D7sus4': [3, 1, 2, 0, None, None],
                'Ddim7': [1, 0, 1, 0, None, None],
                'D#': [6, 8, 8, 8, 6, None],
                'D#M7': [6, 8, 7, 8, 6, None],
                'D#7': [6, 8, 6, 8, 6, None],
                'D#6': [8, 8, 8, 8, 6, None],
                'D#aug': [None, 4, 4, 5, 6, None],
                'D#m': [6, 7, 8, 8, 6, None],
                'D#mM7': [6, 7, 7, 8, 6, None],
                'D#m7': [6, 7, 6, 8, 6, None],
                'D#m6': [6, 4, 5, 4, 6, None],
                'D#m7-5': [None, 7, 6, 7, 6, None],
                'D#add9': [6, 6, 8, 8, 6, None],
                'D#sus4': [6, 9, 8, 8, 6, None],
                'D#7sus4': [6, 9, 6, 8, 6, None],
                'D#dim7': [None, 7, 5, 7, 6, None],
                'Eb': [6, 8, 8, 8, 6, None],
                'EbM7': [6, 8, 7, 8, 6, None],
                'Eb7': [6, 8, 6, 8, 6, None],
                'Eb6': [8, 8, 8, 8, 6, None],
                'Ebaug': [None, 4, 4, 5, 6, None],
                'Ebm': [6, 7, 8, 8, 6, None],
                'EbmM7': [6, 7, 7, 8, 6, None],
                'Ebm7': [6, 7, 6, 8, 6, None],
                'Ebm6': [6, 4, 5, 4, 6, None],
                'Ebm7-5': [None, 7, 6, 7, 6, None],
                'Ebadd9': [6, 6, 8, 8, 6, None],
                'Ebsus4': [6, 9, 8, 8, 6, None],
                'Eb7sus4': [6, 9, 6, 8, 6, None],
                'Ebdim7': [None, 7, 5, 7, 6, None],
                'E': [0, 0, 1, 2, 2, 0],
                'EM7': [0, 0, 1, 1, 2, 0],
                'E7': [0, 0, 2, 0, 1, 0],
                'E6': [0, 2, 1, 2, 2, 0],
                'Eaug': [0, 1, 1, 2, None, None],
                'Em': [0, 0, 0, 2, 2, 0],
                'EmM7': [None, 0, 0, 1, 2, 0],
                'Em7': [0, 0, 0, 0, 2, 0],
                'Em6': [0, 2, 0, 2, 2, 0],
                'Em7-5': [0, 3, 0, 2, 1, 0],
                'Eadd9': [0, 0, 1, 4, 2, 0],
                'Esus4': [0, 0, 2, 2, 2, 0],
                'E7sus4': [0, 0, 2, 0, 2, 0],
                'Edim7': [0, 2, 0, 2, 1, 0],
                'F': [1, 1, 2, 3, 3, 1],
                'FM7': [None, 1, 2, 2, None, 1],
                'F7': [1, 1, 2, 1, 3, 1],
                'F6': [None, 3, 2, 3, None, 1],
                'Faug': [1, 2, 2, 3, None, None],
                'Fm': [1, 1, 1, 3, 3, 1],
                'FmM7': [1, 1, 1, 2, 3, 1],
                'Fm7': [1, 1, 1, 1, 3, 1],
                'Fm6': [1, 3, 1, 3, 3, 1],
                'Fm7-5': [None, 0, 1, 1, None, 1],
                'Fadd9': [3, 1, 2, 3, None, None],
                'Fsus4': [1, 1, 3, 3, 3, 1],
                'F7sus4': [1, 1, 3, 1, 3, 1],
                'Fdim7': [1, 0, 1, 0, None, 1],
                'F#': [2, 2, 3, 4, 4, 2],
                'F#M7': [None, 2, 3, 3, None, 2],
                'F#7': [2, 2, 3, 2, 4, 2],
                'F#6': [2, 4, 3, 4, 2, 2],
                'F#aug': [2, 3, 3, 4, None, None],
                'F#m': [2, 2, 2, 4, 4, 2],
                'F#mM7': [2, 2, 2, 3, 4, 2],
                'F#m7': [2, 2, 2, 2, 4, 2],
                'F#m6': [2, 4, 2, 4, 4, 2],
                'F#m7-5': [0, 1, 2, 2, None, 2],
                'F#add9': [4, 2, 3, 4, None, None],
                'F#sus4': [2, 2, 4, 4, 4, 2],
                'F#7sus4': [2, 2, 4, 2, 4, 2],
                'F#dim7': [None, 1, 2, 1, None, 2],
                'Gb': [2, 2, 3, 4, 4, 2],
                'GbM7': [None, 2, 3, 3, None, 2],
                'Gb7': [2, 2, 3, 2, 4, 2],
                'Gb6': [2, 4, 3, 4, 2, 2],
                'Gbaug': [2, 3, 3, 4, None, None],
                'Gbm': [2, 2, 2, 4, 4, 2],
                'GbmM7': [2, 2, 2, 3, 4, 2],
                'Gbm7': [2, 2, 2, 2, 4, 2],
                'Gbm6': [2, 4, 2, 4, 4, 2],
                'Gbm7-5': [0, 1, 2, 2, None, 2],
                'Gbadd9': [4, 2, 3, 4, None, None],
                'Gbsus4': [2, 2, 4, 4, 4, 2],
                'Gb7sus4': [2, 2, 4, 2, 4, 2],
                'Gbdim7': [None, 1, 2, 1, None, 2],
                'G': [3, 0, 0, 0, 2, 3],
                'GM7': [2, 0, 0, 0, 2, 3],
                'G7': [1, 0, 0, 0, 2, 3],
                'G6': [0, 0, 0, 0, 2, 3],
                'Gaug': [3, 4, 4, 5, None, None],
                'Gm': [3, 3, 3, 5, 5, 3],
                'GmM7': [3, 3, 3, 4, 5, 3],
                'Gm7': [3, 3, 3, 3, 5, 3],
                'Gm6': [3, 5, 3, 5, 5, 3],
                'Gm7-5': [None, 2, 3, 3, None, 3],
                'Gadd9': [3, 0, 2, 0, 0, 3],
                'Gsus4': [3, 1, 0, 0, 3, 3],
                'G7sus4': [3, 3, 5, 3, 5, 3],
                'Gdim7': [None, 2, 3, 2, None, 3],
                'G#': [4, 4, 5, 6, 6, 4],
                'G#M7': [None, 4, 5, 5, None, 4],
                'G#7': [4, 4, 5, 4, 6, 4],
                'G#6': [None, 4, 5, 3, None, 4],
                'G#aug': [4, 5, 5, 6, None, None],
                'G#m': [4, 4, 4, 6, 6, 4],
                'G#mM7': [4, 4, 4, 5, 6, 4],
                'G#m7': [4, 4, 4, 4, 6, 4],
                'G#m6': [4, 6, 4, 6, 6, 4],
                'G#m7-5': [0, 3, 4, 4, None, 4],
                'G#add9': [6, 4, 5, 6, None, None],
                'G#sus4': [4, 4, 6, 6, 6, 4],
                'G#7sus4': [4, 4, 6, 4, 6, 4],
                'G#dim7': [None, 3, 4, 3, None, 4],
                'Ab': [4, 4, 5, 6, 6, 4],
                'AbM7': [None, 4, 5, 5, None, 4],
                'Ab7': [4, 4, 5, 4, 6, 4],
                'Ab6': [None, 4, 5, 3, None, 4],
                'Abaug': [4, 5, 5, 6, None, None],
                'Abm': [4, 4, 4, 6, 6, 4],
                'AbmM7': [4, 4, 4, 5, 6, 4],
                'Abm7': [4, 4, 4, 4, 6, 4],
                'Abm6': [4, 6, 4, 6, 6, 4],
                'Abm7-5': [0, 3, 4, 4, None, 4],
                'Abadd9': [6, 4, 5, 6, None, None],
                'Absus4': [4, 4, 6, 6, 6, 4],
                'Ab7sus4': [4, 4, 6, 4, 6, 4],
                'Abdim7': [None, 3, 4, 3, None, 4],
                'A': [0, 2, 2, 2, 0, None],
                'AM7': [0, 2, 1, 2, 0, None],
                'A7': [0, 2, 0, 2, 0, None],
                'A6': [2, 2, 2, 2, 0, None],
                'Aaug': [1, 2, 2, 3, 0, None],
                'Am': [0, 1, 2, 2, 0, None],
                'AmM7': [0, 1, 1, 2, 0, None],
                'Am7': [0, 1, 0, 2, 0, None],
                'AM6': [2, 1, 2, 2, 0, None],
                'Am7-5': [None, 1, 0, 1, 0, None],
                'Aadd9': [0, 0, 2, 2, 0, None],
                'Asus4': [0, 3, 2, 2, 0, None],
                'A7sus4': [0, 3, 0,2, 0, None],
                'Adim7': [2, 1, 2, 1, 0, None],
                'A#': [1, 3, 3, 3, 1, 0, None],
                'A#M7': [1, 3, 2, 3, 1, None],
                'A#7': [1, 3, 1, 3, 1, None],
                'A#6': [3, 3, 3, 3, 1, None],
                'A#aug': [6, 7, 7, 8, None, None],
                'A#m': [1, 2, 3, 3, 1, None],
                'A#mM7': [1, 2, 2, 3, 1, None],
                'A#m7': [1, 2, 1, 3, 1, None],
                'A#m6': [3, 2, 3, 1, 1, None],
                'A#m7-5': [None, 2, 1, 2, 1, None],
                'A#add9': [1, 1, 3, 3, 1, None],
                'A#sus4': [1, 4, 3, 3, 1, None],
                'A#7sus4': [1, 4, 1, 3, 1, None],
                'A#dim7': [0, 2, 0, 2, 1, None],
                'Bb': [1, 3, 3, 3, 1, 0, None],
                'BbM7': [1, 3, 2, 3, 1, None],
                'Bb7': [1, 3, 1, 3, 1, None],
                'Bb6': [3, 3, 3, 3, 1, None],
                'Bbaug': [6, 7, 7, 8, None, None],
                'Bbm': [1, 2, 3, 3, 1, None],
                'BbmM7': [1, 2, 2, 3, 1, None],
                'Bbm7': [1, 2, 1, 3, 1, None],
                'Bbm6': [3, 2, 3, 1, 1, None],
                'Bbm7-5': [None, 2, 1, 2, 1, None],
                'Bbadd9': [1, 1, 3, 3, 1, None],
                'Bbsus4': [1, 4, 3, 3, 1, None],
                'Bb7sus4': [1, 4, 1, 3, 1, None],
                'Bbdim7': [0, 2, 0, 2, 1, None],
                'B': [2, 4, 4, 4, 2, None],
                'BM7': [2, 4, 3, 4, 2, None],
                'B7': [2, 0, 2, 1, 2, None],
                'B6': [4, 4, 4, 4, 2, None],
                'Baug': [None, 0, 0, 1, 2, None],
                'Bm': [2, 3, 4, 4, 2, None],
                'BmM7': [2, 3, 3, 4, 2, None],
                'Bm7': [2, 3, 2, 4, 2, None],
                'Bm6': [3, 0, 2, 0, 3, None],
                'Bm7-5': [None, 3, 2, 3, 2, None],
                'Badd9': [1, 1, 3, 3, 1, None],
                'Bsus4': [2, 5, 4, 4, 2, None],
                'B7sus4': [2, 5, 2, 4, 2, None],
                'Bdim7': [None, 3, 1, 3, 2, None],
        }
