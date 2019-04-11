# run.py
from contributionModel import *  # omit this in jupyter notebooks
import matplotlib.pyplot as plt
import random

potential_topics = ["A","B","C","D","E","F","G","H","I"]
number_of_agents = 100
number_of_days = 365
number_of_topics = 3
topics = []

for i in range(number_of_topics):
    topics.append(random.choice(potential_topics))

model = Community(number_of_agents,topics)
for i in range(number_of_days):
    model.step()

#     # Store the results
#     for agent in model.schedule.agents:
#         all_wealth.append(agent.wealth)

# plt.hist(all_wealth, bins=range(max(all_wealth)+1))
# plt.show()
