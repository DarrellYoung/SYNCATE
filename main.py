# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:32:06 2024

@author: mail4
"""

import importlib
from environment import Environment
from agent import Agent


def load_plugins(environment):
    # Example of dynamically loading a plugin and extending agent behavior
    plugin = importlib.import_module("plugins.greet")
    for agent in environment.agents:
        plugin.extend_agent(agent)


def main():
    env = Environment()
    agent = Agent("Agent1", env)
    env.add_agent(agent)

    load_plugins(env)

    env.run(steps=5)

if __name__ == "__main__":
    main()
