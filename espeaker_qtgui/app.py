#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow

from espeaker_qtgui.ui.gui import Ui_MainWindow

class  MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, settings):
        super(QMainWindow, self).__init__()
        self.settings = settings
        self.setupUi(self)
        self.connect_buttons()
        self.load_engine()
        self.load_languages()
        
    def load_engine(self):
        self.engine = None
        exec("from espeaker_qtgui.engines." + self.settings.engine + " import Engine")
        exec("self.engine = Engine()")
        
    def load_languages(self):
        languages = []
        self.language_codes = []
        for lang in self.engine.get_languages():
            self.language_codes.append(lang[0])
            languages.append(lang[1])
        self.language_comboBox.clear()
        self.language_comboBox.addItems(languages)

    def connect_buttons(self):
        for e in filter(lambda e: "_button" in e, self.__dict__.keys()):
            eval("self." + e + ".clicked.connect(self." + e + "_clicked)")
            
    def new_button_clicked(self):
        print('1')

    def open_button_clicked(self):
        print('2')

    def save_as_button_clicked(self):
        print('3')

    def record_button_clicked(self):
        print('4')

    def revert_button_clicked(self):
        print('5')

    def play_button_clicked(self):
        print('6')

    def stop_button_clicked(self):
        print('7')
    