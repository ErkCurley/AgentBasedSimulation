# model.py
from mesa import Agent, Model
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

        self.topic_interests = random.choice(potential_topics)

class Message():
    def __init__(self,topic):
        self.topic = topic



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


        

    def step(self):
        '''Advance the model by one step.'''

        # Look over all the agents
        for a in self.schedule.agents:

            # Each agent looks at all the messages in the group
            for x in self.messages:

                # Remove some benefit of information access for every message read
                a.InfoB = a.InfoB - .1

                if x.topic in a.topic_interests:
                    # Gain some benefit for reading messages that match what you want to read
                    a.InfoB = a.InfoB + 1

        self.messages = []
        self.schedule.step()
