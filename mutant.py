#!/usr/bin/env python

import sys, time
from output import *
from beat import *

initSoundEngine()

beat = Beat(120, {0:None, 1: "samples/BT3AADA.WAV", 2:"samples/HANDCLP1.WAV", 3:"samples/CLOP1.WAV"}, [[(1,3),3,(2,3),3,3,[(1,3),3,3,3],(2,3),3],[(1,3),3,(2,3),3,3,[(1,3),1],(2,3),3],[(1,3),3,(2,3),3,3,(1,3),(2,3),3],[(1,3),3,(2,3),[3,2],[3,2],(3,1),(3,2),(3,2)]])

print beat.to_raw()

playRawBeat(beat.to_raw())

# give last sounds time to finish
time.sleep(0.5)
