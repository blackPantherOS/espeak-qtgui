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

import gettext, sys

gettext.install("espeak-qtgui", "/usr/share/locale")

from PyQt5.QtWidgets import QApplication

from espeak_qtgui.settings import Settings
from espeak_qtgui.app import MainWindow

if __name__ == "__main__":
    settings = Settings()
    settings.load()
    app = QApplication(sys.argv)
    window = MainWindow(settings)
    window.show()
    sys.exit(app.exec_())
