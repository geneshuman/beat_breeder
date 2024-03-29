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
    # print "double_base_node"

    track = Phrase.reduce_track(track)
    i = random.randint(0, len(track) - 1)
    track[i] = [track[i], track[i]]

    return Phrase.reduce_track(track)


def triple_base_node(track):
    # print "triple_base_node"

    track = Phrase.reduce_track(track)
    i = random.randint(0, len(track) - 1)
    track[i] = [track[i], track[i]]

    return Phrase.reduce_track(track)


def drop_base_node(track):
    # print "drop_base_node"

    track = Phrase.reduce_track(track)
    i = random.randint(0, len(track) - 1)
    track[i] = []

    return Phrase.reduce_track(track)


def swap_base_nodes(track):
    # print "swap_base_node"

    track = Phrase.reduce_track(track)
    i = random.randint(0, len(track) - 1)
    tmp = track[i]
    track[i] = track[i - 1]
    track[i-1] = tmp

    return Phrase.reduce_track(track)


def replace_following_node(track):
    # print "replace_following_node"

    track = Phrase.reduce_track(track)
    i = random.randint(0, len(track) - 1)
    track[(i + 1) % len(track)] = track[i]

    return Phrase.reduce_track(track)


def replace_preceeding_node(track):
    # print "replace_preceeding_node"

    track = Phrase.reduce_track(track)
    i = random.randint(0, len(track) - 1)
    track[i - 1] = track[i]

    return Phrase.reduce_track(track)


mutations = [(.7, double_base_node),
             (.4, triple_base_node),
             (.2, drop_base_node),
             (.4, replace_following_node),
             (.4, replace_preceeding_node),
             (.6, swap_base_nodes)]
