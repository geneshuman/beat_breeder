#!/usr/bin/env python

import sys, time, random
from output import *
from beat import *

population_size = 1000
num_samples = 4

initSoundEngine()

#beat = Beat(120, {0:None, 1: "samples/BT3AADA.WAV", 2:"samples/HANDCLP1.WAV", 3:"samples/CLOP1.WAV"}, [[(1,3),3,(2,3),3,3,[(1,3),3,3,3],(2,3),3],[(1,3),3,(2,3),3,3,[(1,3),1],(2,3),3],[(1,3),3,(2,3),3,3,(1,3),(2,3),3],[(1,3),3,(2,3),[3,2],[3,2],(3,1),(3,2),(3,2)]])


# generate random population
random.seed(time.time())
def gen_random_node(max_size, p):
    num = random.randint(1, max_size)
    return [random.random() < p and gen_random_node(max_size, p * p) or random.randint(0, num_samples - 1) for i in xrange(num)]

#nodes = [gen_random_node(2, .8) for i in xrange(16)]
#print nodes

#beat = Beat(120, {0:None, 1: "samples/BT3AADA.WAV", 2:"samples/HANDCLP1.WAV", 3:"samples/CLOP1.WAV"}, nodes)

beat1 = Beat(120, {0:None, 1: "samples/BT3AADA.WAV", 2:"samples/HANDCLP1.WAV", 3:"samples/CLOP1.WAV"}, [[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
                                                                                                        [[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3],[3,3,3,3,3,3,3,3]]])

playRawBeat(beat1.sounds, beat1.to_raw())

# give last sounds time to finish
time.sleep(0.5)
    

# while(true)
#    while(population ! judged)
#      judge population
#    breed population(cull results)
#
