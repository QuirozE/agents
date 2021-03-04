

from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

def v_zero(n, vz=1e-16):
    return 0 if n < vz else n

class Ant(Agent):  # noqa
    """
    An agent
    """

    def __init__(self, unique_id, model):
        """
        Customize the agent
        """
        self.unique_id = unique_id
        self.energy = 0
        self.next_energy = 0
        super().__init__(unique_id, model)


    def nei_energy(self):
        return sum([
            a.energy for a in self.model.grid.get_neighbors(
                self.pos, moore=True, include_center=False
            )
        ])

    def energy_step(self):
        from math import tanh
        energy_sum = self.energy + self.nei_energy()
        return tanh(self.model.gain*energy_sum)

    def advance(self):
        self.energy = self.next_energy

        if self.energy > 0:
            nei = self.model.grid.get_neighborhood(self.pos, moore=True)
            self.model.grid.move_agent(self, self.random.choice(nei))

    def step(self):
        if self.energy == 0:
            if self.random.random() < self.model.act_prob or self.nei_energy() > 0:
                self.next_energy = self.model.init_energy
        else:
            self.next_energy = v_zero(self.energy_step())


class Colony(Model):
    """
    The model class holds the model-level attributes, manages the agents, and generally handles
    the global level of our model.
    There is only one model-level parameter: how many agents the model contains. When a new model
    is started, we want it to populate itself with the given number of agents.
    The scheduler is a special model component which controls the order in which agents are activated.
    """

    def __init__(
            self,
            width, height,
            density=0.9, act_prob=0.01, gain=0.01, init_energy=1e-6
    ):
        super().__init__()
        self.act_prob = act_prob
        self.gain = gain
        self.init_energy = init_energy
        self.num_agents = round(width * height * density)
        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(width=width, height=height, torus=True)

        for i in range(self.num_agents):
            agent = Ant(i, self)
            self.schedule.add(agent)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

        # example data collector
        self.datacollector = DataCollector(
            model_reporters={
                'active_count': lambda m: m.count_active()
            })

        self.running = True
        self.datacollector.collect(self)

    def count_active(self):
        return sum([
            1 if a.energy > 0 else 0
            for a in self.schedule.agents
        ])

    def step(self):
        """
        A model step. Used for collecting data and advancing the schedule
        """
        self.datacollector.collect(self)
        self.schedule.step()
