from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
import numpy as np
from enum import Enum, auto


def parse_generator(args):
    if args['sim_type'] == 'constant':
        return lambda: args['sim_percentage']
    if args['sim_type'] == 'normal':
        return lambda: np.random.normal(
            args['mean'],
            args['deviation'],
            1
        )

class Groups(Enum):
    GREEN = auto()
    RED = auto()
    BLUE = auto()

class Citizen(Agent):
    """Citizen with a certain tolerance"""

    def __init__(self, unique_id, group, model, desired_sim):
        self.unique_id = unique_id
        self.group = group
        self.desired_sim = desired_sim
        super().__init__(unique_id, model)

    def get_curr_sim(self):
        nei = self.model.grid.get_neighbors(
            self.pos, moore=True, include_center=False
        )
        if len(nei) == 0:
             return 0

        sim_nei = [n for n in nei if n.group == self.group]
        return len(sim_nei)/len(nei)

    def is_satisfied(self):
        return self.get_curr_sim() >= self.desired_sim()

    def step(self):
        """
        At each step, a citizen will relocate if their neighbors are too
        different.
        """

        if not self.is_satisfied():
            self.model.grid.move_to_empty(self)


class City(Model):
    """
    Schelling segregation model is a simple model used to explain segregation in
    urban areas.

    Each citizen has a certain tolerance level, and will relocate if their
    current position doesn't conform to thei tolerance level.
    """

    def __init__(self, density, width, height, conv_len=10, num_groups=2,
                 **kwargs):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.grid = Grid(width=width, height=height, torus=True)
        self.running = True
        self.conv_len = conv_len
        self.steps = 0

        num_agents = round(width * height * density)
        groups = [g for g in Groups][:num_groups]

        for i in range(num_agents):
            agent = Citizen(
                i,
                self.random.choice(groups),
                self,
                parse_generator(kwargs)
            )
            self.schedule.add(agent)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

        self.datacollector = DataCollector(
            model_reporters={
                "satisfied_citizens": lambda m: m.satisfied_count()
            }
        )

        self.running = True
        self.datacollector.collect(self)

    def has_converged(self):
        if self.steps >= self.conv_len:
            sat_counts = self.datacollector.get_model_vars_dataframe()
            lasts = sat_counts.tail(self.conv_len)
            uniques = lasts.nunique()
            return uniques[0] != 1
        return True

    def satisfied_count(self):
        sats = [
            a for a in self.schedule.agents
            if a.is_satisfied()
        ]
        return len(sats)

    def step(self):
        """
        At each step, move unsatisfied citizens
        """
        self.steps += 1
        self.datacollector.collect(self)
        self.schedule.step()
        self.running = self.has_converged()
