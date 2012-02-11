import random, time
from beat import *

random.seed(time.time())

def mutate(pattern):
    func = False
    
    while(not func):
        i = random.randint(0,len(mutations) - 1)
        mutation = mutations[i]
        
        f = random.random()
        if(f < mutation[0]):
            func = mutation[1]
            
    return func(pattern)


def double_base_event(pattern):
    print "double_base_event"
    pattern = reduce_pattern(pattern)
    i = random.randint(0, len(pattern) - 1)    
    pattern[i] = [pattern[i], pattern[i]]

    return pattern


mutations = [(.5, double_base_event)]
