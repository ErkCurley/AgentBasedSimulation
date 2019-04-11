# model.py
from mesa import Agent, Model
from mesa.time import RandomActivation
import random

potential_topics = ["A","B","C","D","E","F","G","H","I"]

class GroupMember(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Benefit from Information Access
        self.InfoB_access = 0

        # Benefit from Information Sharing
        self.InfoB_share = 0

        # Benefit from Social Identity
        self.SocialB_identity = 0

        # Benefit from Social Bonding
        self.SocailB_bond = 0

        # Intrinsic Benefit of Recreation
        self.IntrinsicB_recreation = 0

        #  Intrninsic Benefit of Reputation
        self.IntrinsicB_reputation = 0

    def step(self):
        # The agent's step will go here.

        # If any of the agent benefits are greater than 3 contribution behavior and benefits from sharing increased.
        if self.SocialB_identity > 3 or self.SocailB_bond > 3 or self.IntrinsicB_recreation > 3:
            # if Community.total_messages < 100:
            print("Increase information sharing benefit")

class Message():
    def __init__(self,topic):
        self.topic = topic
        print(self.topic)



class Community(Model):
    """A model with some number of agents."""
    def __init__(self, N, topics):
        self.schedule = RandomActivation(self)


        # Group was initialied with 30 members
        self.num_agents = 30
        # Group is initialized with 30 messages
        self.totalMessages = 30
        self.messages = []

        for x in range(self.totalMessages):
            self.messages.append(Message(random.choice(potential_topics)))

        self.topics = topics
        # Create agents
        for i in range(self.num_agents):
            a = GroupMember(i, self)
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
