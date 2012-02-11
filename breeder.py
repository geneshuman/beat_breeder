#!/usr/bin/env python

import sys, shelve, random
from phrase import *
from mutate import *

# load swarm
swarm = shelve.open("swarm.brd")

# if doesnt exist, initialize it
if(not swarm):
    print "initializing swarm"
    config = {"population_size": 20, "generation": 0, "necessary_ratings": 3, "num_ratings": 0, "parent_pool_size": 5, "num_rating_exterpolation_pts": 2}
    swarm["config"] = config
    
    for i in xrange(config["population_size"]):
        phrase = generate_random_phrase()
        phrase.swarm_idx = i
        swarm[str(i)] = phrase
        
    print "swarm initialized"

config = swarm["config"]

# begin main loop
while(True):
    try:
        raw_input("> press enter to begin")
        # play & rate sounds
        population_size = config["population_size"]
        phrase_offset = config["generation"] * population_size        
        while(config["num_ratings"] != config["necessary_ratings"]):
            next_phrase = phrase_offset + random.randint(0, population_size - 1)
            phrase = swarm[str(next_phrase)]
            
            print "generation:", config["generation"]
            print "num_rated_phrases:", config["num_ratings"]
            print "phrase idx:", next_phrase
            phrase.play()
            time.sleep(0.5)
    
            rating = int(raw_input("> rating(123..0):"))
            phrase.rating = (phrase.num_ratings * phrase.rating + rating) / (phrase.num_ratings + 1)
            phrase.num_ratings += 1
            swarm[str(next_phrase)] = phrase
    
            config["num_ratings"] += 1
            swarm["config"] = config

        print "done rating phrases"

        # find all rated phrases
        rated_phrases = [swarm[str(phrase_offset + i)] for i in xrange(population_size) if swarm[str(phrase_offset + i)].num_ratings != 0]
        rated_indexes = set([phrase.swarm_idx for phrase in rated_phrases])

        # print rated_indexes
        
        # extrapolate ratings to entire swarm
        print "extrapolation ratings"
        for i in xrange(population_size):
            phrase = swarm[str(phrase_offset + i)]
            if(phrase.swarm_idx in rated_indexes):
                continue
            ratings = []
            for j in xrange(config["num_rating_exterpolation_pts"]):
                pt = rated_phrases[random.randint(0, len(rated_phrases) - 1)]
                ratings.append((1.0 - phrase_distance(pt, phrase)) * pt.rating)

            phrase.rating = sum(ratings) / len(ratings);
            # print "rating phrase:", phrase.swarm_idx, "with", phrase.rating
            swarm[str(phrase.swarm_idx)] = phrase                            
            
        # top rated phrases -> parent_pool
        print "getting parents for the next generation"
        current_phrases = [swarm[str(phrase_offset + i)] for i in xrange(population_size)]
        parent_pool = sorted(current_phrases, key = lambda phrase: phrase.rating)[::-1][0:config["parent_pool_size"]]
        # print [(phrase.swarm_idx, phrase.rating) for phrase in parent_pool]

        # breed swarm
        print "breeding swarm"
        for i in xrange(population_size):
            parent1 = parent_pool[random.randint(0, len(parent_pool) - 1)]
            parent2 = parent_pool[random.randint(0, len(parent_pool) - 1)]
            # print "breeding", parent1.swarm_idx, parent2.swarm_idx
            child = breed(parent1, parent2)
            idx = phrase_offset + population_size + i
            child.swarm_idx = idx
            swarm[str(idx)] = child
            # print "= child", child.swarm_idx

        # increase generation
        config["generation"] += 1
        config["num_ratings"] = 0
        swarm["config"] = config

    except (KeyboardInterrupt, SystemExit):
        print "exiting"
        sys.exit(0)

