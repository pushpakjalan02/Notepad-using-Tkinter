# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:46:13 2019

@author: Sneha Jalan
"""

from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.txt"),("all files","*.*")))
print (root.filename)