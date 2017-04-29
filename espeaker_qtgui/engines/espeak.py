#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Engine():
    languages = [["de", _("German")],
                 ["en", _("English")],
                 ["es", _("Spanish")],
                 ["hu", _("Hungarian")]]
    
    variants_male = ["m1", "m2", "m3", "m4", "m5", "m6", "m7", "croak", "wisper"]
    variants_female = ["f1", "f2", "f3", "f4", "f5", "whisper"]
    
    def __init__(self):
        pass
    
    def get_languages(self):
        return self.languages

    def get_variants(self, gender="male"):
        if gender == "male":
            return self.variants_male
        else:
            return self.variants_female
 
    def play(self, text, language):
        pass
    
    def stop(self):
        pass
    
    def pause(self):
        pass
