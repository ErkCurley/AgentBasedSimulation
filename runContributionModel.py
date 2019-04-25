# run.py
from contributionModel import *  # omit this in jupyter notebooks
import matplotlib.pyplot as plt
import random
import math
# from mesa.datacollection import DataCollector
 

# The are the potential message topics
potential_topics = ["A","B","C","D","E","F","G","H","I"]

number_of_agents = 10
number_of_messages = 30
number_of_days = 365

# This is the number of topics that will be included in this group
# number_of_topics = 3
# topics = []

# # Pick x random topics for the list of potential topics
# for i in range(number_of_topics):
#     topics.append(random.choice(potential_topics))


topics = ["A","B","C"]
# Create a Community with a number of members and a set of topics
model = Community(number_of_agents, number_of_messages, topics)


averages = []

# Step the model for number of days
for i in range(number_of_days):
    # Step the model
    model.step()

plt.plot(model.datacollector.get_model_vars_dataframe())
plt.show()