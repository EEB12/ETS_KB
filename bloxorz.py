#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Run"""

import pygame
import sys
import os
import time

class algortima:
    astar = 1

class level:
    lvmain = "./level/main.json"
    # lv1  = "./level/1.json"
    # lv2 = "./level/2.json"
    # lv3 = "./level/3.json"
    # lv4 = "./level/4.json"
    # lv5 = "./level/5.json"
    # lv6 = "./level/6.json"
    # lv7 = "./level/7.json"
    # lv8 = "./level/8.json"
    # lv9 = "./level/9.json"
    # lv10 = "./level/10.json"
    # lv11 = "./level/11.json"
    # lv12 = "./level/12.json"
    # lv13 = "./level/13.json"
    # lv14 = "./level/14.json"
    # lv15 = "./level/15.json"

def duration(start):
    dur = time.time() - start
    print("Duration Time: ", dur)

def map(path):
    return [y for x in path for y in x]

def drawPath(solution, time=1, level=level):
    if solution != None:
        print("Success!")
        print("Step:", len(solution))
        prin