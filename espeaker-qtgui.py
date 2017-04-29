#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gettext, sys

gettext.install("espeaker-qtgui", "/usr/share/locale")

from PyQt5.QtWidgets import QApplication

from espeaker_qtgui.settings import Settings
from espeaker_qtgui.app import MainWindow

if __name__ == "__main__":
    settings = Settings()
    settings.load()
    app = QApplication(sys.argv)
    window = MainWindow(settings)
    window.show()
    sys.exit(app.exec_())
