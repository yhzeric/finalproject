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
        
        self.BtnPlot = wx.Button(self.panel, label = "plot the times each one has been chosen", pos = (200,250))
        
        self.BtnPlot.Bind(wx.EVT_BUTTON,self.OnPlot)
        
        self.showresult = wx.TextCtrl(self.panel, pos = (200,100))
        
        self.showresult.Show(False)
        
        self.showinput = wx.TextCtrl(self.panel, pos = (200,100), size = (200,50),style = wx.TE_MULTILINE)
        
        self.namesinput = f.readlines()
        

        self.newstring = ""
        
        for currentnames in self.namesinput:
            
            self.newstring += currentnames
        
        self.showinput.SetValue(self.newstring)
    

    def OnSubmit(self, e):
    
        nameschanged = self.showinput.GetValue()
        
        f.seek(0)
        
        f.truncate()
        
        f.write(nameschanged)
        
        f.seek(0)
        
        newnames = f.readlines()
        
        for i in newnames:
        
        	times.append(0)
        	
        self.BtnChoose.Show(True)
        
        self.showresult.Show(True)
        
        self.BtnPlot.Show(True)
        
        self.reminder.Show(False)
        
        self.showinput.Show(False)
        
        self.BtnSubmit.Show(False)
    

    def OnChoose(self, e):
    
    	f.seek(0)
        
        namesGiven = f.readlines()
        
        numberofnames = len(namesGiven)
        
        rankchosen = random.randint(0,numberofnames-1)
        
        namechosen = namesGiven[rankchosen]
        
        self.showresult.SetValue(namechosen)

        times[rankchosen]+=1

        print times[rankchosen]


    def OnPlot(self, e):
    
        f.seek(0)
        
        people = f.readlines()
        
        fig = plt.figure()
        
        ax = fig.add_subplot(111)

        ind = np.arange(len(people))
        
        width = 0.05
        
        rect1 = ax.bar(ind,times,width)

        ax.set_ylim(0,10)

        ax.set_ylabel('times chosen')

        ax.set_title('number of times each individual is chosen')

        xTickMarks = people

        ax.set_xticks(ind+width)

        xtickNames = ax.set_xticklabels(xTickMarks)

        plt.setp(xtickNames, rotation = 45, fontsize = 10)

        plt.show()

app = wx.App(False)

frame = NewFrame(None)

frame.Show()

app.MainLoop()
