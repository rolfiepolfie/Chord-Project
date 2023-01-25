# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 06:19:09 2022

@author: rolfe
"""
### chord_classes2


from typing import Any, List



class CCvalues:
    """
    defines values that follows a CC (Control Change) message (CC, value)
    """
    
    ALL_SOUND_OFF = 120 #check midi spec for this one 
    RESET_ALL_CONTROLLERS = 121
    ALL_NOTES_OFF = 123
   
    # 122 Local Control On/Off  -  interrupt the internal control path between the keyboard and the sound-generating circuitry
    # 123 All Notes Off
    # 124 Omni Mode Off
    # 125 Omni Mode On
    # 126 Poly Mode On/Off
    # 127 Poly Mode Mono Off

    #https://www.lim.di.unimi.it/IEEE/MIDI/SOT0.HTM#Local


"""
All Sound Off (CC 120)

Mutes all sounding notes that were turned on by received Note On messages, 
and which haven't yet been turned off by respective Note Off messages. 
This message is not supposed to mute any notes that the musician is playing on the local keyboard. 
So, if a device can't distinguish between notes played via its MIDI IN and notes played on the local keyboard, 
it should not implement All Sound Off.

Note: The difference between this message and All Notes Off is that this message immediately mutes all sound 
on the device regardless of whether the Hold Pedal is on, and mutes the sound quickly regardless 
of any lengthy VCA release times. It's often used by sequencers to quickly mute all sound when 
the musician presses "Stop" in the middle of a song.

All Notes Off (CC 123)

Turns off all notes that were turned on by received Note On messages, 
and which haven't yet been turned off by respective Note Off messages. 
This message is not supposed to turn off any notes that the musician is playing on 
the local keyboard. So, if a device can't distinguish between notes played via its 
MIDI IN and notes played on the local keyboard, it should not implement 
All Notes Off. Furthermore, if a device is in Omni On state, it should ignore this message on any channel.

Note: If the device's Hold Pedal controller is on, the notes aren't actually released until the Hold Pedal is turned off. See All Sound Off controller message for turning off the sound of these notes immediately.    

Reset All Controllers (CC 121)
---
---
---

"""    


""""
Undefined MIDI CC List
In case you just need a MIDI CC List of undefined MIDI CCs to attach an effect/parameter/etc. to a MIDI Controller, here is one with the by default undefined MIDI CCs:

CC 3
CC 9
CC 14-15
CC 20-31
CC 85-87
CC 89-90
CC 102-119
"""


class GmSounds():
    
    def _class_to_list(the_object: Any) -> List[str]:
        """
        gets the public attributes of an object, if possible 
        the creation order is preserved
        this funtion's name starts with _ to not get inlcuded in the output
        """
        if hasattr(the_object, '__dict__'):
            fields = the_object.__dict__.keys()
        elif hasattr(the_object, '__slots__'):
            fields = the_object.__slots__
        else:
            fields = dir(the_object)
        fields = [field for field in fields if not field.startswith('_')]
        return fields
    
    AcousticGrandPiano = 0
    BrightAcousticPiano = 1
    lectricGrandPiano =2
    Honky_tonkPiano = 3
    ElectricPiano=4
    ElectricPiano=5
    Harpsichord=6
    Clavi=7
    Celesta=8
    Glockenspiel=9
    MusicBox=10
    Vibraphone=11
    Marimba=12
    Xylophone=13
    TubularBells=14
    Dulcimer=15
    DrawbarOrgan=16
    PercussiveOrgan=17
    RockOrgan=18
    ChurchOrgan=19
    
    ReedOrgan=20
    Accordion=21
    Harmonica=22
    TangoAccordion=23
    AcousticGuitar_nylon=24
    AcousticGuitar_steel=25
    Electric_Guitar_jazz=26
    Electric_Guitar_clean=27
    Electric_Guitar_muted=28
    Overdriven_Guitar=29
    Distortion_Guitar=30
    Guitar_harmonics=31
    AcousticBass=32
    ElectricBass_finger=33
    Electric_Bass_pick=34
    Fretless_Bass=35
    SlapBass_1 =36
    SlapBass_2=37
    SynthBass_1=38
    SynthBass_2=39
    Violin=40
    Viola=41
    Cello=42
    Contrabass=43
    TremoloStrings=44
    Pizzicato_Strings=45
    OrchestralHarp=46
    Timpani=47
    String_Ensemble1=48
    String_Ensemble2=49
    SynthStrings1=50
    SynthStrings2=51
    ChoirAahs=52
    VoiceOohs=53
    SynthVoice=54
    OrchestraHit=55
    Trumpet=56
    Trombone=57
    Tuba=58
    MutedTrumpet=59
    FrenchHorn=60
    BrassSection=61
    SynthBrass1=62
    SynthBrass2=63
    SopranoSax=64
    AltoSax=65  
    TenorSax=66
    BaritoneSax=67
    Oboe=68
    EnglishHorn=69
    Bassoon=70
    Clarinet=71
    Piccolo=72
    Flute=73
    Recorder=74
    PanFlute=75
    BlownBottle=76
    Shakuhachi=77
    Whistle=78
    Ocarina=79
    Lead1square =80
    Lead2sawtooth=81
    Lead3calliope=82
    Lead4chiff=83
    Lead5charang=84
    Lead6voice=85
    Lead7fifths=86
    Lead8basslead=87
    Pad1newage=88
    Pad2warm=89
    Pad3polysynth=90
    Pad4choir=91
    Pad5bowed=92
    Pad6metallic=93
    Pad7halo=94
    Pad8sweep=95
    FX1rain=96
    FX2soundtrack=97
    FX3crystal=98
    FX4atmosphere=99
    FX_5_brightness = 100
# 102.	FX 6 (goblins)
# 103.	FX 7 (echoes)
# 104.	FX 8 (sci-fi)
# 105.	Sitar
# 106.	Banjo
# 107.	Shamisen
# 108.	Koto
# 109.	Kalimba
# 110.	Bag pipe
# 111.	Fiddle
# 112.	Shanai
# 113.	Tinkle Bell
# 114.	Agogo
# 115.	Steel Drums
# 116.	Woodblock
# 117.	Taiko Drum
# 118.	Melodic Tom
# 119.	Synth Drum
# 120.	Reverse Cymbal
# 121.	Guitar Fret Noise
# 122.	Breath Noise
# 123.	Seashore
# 124.	Bird Tweet
# 125.	Telephone Ring
# 126.	Helicopter
# 127.	Applause
# 128.	Gunshot







