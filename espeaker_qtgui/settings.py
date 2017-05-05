#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#* http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles Barcza *
#*                                                                                                       *
#*                      Written by Miklos Horvath * hmiki[]blackpantheros.eu                             *
#*                                                                                                       *
#*************************************************************************************(c)2002-2017********

import os, configparser

CFGFILE = os.environ["HOME"]+"/.config/espeaker_qtgui.cfg"

class Settings():
    def __init__(self):
        pass
   
    def load(self):
        self.config = configparser.ConfigParser()
        self.config.read(CFGFILE)
        try:
            s = self.config["SETTINGS"]
        except:
            self.config.add_section("SETTINGS")
            s = self.config["SETTINGS"]
        self.engine = s.get("engine", "espeak")
        self.language = s.get("language", "en")
        self.gender = s.get("gender", "male")
        self.variant = s.get("variant", "m3")
        self.pitch = s.get("pitch", 20)
        self.volume = s.get("volume", 30)
        self.speed = s.get("speed", 40)
        self.delay = s.get("delay", 100)
 
    def change(self, var, value):
        self.__dict__[var] = value
        self.config.set("SETTINGS", var, str(value))
        with open(CFGFILE, "w") as file:
            self.config.write(file)

    def set_gender(self, gender):
        self.change("gender", gender)
    
    def set_variant(self, variant):
        self.change("variant", variant)
    
    def set_language(self, language):
        self.change("language", language)
    
    def set_pitch(self, pitch):
        self.change("pitch", pitch)
    
    def set_volume(self, volume):
        self.change("volume", volume)
    
    def set_speed(self, speed):
        self.change("speed", speed)
    
    def set_delay(self, delay):
        self.change("delay", delay)
