#!/usr/bin/env python

import wx

import random

import matplotlib.pyplot as plt

import numpy as np

f = open('finalproject.txt','r+')

times = [ ]

class NewFrame(wx.Frame):
    
    def __init__(self, parent):
        
        wx.Frame.__init__(self, parent, wx.ID_ANY, "NamePicking", size = (500,300))
        
        self.panel = wx.Panel(self)
        
        self.reminder = wx.StaticText(self.panel, label = "Please insert the student names one per line", pos = (110,20))
        
        self.BtnSubmit = wx.Button(self.panel, label = "submit", pos = (200,200))
        
        self.BtnSubmit.Bind(wx.EVT_BUTTON,self.OnSubmit)
        
        self.BtnChoose = wx.Button(self.panel, label = "choose", pos = (200,200))
        
        self.BtnChoose.Bind(wx.EVT_BUTTON,self.OnChoose)
        
        self.BtnChoose.Show(False)
        
        self.BtnPlot = wx.Button(self.panel, label = "plot the times each one has been chosen", pos = (250,250))
        
        self.BtnPlot.Bind(wx.EVT_BUTTON,self.OnPlot)
        
        self.showresult = wx.TextCtrl(self.panel, pos = (200,100))
        
        self.showresult.Show(False)
        
        self.showinput = wx.TextCtrl(self.panel, pos = (200,100), size = (200,50),style = wx.TE_MULTILINE)
        
        self.namesinput = f.readlines()
        
        self.newstring = " "
        
        for currentnames in self.namesinput:
            
            self.newstring += currentnames
        
        self.showinput.SetValue(self.newstring)
    

    def OnSubmit(self, e):
    
        nameschanged = self.showinput.GetValue()
        
        f.seek(0)
        
        f.truncate()
        
        f.write(nameschanged)
        
        self.BtnChoose.Show(True)
        
        self.showresult.Show(True)
        
        self.BtnPlot.Show(True)
        
        self.reminder.Show(False)
        
        self.showinput.Show(False)
        
        self.BtnSubmit.Show(False)
    

    def OnChoose(self, e):
        
        f.seek(0)
        
        namesGiven = f.readlines()
        
        for givennames in namesGiven:
            times.append(0)
        
        numberofnames = len(namesGiven)
        
        rankchosen = random.randint(0,numberofnames-1)
        
        namechosen = namesGiven[rankchosen]
        
        self.showresult.SetValue(namechosen)

        times[rankchosen]+=1

        print times[rankchosen]


    def OnPlot(self, e):

        people = f.readlines()

        y_pos = np.arrange(len(people))

        plt.barh(y_pos, times, align = 'center', alpha = 0.4)

        plt.ysticks(y_pos, people)

        plt.xlabel('times chosen')

        plt.title('The times that the students have been chosen')

        plt.show()

app = wx.App(False)

frame = NewFrame(None)

frame.Show()

app.MainLoop()
