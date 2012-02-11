#!/usr/bin/env python

import sys, time, random
from output import *
from phrase import *
from mutate import *

population_size = 1000
num_samples = 4

initSoundEngine()

track1 = [[1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]]
track2 = [[(1,3),3,(2,3),3,3,[(1,3),3,3,3],(2,3),3],[(1,3),3,(2,3),3,3,[(1,3),1],(2,3),3],[(1,3),3,(2,3),3,3,(1,3),(2,3),3],[(1,3),3,(2,3),[3,2],[3,2],(3,1),(3,2),(3,1)]]

track1 = mutate(track1)

phrase = Phrase(120, {0:None, 1: "samples/BT3AADA.WAV", 2:"samples/HANDCLP1.WAV", 3:"samples/CLOP1.WAV"}, [track1])

playRawPhrase(phrase.sounds, phrase.to_raw())

# give last sounds time to finish
time.sleep(0.5)
    

# while(true)
#    while(population ! judged)
#      judge population
#    breed population(cull results)
#
