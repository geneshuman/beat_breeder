import time
import sys
import pygame
import threading

# global constants
FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples
FRAMERATE = 30 # how often to check if playback has finished

loaded_samples = {}

# initialize engine
def initSoundEngine():
     try:
         pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
     except pygame.error, exc:
         print >>sys.stderr, "Could not initialize sound system: %s" % exc
         system.exit(0)         

         
# play a sample         
def playSample(sample_name):
    loaded_samples[sample_name].play()

    
# load a sample into preloaded database
def loadSamples(samples):
    for sample in samples:
        if(sample):            
            loaded_samples[sample] = pygame.mixer.Sound(sample)


# play a raw phrase 
def playRawPhrase(samples, raw_phrase):
    loadSamples(samples.values())
    
    start_time = time.time() + 0.1 # add 0.1 to reduce initial stuttering
    
    t_evt = threading.Event()
    while(len(raw_phrase) != 0):
        local_time = time.time() - start_time
        evt = raw_phrase[0]
        raw_phrase = raw_phrase[1:]
        if(local_time < evt["time"]):
            t_evt.wait(evt["time"] - local_time)
        local_time = time.time() - start_time
        for sound in evt["sounds"]:
            playSample(sound)

                   
        
