#!/usr/bin/env python

import wx

import random

f = open('finalproject.txt','r+')


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
        
        self.reminder.Show(False)
        
        self.showinput.Show(False)
        
        self.BtnSubmit.Show(False)
    

    def OnChoose(self, e):
        
        f.seek(0)
        
        namesGiven = f.readlines()
        
        namesChosen = random.choice(namesGiven)
        
        self.showresult.SetValue(namesChosen)

        for stuff in namesGiven:

            int(stuff) = 0

            if stuff == namesChosen:
                int(stuff) += 1
                print int(stuff)




app = wx.App(False)

frame = NewFrame(None)

frame.Show()

app.MainLoop()
