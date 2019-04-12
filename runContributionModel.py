# run.py
from contributionModel import *  # omit this in jupyter notebooks
import matplotlib.pyplot as plt
import random

# The are the potential message topics
potential_topics = ["A","B","C","D","E","F","G","H","I"]

number_of_agents = 100
number_of_days = 365

# This is the number of topics that will be included in this group
number_of_topics = 3
topics = []

# Pick x random topics for the list of potential topics
for i in range(number_of_topics):
    topics.append(random.choice(potential_topics))

model = Community(number_of_agents,topics)
for i in range(number_of_days):
    model.step()

    # Store the results
    Info_Benefit = []
    for agent in model.schedule.agents:
        Info_Benefit.append(agent.InfoB_access)

plt.hist(Info_Benefit, bins=range(max(Info_Benefit)+1))
plt.show()
