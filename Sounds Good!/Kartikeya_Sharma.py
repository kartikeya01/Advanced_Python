#
# Assignment4_Template.py, "Sounds Good!"
#
# Name(s): Kartikeya Sharma
#
import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # needed in 2015

# a function to get started with a reminder 
# about list comprehensions...

def three_ize( L ):
    """ three_ize is the motto of the green CS 5 alien.
        It's also a function that takes in a list and
        returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [ 3*x for x in L ]
    return LC

# Function to write #1:  scale
def scale(L, scale_factor):
    """This is a function which expands(amplifies) a set of integers
       The theory behind this function can be used to increase the
       volume of the .wav file. It multiplies L by the scale_factor
    """
    return [ x*scale_factor for x in L ]
  
# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index( L ):
    """ three_ize_by_index has the same I/O behavior as three_ize
        but it uses the INDEX of each element, instead of
        using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [ 3*L[i] for i in range(N) ]
    return LC

# Function to write #2:  add_2
def add_2(L, M):
    """This simple function adds every element in L with each element in M.
        I am able to do this by using [] to specify the position which must be
        added. With a for loop, I am able to add all the elements in L with M.
        The range insures that the group(L or M) with the lowest no. of 
        elements are fully added.
    """
    N = min( len(L), len(M) )
    return [ L[i] + M[i] for i in range(N) ]

# Function to write #3:  add_3
def add_3(L, M, P):
    """This is similiar to the function: add_2 except with three variables now.
        The concept remains similar
    """
    N = min( len(L), len(M), len(P) )
    return [ L[i] + M[i] + P[i] for i in range(N) ]

# Function to write #4:  add_scale_2
def add_scale_2(L, M, L_scale, M_scale):
    """This function combines the amplifying function with the previous
       add funtions. Each scale is exclusive to the letter in-front of it:
       L_scale with L and M_scale with M.
       After the scale has been multiplied with the list, both lists are
       added: L + M. Again, the for loop insures that each element in the list
       is added with each element in the other list respective of position.
    """
    N = min( len(L), len(M) )
    a = [ x*L_scale for x in L ]
    b = [ x*M_scale for x in M ]
    return [ a[i] + b[i] for i in range(N) ] 

# Helper function:  randomize
def randomize( x, chance_of_replacing ):
    """ randomize takes in an original value, x
        and a fraction named chance_of_replacing.

        With the "chance_of_replacing" chance, it
        should return a random float from -32767 to 32767.

        Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0,1)
    if r < chance_of_replacing:
        return random.uniform(-32768,32767)
    else:
        return x

# Function to write #5:  replace_some
def replace_some(L, chance_of_replacing):
    """This function uses the help of the previous function: randomize
       to replace or not replace each element in the list L.
    """
    LC = [ randomize( x, chance_of_replacing ) for x in L ]
    return LC

#
# below are functions that relate to sound-processing ...
#

# a function to make sure everything is working
def test():
    """ a test function that plays swfaith.wav
        You'll need swfailt.wav in this folder.
    """
    play( 'swfaith.wav' )

# The example changeSpeed function
def changeSpeed(filename, newsr):
    """ changeSpeed allows the user to change an audio file's speed
        input: filename, the name of the original file
               newsr, the *new* sampling rate in samples per second
        output: no return value; creates and plays the file 'out.wav'
    """
    samps, sr = readwav(filename)

    print "The first 10 sound-pressure samples are\n", samps[:10]
    print "The original number of samples per second is", sr
    
    newsamps = samps
    writewav( newsamps, newsr, "out.wav" )
    
    print "You have initiated SPEEDCHANGE!!"
    print "\nPlaying new sound..."
    play( 'out.wav' )

# The example flipflop function
def flipflop(filename):
    """ flipflop swaps the halves of an audio file
        input: filename, the name of the original file
        output: no return value, but
                this creates the sound file 'out.wav'
                and plays it
    """
    print "Playing the original sound..."
    play(filename)
    
    print "Reading in the sound data..."
    samps, sr = readwav(filename)
    
    print "You have initiated FLIPFLOP!!"
    print "Computing new sound..."
    # this gets the midpoint and calls it x
    x = len(samps)/2
    newsamps = samps[x:] + samps[:x] # flip flop
    newsr = sr                       # no change to the sr
    
    writewav( newsamps, newsr, "out.wav" )
    print "Playing new sound..."
    play( 'out.wav' )

# Sound function to write #1:  reverse
def reverse(filename):
    """reverse literally reverses the sound which the user has input
       instead of "filname". This is done by simply redefining the new
       sample rate and playing it in reverse with [::-1].
       Then, writewav is able to interpret this and edit "out.wav" and
       play it according to the new sample rate integer: sr.
    """
    print "Playing the original sound..."
    play(filename)
    
    print "Reading in the sound data..."
    samps, sr = readwav(filename)
    
    print "You have initiated REVERSE!!"
    print "Computing new sound..."
    newsamps = samps[::-1]  
    newsr = sr
    
    writewav( newsamps, newsr, "out.wav" )
    print "Playing new sound..."
    play( 'out.wav' )

# Sound function to write #2:  volume
def volume(filename, scale_factor):
    """Volume uses the same concept as the function: scale.
       x represents the number of samples. we are then able to multiply
       this by the scale_factor which the user has input. This is then
       the new value for samps which writewav() plays as "out.wav"
    """
    print "Playing the original sound..."
    play(filename)
    
    print "Reading in the sound data..."
    samps, sr = readwav(filename)
    
    print "You have initiated VOLUME CHANGE!!"
    print "Computing new sound..."
    x = len(samps)
    newsamps = [ x*scale_factor for x in samps ]
    newsr = sr

    writewav( newsamps, newsr, "out.wav" )
    print "Playing new sound..."
    play( 'out.wav' )

# Sound function to write #3:  static
def static(filename, probablity_of_static):
    """static uses the same concept as randomize and replace_some. 
       replace_some basically replaces or doesn't (depending on the random
       outcome) each element in the samps , using the function randomize. By 
       doing so to the new sample rate (newsamps), writewav() is able to output the new samples to
       "out.wav" thus creating this "static" noise which can be altered by inputing
       different values. 
    """
    print "Playing the original sound..."
    play(filename)
    
    print "Reading in the sound data..."
    samps, sr = readwav(filename)
    
    print "You have initiated STATIC!!"
    print "Computing new sound..."
    newsamps = [ randomize( x, probablity_of_static ) for x in samps ]
    newsr = sr
    
    writewav( newsamps, newsr, "out.wav" )
    print "Playing new sound..."
    play( 'out.wav' )

# Sound function to write #4:  overlay
def overlay (filename1, filename2, scale_factor1, scale_factor2):
    """This function is complicated in the sense that instead of one
       .wav file, we must deal with two. This means two filenames, two
       sample rates. Two sample rates mean that the new sample rate is
       the sum of both, just like in the function add_scale_2. The newsr
       is also divided by two since if we only add both sample rates, the speed
       will also increase roughly by 2. The reason for this is because There will
       be more samples per second. In order to make it similar to one .wav, we can
       divide newsr by 2 to make the overlay sound clearer.
    """
    print "Playing the first sound..."
    play(filename1)
    
    print "Playing the second sound..."
    play(filename2)
    
    print "Reading in the sound data..."
    samps1, sr1 = readwav(filename1)
    samps2, sr2 = readwav(filename2)

    N = min( len(samps1), len(samps2) )
    
    a = [ x*scale_factor1 for x in samps1 ]
    b = [ x*scale_factor2 for x in samps2 ]
    
    newsamps = [ a[i] + b[i] for i in range(N) ] 
    newsr = (sr1 + sr2)/2                   
    
    print "You have initiated AN OVERLAY!!"
    print "Computing new sound..."
    writewav( newsamps, newsr, "out.wav" )
    print "Playing new sound..."
    play( 'out.wav' )



# Sound function to write #5:  echo
def echo(filename, time_delay):
    """echo overlays the same sound on top of an existing playing sound
       and creates an echo. I was able to add delay to it by concatinating [0]'s
       to samps2. I also used the function add_scale_2 to define the new sappling speed.
       Since add_scale_2 has 4 inputs, I pasted time_delay twice to multiply the delay to
       both sams1 and samps2, With sams2 starting len(samps1)*time_delay after.
    
    """
    print "Playing the first sound..."
    play(filename)

    
    print "Reading in the sound data..."
    samps1, sr = readwav(filename)
    samps2 = [0] * int(len(samps1)*time_delay) + samps1
    
    
    newsamps = add_scale_2(samps1, samps2, time_delay, time_delay) 
    newsr = sr 
    
    print "You have initiated AN ECHO!!"
    print "Computing new sound..."
    writewav( newsamps, newsr, "out.wav" )
    print "Playing new sound..."
    play( 'out.wav' )
    


#a function to make sure everything is working



flipflop("swfaith.wav")

changeSpeed( "swfaith.wav", 44100 )

reverse('swfaith.wav')

volume( 'swfaith.wav', .1 )

static('swfaith.wav', .05)

overlay( 'swfaith.wav', 'swnotry.wav', 0.5, 2.5)

echo( 'swfaith.wav', .1 )