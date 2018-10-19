#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 12:02:32 2018

@author: jose
"""
#con twint se puede cambiar el modo en que 
# Import the module
import twint
import os
import sys
import json
import time

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    screen_name = sys.argv[1]
    c = twint.Config()
    c.Username = screen_name
    c.Store_json = True
    c.Custom = ["id", "name", "username", "bio","location","url",
            "join_date","join_time","tweets","following","followers",
            "likes","media","private","verified","avatar"]
    c.User_full = True
    c.Output = "juanmarin_cs_followers.json"

    twint.run.Followers(c)