# model.py
from mesa import Agent, Model
from mesa.datacollection import DataCollector
from mesa.time import RandomActivation
import random

potential_topics = ["A","B","C","D","E","F","G","H","I"]
random.seed(a=123)

class GroupMember(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Benefit from Information Access
        self.InfoB = 0

        # Choose a random topic to be your choice
        self.topic_interests = random.choice(potential_topics)

class Message():
    def __init__(self,topic):
        self.topic = topic
        # print(topic)


def compute_benefit(model):
    b = 0
    for member in model.schedule.agents:
        b = b + member.InfoB

    a = b / len(model.schedule.agents)
    return a


class Community(Model):
    """A model with some number of agents."""
    def __init__(self, N, M, topics):
        self.schedule = RandomActivation(self)

        # Group was initialied with n members
        self.num_agents = N
        # Group is initialized with m messages
        self.totalMessages = M
        self.messages = []

        for x in range(self.totalMessages):
            # self.messages.append(Message("A"))
            self.messages.append(Message(random.choice(potential_topics)))
        
        self.topics = topics
        # Create agents
        for i in range(self.num_agents):
            a = GroupMember(i, self)
            self.schedule.add(a)
        
        self.datacollector = DataCollector(
                model_reporters = {
                    "Average_Info_Benefit": compute_benefit
                    # "Messge Topics": compute_topics
                }
            )


        

    def step(self):
        '''Advance the model by one step.'''

        # Look over all the agents
        for a in self.schedule.agents:

            # Each agent looks at all the messages in the group
            count_of_interest = 0
            if len(self.messages) > 0:
                for x in self.messages:
                    if x.topic in a.topic_interests:
                        count_of_interest = count_of_interest + 1

                # The cost is the proportion of messages that were read divided by the signal to noise ratio

                not_interesting = len(self.messages) - count_of_interest
                if not_interesting == 0:
                    signal_to_noise = 0
                else:
                    signal_to_noise = count_of_interest/not_interesting

                if signal_to_noise == 0:
                    a.InfoB = 0
                else:
                    a.InfoB = len(self.messages) / signal_to_noise

        # Delete all messages
        self.messages = []
        for a in self.schedule.agents:
            if a.InfoB > 1:
                new_message_topic = random.choice(a.topic_interests)
                new_message = Message(new_message_topic)
                self.messages.append(new_message)
                a.InfoB = a.InfoB - 1


        self.datacollector.collect(self)
        self.schedule.step()



    
