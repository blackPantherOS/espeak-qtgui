#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

class Engine():
    languages = [["de", _("German")],
                 ["en", _("English")],
                 ["es", _("Spanish")],
                 ["hu", _("Hungarian")]]
    
    variants_male = ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "croak", "wisper"]
    variants_female = ["f1", "f2", "f3", "f4", "f5", "whisperf"]
    
    sliders = {"pitch":99, "volume":200, "speed":500, "delay":200}
    
    def __init__(self):
        self.process = None
    
    def get_languages(self):
        return self.languages

    def get_variants(self, gender="male"):
        if gender == "male":
            return self.variants_male
        else:
            return self.variants_female
        
    def get_sliders(self):
        return self.sliders
 
    def play(self, text, language, pitch, volume, speed, delay):
        arguments = ["espeak", "-v", language, "-p", str(pitch), "-a", str(volume), "-s", str(speed), "-g", str(delay)]
        self.process = subprocess.Popen(arguments, stdin=subprocess.PIPE)
        self.process.stdin.write(text.encode("utf-8"))
        self.process.stdin.flush()
        self.process.stdin.close()        
    
    def stop(self):
        pass
    
    def pause(self):
        pass
