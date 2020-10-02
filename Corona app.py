#!/usr/bin/env python
# coding: utf-8

# In[1]:


from kivy.lang import Builder


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from bs4 import BeautifulSoup
import requests
import locale

KV = '''
Screen:

    BoxLayout:
        id: box
        orientation: "vertical"

        MDToolbar:
            title: "Coronavirus Stats USA"
'''


class Test(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        source = requests.get('https://www.worldometers.info/coronavirus/usa/texas/').text
        soup = BeautifulSoup(source, 'lxml')
        stats = soup.find('div', class_='content-inner')
        stats = stats.find_all('div', class_='maincounter-number')
        a = stats
        cases = a[0].span.text
        deaths = a[1].span.text
        recover = a[2].span.text
        screen.ids.box.add_widget(
            MDLabel(
                text='Coronavirus Stats in Texas',
                halign="center",
                theme_text_color='Primary',
                font_style=('H3')
            )
        )
        screen.ids.box.add_widget(
            MDLabel(
                text="Coronavirus Cases - %s" % (cases),
                halign="center",
                theme_text_color='Error',
                font_style=('H6')
            )
        )
        screen.ids.box.add_widget(
            MDLabel(
                text="Coronavirus Deaths - %s" % (deaths),
                halign="center",
                theme_text_color='Error',
                font_style=('H6')
            )
        )
        screen.ids.box.add_widget(
            MDLabel(
                text="Coronavirus Recoveries - %s" % (recover),
                halign="center",
                theme_text_color='Error',
                font_style=('H6')
            )
        )
        return screen


Test().run()


# In[1]:


from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

# create a dropdown with 10 buttons
dropdown = DropDown()
for index in range(10):
    # When adding widgets, we need to specify the height manually
    # (disabling the size_hint_y) so the dropdown can calculate
    # the area it needs.

    btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

    # for each button, attach a callback that will call the select() method
    # on the dropdown. We'll pass the text of the button as the data of the
    # selection.
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))

    # then add the button inside the dropdown
    dropdown.add_widget(btn)

# create a big main button
mainbutton = Button(text='Hello', size_hint=(None, None))

# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the
# mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).
mainbutton.bind(on_release=dropdown.open)

# one last thing, listen for the selection in the dropdown list and
# assign the data to the button text.
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

runTouchApp(mainbutton)


# In[ ]:




