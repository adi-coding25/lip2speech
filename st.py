#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 00:50:04 2021

@author: aditya
"""

import speech_recognition as sr
import time
s=time.time()
fl="audio.wav"
r=sr.Recognizer()
with sr.Microphone() as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
end=time.time()
print(end-s)