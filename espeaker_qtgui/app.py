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
        self.load_settings()
        self.load_languages()
        self.load_sliders()
        
        self.male_radioButton.toggled.connect(self.load_variants)
        self.variant_comboBox.currentIndexChanged.connect(self.variant_changed)
        self.language_comboBox.currentIndexChanged.connect(self.language_changed)
        self.pitch_slider.valueChanged.connect(self.pitch_changed)
        self.pitch_slider.sliderMoved.connect(self.pitch_moved)
        self.volume_slider.valueChanged.connect(self.volume_changed)
        self.volume_slider.sliderMoved.connect(self.volume_moved)
        self.speed_slider.valueChanged.connect(self.speed_changed)
        self.speed_slider.sliderMoved.connect(self.speed_moved)
        self.delay_slider.valueChanged.connect(self.delay_changed)
        self.delay_slider.sliderMoved.connect(self.delay_moved)
        
    def load_settings(self):
        self.settings.load()
        if self.settings.gender == "male":
            self.male_radioButton.setChecked(True)
        else:
            self.female_radioButton.setChecked(True)
        self.variants = self.engine.get_variants(self.settings.gender)
        self.variant_comboBox.clear()
        self.variant_comboBox.addItems(self.variants)
        self.variant_comboBox.setCurrentIndex(self.variants.index(self.settings.variant))
        
    def pitch_changed(self, pitch):
        self.settings.set_pitch(pitch)
        self.pitch_lcdNumber.display(pitch)
        
    def pitch_moved(self, pitch):
        self.pitch_lcdNumber.display(pitch)

    def volume_changed(self, volume):
        self.settings.set_volume(volume)
        self.volume_lcdNumber.display(volume)
        
    def volume_moved(self, volume):
        self.volume_lcdNumber.display(volume)

    def speed_changed(self, speed):
        self.settings.set_speed(speed)
        self.speed_lcdNumber.display(speed)
        
    def speed_moved(self, speed):
        self.speed_lcdNumber.display(speed)

    def delay_changed(self, delay):
        self.settings.set_delay(delay)
        self.delay_lcdNumber.display(delay)
    
    def delay_moved(self, delay):
        self.delay_lcdNumber.display(delay)

    def load_sliders(self):
        sliders = self.engine.get_sliders()
        for slider in sliders:
            self.__dict__[slider+"_slider"].setMaximum(sliders[slider])
            self.__dict__[slider+"_slider"].setValue(int(self.settings.__dict__[slider]))
            self.__dict__[slider+"_lcdNumber"].display(int(self.settings.__dict__[slider]))
            
    def language_changed(self, index):
        self.settings.set_language(self.language_codes[index])
        
    def variant_changed(self, index):
        if index >= 0:
            self.settings.set_variant(self.variants[index])
        
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
        self.language_comboBox.setCurrentIndex(self.language_codes.index(self.settings.language))
 
    def load_variants(self, *args):
        if self.male_radioButton.isChecked():
            gender = "male"
        else:
            gender = "female"
        self.variants = self.engine.get_variants(gender)
        self.variant_comboBox.clear()
        self.variant_comboBox.addItems(self.variants)
        self.settings.set_gender(gender)
        
    def connect_buttons(self):
        for e in filter(lambda e: "_button" in e, self.__dict__.keys()):
            eval("self." + e + ".clicked.connect(self." + e + "_clicked)")
            
    def new_button_clicked(self):
        self.textEdit.clear()

    def open_button_clicked(self):
        print('2') # txt megnyitása

    def save_as_button_clicked(self):
        print('3') # Írás egy text fileba

    def record_button_clicked(self):
        print('4') # Írás wav-ba

    def revert_button_clicked(self):
        self.pitch_slider.setValue(50)
        self.volume_slider.setValue(100)
        self.speed_slider.setValue(175)
        self.delay_slider.setValue(10)

    def play_button_clicked(self):
        text = self.textEdit.toPlainText()
        language = self.language_codes[self.language_comboBox.currentIndex()] + "+" + self.variants[self.variant_comboBox.currentIndex()]
        pitch = self.pitch_slider.value()
        volume = self.volume_slider.value()
        speed = self.speed_slider.value()
        delay = self.delay_slider.value()
        self.engine.play(text, language, pitch, volume, speed, delay)

    def stop_button_clicked(self):
        print('7')
    