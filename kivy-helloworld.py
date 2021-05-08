"""
Author: Hello (World)
Untitled-1 (c) 2021
Desc: kivy gui test
Created:  2021-05-08T05:17:46.675Z
Modified: !date!
"""

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()