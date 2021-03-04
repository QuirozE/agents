from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from enum import Enum, auto

def present_color(d):
    for c, l in d.items():
        if len(l) > 0:
            return c
    return None

class ChipColors(Enum):
    YELLOW = auto()
    BROWN = auto()

class Chip(Agent):
    def __init__(self, unique_id, color, model):
        self.unique_id = unique_id
        self.color = color
        self.taken = False
        super().__init__(unique_id, model)

    def step(self):
        pass

class Termite(Agent):
    """
    A termite wanders aimlessly until it finds an wood chip and picks it up.
    It continues to wander until it finds another chip, then it drops its
    package and continues to wander empty handed.
    """

    def __init__(self, unique_id, direction, model, vis_angle=50):
        self.unique_id = unique_id
        self.direction = direction
        self.vis_angle=vis_angle
        self.chip = None
        super().__init__(unique_id, model)

    def chips_at_pos(self):
        x, y = self.pos
        agents_at_pos =  self.model.grid[x][y]
        chips = {c: [] for c in ChipColors}
        for agent in agents_at_pos:
            if isinstance(agent, Chip) and agent != self.chip:
                chips[agent.color].append(agent)
        return chips

    def rotate(self, angle):
        self.direction = (self.direction + angle) % 360

    def forward(self, jump_size):
        from math import cos, sin
        dx, dy = jump_size * cos(self.direction),jump_size*sin(self.direction)
        dx, dy = round(dx), round(dy)
        x, y = self.pos
        self.model.grid.move_agent(self, (x+dx, y+dy))
        if self.chip is not None:
            self.model.grid.move_agent(self.chip, (x+dx, y+dy))

    def wiggle(self):
        self.forward(1)
        self.rotate(self.random.randrange(self.vis_angle))
        self.rotate(-self.random.randrange(self.vis_angle))

    def rand_jump(self, jump_dist):
        self.rotate(self.random.uniform(0, 360))
        self.forward(jump_dist)

    def random_teleport(self):
        x = self.random.randrange(self.model.grid.width)
        y = self.random.randrange(self.model.grid.height)

        self.model.grid.move_agent(self, (x, y))

    def get_away(self):
        m = self.model.get_away_method
        while present_color(self.chips_at_pos()) is not None:
            if m == 'jump':
                self.rand_jump(self.model.jump_dist)
            elif m == 'teleport':
                self.random_teleport()

    def find_chip(self):
        if self.chip is None:
            _, chip = self.find_any_pile()
            chip[0].taken = True
            self.chip = chip[0]
            self.rotate(180)
            self.forward(self.model.jump_dist)

    def find_any_pile(self):
        while present_color(self.chips_at_pos()) is None:
            self.wiggle()
        chips = self.chips_at_pos()
        c = present_color(chips)
        return (c, chips[c])

    def find_sim_pile(self):
        if self.chip is not None:
            c, chips = self.find_any_pile()
            while c != self.chip.color:
                self.wiggle()
                c, chips = self.find_any_pile()
            return chips

    def drop_chip(self):
        if self.chip is not None:
            while present_color(self.chips_at_pos()) == self.chip.color:
                self.rand_jump(1)
            self.chip.taken = False
            self.chip = None
            self.get_away()

    def step(self):
        self.find_chip()
        self.find_sim_pile()
        self.drop_chip()

class Nest(Model):
    """
    A Termite nest is full of wood chips an termites. Termites will naturally
    try to collect chips, and move them toward other chips, creating chip heaps.
    """

    def __init__(
            self,
            num_agents,
            width, height,
            chip_density=0.2,
            jump_dist=20,
            get_away='jump',
            num_chip_types=1,
    ):
        super().__init__()
        self.num_agents = num_agents
        self.jump_dist = jump_dist
        self.get_away_method = get_away
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width=width, height=height, torus=True)

        for i in range(self.num_agents):
            agent = Termite(i, self.random.randrange(360), self)
            self.schedule.add(agent)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

        chipColors = list(ChipColors)[:num_chip_types]
        for i in range(round(height*width*chip_density)):
            chip = Chip(
                i+num_agents,
                self.random.choice(chipColors),
                self
            )
            self.schedule.add(chip)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(chip, (x, y))

        self.datacollector = DataCollector(
            model_reporters = {
                "busy_termites": lambda m: m.num_busy_termites()
            }
        )

        self.running = True
        self.datacollector.collect(self)

    def num_busy_termites(self):
        bt = [
            t for t in self.schedule.agents
            if isinstance(t, Chip) and t.color == ChipColors.BROWN
        ]
        return len(bt)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
