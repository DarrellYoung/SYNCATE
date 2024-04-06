# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:31:40 2024

@author: mail4
"""

class Environment:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def run(self, steps=1):
        for _ in range(steps):
            for agent in self.agents:
                agent.act()
