#!/usr/bin/env python
# coding: utf-8

# In[1]:


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import numpy as np


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Coefficient Equation 1: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        

        self.inside.add_widget(Label(text="Second Coefficient Equation 1: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)
        
       
        
        self.inside.add_widget(Label(text="First Coefficient Equation 2: "))
        self.nameeq = TextInput(multiline=False)
        self.inside.add_widget(self.nameeq)
        
        self.inside.add_widget(Label(text="Second Coefficient Equation 2: "))
        self.lastNameeq = TextInput(multiline=False)
        self.inside.add_widget(self.lastNameeq)
        
        self.inside.add_widget(Label(text="Solution 1: "))
        self.sol1 = TextInput(multiline=False)
        self.inside.add_widget(self.sol1)
        
        self.inside.add_widget(Label(text="Solution 2: "))
        self.sol2 = TextInput(multiline=False)
        self.inside.add_widget(self.sol2)
        
        

        self.add_widget(self.inside)
            
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        cof1 = self.name.text
        cof2 = self.lastName.text
        cof1eq = self.nameeq.text
        cof2eq= self.lastNameeq.text
        sol1 = self.sol1.text
        sol2 = self.sol2.text

        #print("cof1", cof1, "Last Name:", cof2, "Solution 1:", sol1, "Solution 2:", sol2)
        cof1 = int(cof1)
        cof2 = int(cof2)
        cof1eq = int(cof1eq)
        cof2eq= int(cof2eq)
        sol1 = int(sol1)
        sol2 = int(sol2)

        a = np.array([[cof1,cof2], [cof1eq,cof2eq]])
        b = np.array([sol1,sol2])
        x = np.linalg.solve(a, b)
        x = str(x)
        self.inside.add_widget(Label(text=x))
        self.ans = TextInput(multiline=False)
        self.inside.add_widget(self.ans)
        
        
        
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()


# In[ ]:





# In[ ]:




