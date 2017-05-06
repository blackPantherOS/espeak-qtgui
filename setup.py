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

from distutils.core import setup

setup(name='espeaker-qtgui',
      version='1.0',
      description='Qt5 Gui for Espeak',
      author='Miklos Horvath',
      author_email='hmiki@blackpantheros.eu',
      url='https://github.com/hmikihth/espeaker-qtgui/',
      packages=['espeaker_qtgui', 'espeaker_qtgui.ui', 'espeaker_qtgui.engines'],
      scripts=['espeaker-qtgui'],
      data_files=[('share/applications',['espeaker-qtgui.desktop'])]
     )