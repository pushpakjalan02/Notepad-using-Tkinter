# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:08:36 2019

@author: Sneha Jalan
"""

#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)

# Close opend file
fo.close()