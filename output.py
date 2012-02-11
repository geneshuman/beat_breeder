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


def initSoundEngine():
     try:
         pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
     except pygame.error, exc:
         print >>sys.stderr, "Could not initialize sound system: %s" % exc
         system.exit(0)         

         
def playSample(sample_name):
    loaded_samples[sample_name].play()


def loadSamples(samples):
    for sample in samples:
        if(sample):            
            loaded_samples[sample] = pygame.mixer.Sound(sample)

            
def playRawBeat(raw_beat):
    try:
        playsound(sys.argv[1])
    except pygame.error, exc:
        print >>sys.stderr, "Could not play sound file: %s" % soundfile
        print exc


def playRawBeat(samples, raw_beat):
    loadSamples(samples.values())
    start_time = time.time() + 0.1
    t_evt = threading.Event()
    while(len(raw_beat) != 0):
        local_time = time.time() - start_time
        evt = raw_beat[0]
        raw_beat = raw_beat[1:]
        if(local_time < evt["time"]):
            t_evt.wait(evt["time"] - local_time)
        local_time = time.time() - start_time
        for sound in evt["sounds"]:
            playSample(sound)

                   
        
