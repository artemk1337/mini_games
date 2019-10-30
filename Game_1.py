#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from tkinter import *


def Quit(ev):
    global root
    root.destroy()


def SimpleNumbers():
    pass


def SimpleGame():
    pass


root = Tk()

panelFrame = Frame(root, height=60, bg='gray')
textFrame = Frame(root, height=340, width=600)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

SmplNmBtn = Button(panelFrame, text='Простые чисела')
GameBtn = Button(panelFrame, text='Игра')
quitBtn = Button(panelFrame, text='Выйти')

SmplNmBtn.bind("<Button-1>", SimpleNumbers)
GameBtn.bind("<Button-1>", SimpleGame)
quitBtn.bind("<Button-1>", Quit)

SmplNmBtn.place(x=10, y=10, width=100, height=40)
GameBtn.place(x=120, y=10, width=100, height=40)
quitBtn.place(x=230, y=10, width=100, height=40)

root.mainloop()