# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:30:59 2024

@author: mail4
"""

class Agent:
    def __init__(self, name, environment):
        self.name = name
        self.environment = environment

    def decide(self):
        # Placeholder for decision-making behavior.
        pass

    def act(self):
        # Placeholder for action execution.
        print(f"{self.name} is acting in the environment.")
