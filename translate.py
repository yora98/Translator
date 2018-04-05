#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from googletrans import Translator

class Translate(object):
   source=""
   dest=""
   detected_lang=""
   dest_lang=""

   def __init__(self,source):
        self.source=source

   def translate(self,langu):
        dest_lang=langu
        translator = Translator()
        v=translator.translate(self.source,dest=dest_lang)
        self.dest=v.text


   def detectLang(self):
       translator = Translator()
       print(self.source)
       self.detected_lang = translator.detect(self.source).lang
       print(self.detected_lang)
       return self.detected_lang

   def translatedLang(self):
       return self.dest