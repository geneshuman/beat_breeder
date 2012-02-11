import random, time
from phrase import *

random.seed(time.time())


def mutate(track):
    func = False
    
    while(not func):
        i = random.randint(0,len(mutations) - 1)
        mutation = mutations[i]
        
        f = random.random()
        if(f < mutation[0]):
            func = mutation[1]
            
    return func(track)


def double_base_node(track):
    print "double_base_node"
    track = reduce_track(track)
    i = random.randint(0, len(track) - 1)    
    track[i] = [track[i], track[i]]

    return reduce_track(track)


def triple_base_node(track):
    print "triple_base_node"
    track = reduce_track(track)
    i = random.randint(0, len(track) - 1)    
    track[i] = [track[i], track[i]]

    return reduce_track(track)


def drop_base_node(track):
    print "drop_base_node"
    track = reduce_track(track)
    i = random.randint(0, len(track) - 1)    
    track[i] = []

    return reduce_track(track)


def swap_base_nodes(track):
    print "swap_base_node"
    track = reduce_track(track)
    i = random.randint(0, len(track) - 1)
    tmp = track[i]
    track[i] = track[i - 1]
    track[i-1] = tmp

    return reduce_track(track)


mutations = [(.5, double_base_node), (.3, triple_base_node), (.7, drop_base_node), (.5, swap_base_nodes)]




