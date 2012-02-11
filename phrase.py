from util import *

def reduce_track(track):
    if(type(track) is not list):
        return track
                    
    if(len(track) == 1):
        return reduce_track(track[0])

    sub_tracks = [reduce_track(sub_track) for sub_track in track]
        
    lengths = [type(sub_track) is not list and 1 or len(sub_track) for sub_track in sub_tracks]
    
    def get_len_group_sizes(lens, cur, res):
        if(lens[0] == cur):
            res[-1] += 1
        else:
            cur = lens[0]
            res.append(1)
    
        return len(lens) == 1 and res[::-1] or get_len_group_sizes(lens[1:], cur, res)

    len_group_sizes = get_len_group_sizes(lengths[1:], lengths[0], [1])

    g = gcd(len_group_sizes)

    result = [shallow_flatten(sub_tracks[n:n+g]) for n in range(0, len(sub_tracks), g)]

    if(len(result) == 1):
        result = result[0]
            
    return result


class Phrase(object):

    def __init__(self, bpm, sounds, tracks):
        self.bpm, self.sounds, self.tracks = bpm, sounds, tracks

        
    def to_raw(self):
        sec_per_beat = 60.0 / self.bpm
        total_time = 16 * sec_per_beat

        self.reduce

        raw_events = flatten([self.to_raw_internal(track, 0, total_time) for track in self.tracks])
    
        return sorted(raw_events, key = lambda event: event["time"])


    def to_raw_internal(self, track, offset, total):
        interval = total / len(track)

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
            
        res = [res_for(track[i], interval, offset) for i in xrange(len(track)) if track[i]]
        
        return flatten(res)


    def reduce(self):
        self.tracks = [reduce_track(track) for track in self.tracks]

        
