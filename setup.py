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

setup(name='espeak-qtgui',
      version='1.0',
      description='Qt5 Gui for Espeak',
      author='Miklos Horvath',
      author_email='hmiki@blackpantheros.eu',
      url='https://github.com/hmikihth/espeak-qtgui/',
      packages=['espeak_qtgui', 'espeak_qtgui.ui', 'espeak_qtgui.engines'],
      scripts=['espeak-qtgui'],
      data_files=[('share/applications',['espeak-qtgui.desktop'])]
     )
