# run.py
from contributionModel import *  # omit this in jupyter notebooks
import matplotlib.pyplot as plt
import pandas as pd
import random
import math
# from mesa.datacollection import DataCollector
 

# The are the potential message topics
potential_topics = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

number_of_agents = 10
number_of_messages = 30
number_of_days = 365

# This is the number of topics that will be included in this group
# number_of_topics = 3
# topics = []

# # Pick x random topics for the list of potential topics
# for i in range(number_of_topics):
#     topics.append(random.choice(potential_topics))


# topics = ["A", "B", "C"]
topics = ["A", "B", "C"]
# Create a Community with a number of members and a set of topics
model = Community(number_of_agents, number_of_messages, topics)

# Initial Distribution of Messages
initial_messages = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0
}

for message in model.messages:
    initial_messages[message.topic] = initial_messages[message.topic] + 1


message_topic_count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0
}

messages_on_topic = []
agents_in_group = []
agents_interested_in_group = []
total_messages = []

# Step the model for number of days
for i in range(number_of_days):
    # Step the model
    model.step()

    count_of_on_topic = 0
    for message in model.messages:
        message_topic_count[message.topic] = message_topic_count[message.topic] + 1
        if message.topic in topics:
            count_of_on_topic = count_of_on_topic + 1
    total_messages.append(len(model.messages))
    messages_on_topic.append(count_of_on_topic)

    agents_in_group.append(len(model.schedule.agents))
    count_of_agents_interested = 0
    for a in model.schedule.agents:
        if a.topic_interests in topics:
            count_of_agents_interested = count_of_agents_interested + 1
    agents_interested_in_group.append(count_of_agents_interested)

message_topic_count_names = list(message_topic_count.keys())
message_topic_count_values = list(message_topic_count.values())

plt.plot(model.datacollector.get_model_vars_dataframe())
plt.title('Info Benefit')
plt.xlabel('Day')
plt.ylabel('Benefit Level')
plt.show()

plt.plot(total_messages, label='Total')
plt.plot(messages_on_topic, label='On Topic')
plt.title('Messages on Topic')
plt.xlabel('Day')
plt.ylabel('Count of Messages')
plt.legend()
plt.show()

plt.plot(agents_in_group, label='Total')
plt.plot(agents_interested_in_group, label='Interested')
# plt.plot(model.datacollector.get_model_vars_dataframe()['Count_of_Members_Left'], label="Left")
plt.title('Agents in Group')
plt.xlabel('Day')
plt.ylabel('Count of Agents')
plt.legend()
plt.show()

plt.bar(message_topic_count_names, message_topic_count_values)
plt.title('Total Messages per Topic')
plt.xlabel('Topic')
plt.ylabel('Count of Messages')
plt.show()
