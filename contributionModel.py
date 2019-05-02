# model.py
from mesa import Agent, Model
from mesa.datacollection import DataCollector
from mesa.time import RandomActivation
import random

potential_topics = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
random.seed(a=123)
unique_id = 0


class GroupMember(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Benefit from Information Access
        self.InfoB = 10
        self.unique_id = unique_id
        # Choose a random topic to be your choice
        self.topic_interests = random.choice(potential_topics)


class Message:
    def __init__(self, topic):
        self.topic = topic
        # print(topic)


def compute_benefit(model):
    b = 0
    for member in model.schedule.agents:
        b = b + member.InfoB

    if len(model.schedule.agents) == 0:
        return 0

    a = b / len(model.schedule.agents)
    return a


def compute_member_joined(model):
    return model.member_joined


def compute_member_left(model):
    return model.member_left


class Community(Model):
    """A model with some number of agents."""
    def __init__(self, N, M, topics):
        global unique_id
        self.schedule = RandomActivation(self)

        # Group was initialied with n members
        self.num_agents = N
        # Group is initialized with m messages
        self.totalMessages = M
        self.messages = []
        self.member_joined = 0
        self.member_left = 0

        for x in range(self.totalMessages):
            # self.messages.append(Message("A"))
            self.messages.append(Message(random.choice(topics)))

        self.topics = topics
        # Create agents
        for i in range(self.num_agents):
            unique_id = i
            a = GroupMember(i, self)
            self.schedule.add(a)
        
        self.datacollector = DataCollector(
                model_reporters = {
                    "Average_Info_Benefit": compute_benefit,
                    "Count_of_Members_Joined": compute_member_joined,
                    "Count_of_Members_Left": compute_member_left

                    # "Messge Topics": compute_topics
                }
            )

    def step(self):
        # Look over all the agents
        for a in self.schedule.agents:

            # Calculate the cost to read messages
            if len(self.messages) > 0:
                count_of_interest = 0
                for x in self.messages:
                    if x.topic in a.topic_interests:
                        count_of_interest = count_of_interest + 1

                # Calculate reading benefit: 1 while < 40 | 1/x while above 40
                if count_of_interest < 40:
                    a.InfoB = a.InfoB + count_of_interest
                else:
                    a.InfoB = a.InfoB + 40
                    for j in range(1, count_of_interest % 40):
                        a.InfoB = a.InfoB + 1 / j

                # The cost is the proportion of irrelevant messages
                cost = 1 - (count_of_interest / len(self.messages))
                a.InfoB = a.InfoB - (a.InfoB * cost)

                # not_interesting = len(self.messages) - count_of_interest
                #
                # if not_interesting == 0:
                #     signal_to_noise = 1
                # else:
                #     signal_to_noise = count_of_interest / not_interesting
                #
                #
                # # If signal to noise is 0, all of the messages were not interesting
                # if signal_to_noise == 0:
                #     # If nothing was interesting remove half of your benefit
                #     a.InfoB = a.InfoB / 2
                # else:
                #     cost = len(self.messages) / signal_to_noise
                #     print(len(self.messages))
                #     a.InfoB = a.InfoB - cost

    def post(self):
        global unique_id
        self.messages = []
        for a in self.schedule.agents:
            if a.InfoB >= 1:
                new_message_topic = random.choice(a.topic_interests)
                new_message = Message(new_message_topic)
                self.messages.append(new_message)
                # a.InfoB = a.InfoB - .1 * a.InfoB

        if len(self.schedule.agents) < 25:
            a = GroupMember(unique_id + 1, self)
            unique_id = unique_id + 1
            self.schedule.add(a)
            self.member_joined = self.member_joined + 1

        for a in self.schedule.agents:
            if a.InfoB < 1:
                self.schedule.remove(a)
                self.member_left = self.member_left + 1

        Agents = []
        for a in self.schedule.agents:
            Agents.append(a.topic_interests)
        print(Agents)

        self.datacollector.collect(self)
        self.schedule.step()
