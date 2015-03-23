#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_02, password authentication"""


import authentication
import getpass


password = 'food'



def login(username, maxattempts = 3):
    """"""
    incorrectPrt = 'Incorrect username or password. You have {} attempts left.'
    
    passw = False
   
    # inputs = raw_input('Please enter your password:')
   
    while(maxattempts <> 0 or maxattempts <0):
        #inputs = raw_input('Please enter your password:')
        inputs = getpass.getpass('Please enter your password:')
        password = inputs.split()
        # authentication.authenticate(username, password)
        if(password <> authentication.authenticate(username, password)):
            passw = True
        else:
            maxattempts -= 1
            
            print incorrectPrt.format(maxattempts)
            
            passw
            
        
        
    return passw

## import getpass

##def login():
##    user = input("Username [%s]: " % getpass.getuser())
##    if not user:
##        user = getpass.getuser()
##
##    pprompt = lambda: (getpass.getpass(), getpass.getpass('Retype password: '))
##
##    p1, p2 = pprompt()
##    while p1 != p2:
##        print('Passwords do not match. Try again')
##        p1, p2 = pprompt()
##
##    return user, p1
