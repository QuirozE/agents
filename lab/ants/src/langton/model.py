from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

from .rules import apply_transition, init_state

class Cell(Agent):
    def __init__(self, unique_id, model, state=0):
        self.unique_id = unique_id
        self.state = state
        self.next_state = 0
        super().__init__(unique_id, model)

    def advance(self):
        self.state = self.next_state

    def step(self):
        ps = [
            self.model.grid.torus_adj(
                (self.pos[0] + p[0], self.pos[1] + p[1])
            )
            for p in [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ]
        s = tuple([self.state] + [
            self.model.grid[p[0]][p[1]].state
            for p in ps
        ])

        ns = apply_transition(s)
        if ns is None:
            self.next_state = self.state
        else:
            self.next_state = ns


class Grid(Model):
    """
    The model class holds the model-level attributes, manages the agents, and generally handles
    the global level of our model.
    There is only one model-level parameter: how many agents the model contains. When a new model
    is started, we want it to populate itself with the given number of agents.
    The scheduler is a special model component which controls the order in which agents are activated.
    """

    def __init__(self, side, x_off, y_off):
        super().__init__()
        self.schedule = SimultaneousActivation(self)
        self.grid = SingleGrid(width=side, height=side, torus=True)

        for i in range(side):
            for j in range(side):
                agent = Cell(j*side+i, self)
                if 0 <= i - y_off and i - y_off < len(init_state):
                    if 0 <= j - x_off and j - x_off < len(init_state[i-y_off]):
                        agent.state = init_state[i-y_off][j-x_off]
                self.schedule.add(agent)
                self.grid.place_agent(agent, (j, i))

        # example data collector
        self.datacollector = DataCollector()

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
