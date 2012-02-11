from util import *

def reduce_pattern(pattern):
    if(type(pattern) is not list):
        return pattern
                    
    if(len(pattern) == 1):
        return reduce_pattern(pattern[0])

    sub_patterns = [reduce_pattern(sub_pattern) for sub_pattern in pattern]
        
    lengths = [type(sub_pattern) is not list and 1 or len(sub_pattern) for sub_pattern in sub_patterns]
    
    def get_len_group_sizes(lens, cur, res):
        if(lens[0] == cur):
            res[-1] += 1
        else:
            cur = lens[0]
            res.append(1)
    
        return len(lens) == 1 and res[::-1] or get_len_group_sizes(lens[1:], cur, res)

    len_group_sizes = get_len_group_sizes(lengths[1:], lengths[0], [1])

    g = gcd(len_group_sizes)

    result = [shallow_flatten(sub_patterns[n:n+g]) for n in range(0, len(sub_patterns), g)]

    if(len(result) == 1):
        result = result[0]
            
    return result


class Beat(object):

    def __init__(self, bpm, sounds, patterns):
        self.bpm, self.sounds, self.patterns = bpm, sounds, patterns

        
    def to_raw(self):
        sec_per_beat = 60.0 / self.bpm
        total_time = 16 * sec_per_beat

        self.reduce

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
            
        res = [res_for(pattern[i], interval, offset) for i in xrange(len(pattern)) if pattern[i]]
        
        return flatten(res)


    def reduce(self):
        self.patterns = [reduce_pattern(pattern) for pattern in self.patterns]

        
