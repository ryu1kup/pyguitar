# pyguitar
A brief class for playing guitar chords

# usage
You can play guitar chords much easily by instantiating Guitar object and using its method.
```
from pyguitar import Guitar

g = Guitar()
time = 1 # time per a note [sec]
chords = ['F', 'G', 'C', 'C']
g.play_chords(chords, time)
```
