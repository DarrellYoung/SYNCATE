# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:32:42 2024

@author: mail4
"""

def extend_agent(agent):
    def new_act():
        print(f"{agent.name} says hello!")
    agent.act = new_act
