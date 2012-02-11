from util import *

class Beat(object):

    def __init__(self, bpm, sounds, patterns):
        self.bpm, self.sounds, self.patterns = bpm, sounds, patterns

        
    def to_raw(self):
        sec_per_beat = 60.0 / self.bpm
        total_time = 16 * sec_per_beat

        raw_beats = flatten([self.to_raw_internal(pattern, 0, total_time) for pattern in self.patterns])
    
        return sorted(raw_beats, key = lambda beat: beat["time"])


    def to_raw_internal(self, pattern, offset, total):
        interval = total / len(pattern)

        def sounds_for(p):
            if(type(p) is tuple):
                return [self.sounds[e] for e in p]
            else:
                return [self.sounds[p]]

        def res_for(p, intv, off):
            if(type(p) is list):
                return self.to_raw_internal(p, intv * i + off, intv)
            else:
                return {"time": intv * i + off, "sounds":sounds_for(p)}
            
        res = [res_for(pattern[i], interval, offset)  for i in xrange(len(pattern)) if pattern[i]]
        
        return flatten(res)

