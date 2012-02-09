#!/usr/bin/env python

import sys, time
from output import *
from beat import *

initSoundEngine()

beat = Beat(120, {0:None, 1: "samples/LT7D3.WAV"}, [[1,[1,1,1,1,1,1,1,1],1],0,0,0,1,1,1,1,1,1,1,1,1,1,1,1])

print beat.to_raw()

playRawBeat(beat.to_raw())

# give last sounds time to finish
time.sleep(0.5)
