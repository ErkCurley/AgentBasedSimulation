# run.py
from contributionModel import *  # omit this in jupyter notebooks
import matplotlib.pyplot as plt


number_of_agents = 100
model = Community(number_of_agents)
for i in range(number_of_agents):
    model.step()

#     # Store the results
#     for agent in model.schedule.agents:
#         all_wealth.append(agent.wealth)

# plt.hist(all_wealth, bins=range(max(all_wealth)+1))
# plt.show()
