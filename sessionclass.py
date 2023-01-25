# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 17:51:35 2023

@author: rolfe
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg    

class BaseClass():
    def classname(self): 
        """
        Nice to have for error messages
        """
        return __class__.__name__
    
class Session(BaseClass):
    """
    Contains everything that enables a session 
    These data will be loaded/saved to storage for retrieval 
    
    """
    def __init__(self, mido):
        
        self._chords=None
        
    
    class MidiChannels:
        Chord_Out=1 
        chordDetection_in=15 #chord detection using midi "notes" not control messages
        bass_in=2
    
    def addChords(self, chordsList):
        """
        This is not finished ...
        """
        
        self._chords=chordsList
        
        print("Chords added:") 
        for i, chord in enumerate(self._chords):
            print("{} - {}".format(i, chord.name))
        

    def start(self):
        """
        """
        
        if self._chords==None:
            
            print("{}".format(self.classname()))              
            print("add some chords first!")
            
        
    def save(self):
        pass
    
    def printMeny(self):
        """
        possible sessions
        """
        print(" --- MENU ---")
        print("1. open ports + testout")
        print("2. load a chordsceme")
        print("3. register a new chordsceme")
        print("4. start message loop")
            
        print("5. exit")
        
    
        
class Misc():
    
    class MidiNotes: ## insert correct notes   
        """
        https://studiocode.dev/resources/midi-middle-c/

        """ 
        c4_middle = 60
        c4_sharp=61
        d4 = 62
        d4_sharp=63
        e4=64
        f4=65
        g4=67
        
    
    def showkeyb():
        img = mpimg.imread('keyb.png')
        plt.imshow(img)
        plt.show()

    
    #make a filepath if it not exist
    def functionalityreport(chords, controls):
        """
        Prints all the chords and controls loaded in this session 
        
        """
        print("\n")
        print("--- CHORDS registered for controller messages in this session---")
        
        for c in chords:
            print("chord name: \t", c.name + " - " + str(c.index))   
            print("triggered by: \t", c.msgtype)
            print("note_cc: \t\t", c.note_cc)
            print("action: \t\t", c.action)
        
        print("\n")
                 
        print("--- CONTROLS registered for controller messages this session ---")
        for c in controls:        
            print("control name: \t", c.name)   
            print("triggered by: \t", c.msgtype)
            print("note_cc: \t\t", c.note_cc)
            print("action: \t\t", c.action)
        
        print("\n")
  
    
    def classname(self): return __class__.__name__
    
    def isControlChange(msg):
        return msg.type == 'control_change'
    
    def isNote(msg):
        return msg.type == 'note_on' or msg.type == 'note_off'
        #return msg.type in ('note_on', 'note_off') # alternative
    
    def getListofUndefinedCC():
        t1=" Undefined MIDI CC List"

        t2="CC 3 "
        t3="CC 9 "
        t4="CC 14-15 "
        t5="CC 20-31 "
        t6="CC 85-87 "
        t7="CC 89-90 "
        t8="CC 102-119 "
        return t1+t2+t3+t4+t5+t6+t7+t8
        
        
    def listClassMemebers(theObject):
        
        for property, value in vars(theObject).items():
            print(property, ":", value)
    
    def printUserprotertiesClass(clas):
        print([ m for m in dir(clas) if not m.startswith('__')])
    
    def clearSpyderTerminal():
        print("\033[H\033[J")  
    

    
    def printTitle(mido): # the app's name .... 
        print("\033[H\033[J")  
        print("Mido version:   \t", mido.__version__)
        print("  / ____| |                 | |")
        print(" | |    | |__   ___  _ __ __| |")
        print(" | |__  | '_ \ / _ \| '__/ _` |")
        print(" \_____ |_| |_|\___/|_|  \__,_|")    
     ### a testing function ... shall be removed and replaced with Chord-Service  
     
     
    def overviewChords():
        return """
                    https://www.pianochord.org/c5.html
            
            C - C major (C△)
            Cm - C minor
            C7 - C dominant seventh
            Cm7 - C minor seventh
            
            Cmaj7 - C major seventh (C△7)
            CmM7 - C minor major seventh
            
            C6 - C major sixth
            Cm6 - C minor sixth
            C6/9 - C sixth/ninth (sixth added ninth)
            
            C5 - C fifth   (interval - 2 notes)
            
            C9 - C dominant ninth
            Cm9 - C minor ninth
            Cmaj9 - C major ninth
            
            C11 - C eleventh
            Cm11 - C minor eleventh
            
            C13 - C thirteenth
            Cm13 - C minor thirteenth
            Cmaj13 - C major thirteenth
            
            Cadd - C add
            C7-5 - C seven minus five
            C7+5 - C seven plus five
            Csus - C suspended
            
            Cdim - C diminished (C°)
            Cdim7 - C diminished seventh (C°7)
            Cm7b5 - C minor seventh flat five (Cø)
            
            Caug - C augmented (C+)
            Caug7 - C augmented seventh
        """
        

     
     
     
    