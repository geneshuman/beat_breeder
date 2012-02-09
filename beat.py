from util import *

class Beat(object):

    def __init__(self, bpm, sounds, pattern):
        self.bpm, self.sounds, self.pattern = bpm, sounds, pattern        

        
    def to_raw(self):
        sec_per_beat = 60.0 / self.bpm
        total_time = 16 * sec_per_beat

        return self.to_raw_internal(self.pattern, 0, total_time)


    def to_raw_internal(self, pattern, offset, total):
        interval = total / len(pattern)

        def sounds_for(p):
            if(type(p) is tuple):
                return [self.sounds[e] for e in p]
            else:
                return [self.sounds[p]]

        res = [type(pattern[i]) is list and self.to_raw_internal(pattern[i], interval * i + offset, interval) or {"time": interval * i + offset, "sounds":sounds_for(pattern[i])} for i in xrange(len(pattern)) if pattern[i]]
        
        return flatten(res)

