"""
Configure visualization elements and instantiate a server
"""

from .model import Termite, Chip, Nest, ChipColors

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

def termite_portrayal(agent):
    if agent is None:
        return None
    portrayal = {}
    if type(agent) == Termite:
        portrayal = {
            'Shape': 'circle',
            'r': 0.9,
            'Color': 'Blue',
            'Filled': 'true',
            'Layer': 1
        }

    
    elif type(agent) == Chip:
        chip_colors = {
            ChipColors.BROWN: 'Brown',
            ChipColors.YELLOW: 'Yellow'
        }
        portrayal = {
            'Shape': 'rect',
            'w': 0.9,
            'h': 0.9,
            'Color': chip_colors[agent.color],
            'Filled': 'true',
            'Layer': 0
        }
    return portrayal

canvas_element = CanvasGrid(termite_portrayal, 100, 100, 600, 600)

model_kwargs = {
    "num_agents": UserSettableParameter(
        param_type='slider',
        name='number of agents',
        value=400,
        min_value=1,
        max_value=1000,
        step=1
    ),
    'chip_density': UserSettableParameter(
        param_type='slider',
        name='density',
        value=0.2,
        min_value=0.01,
        max_value=1,
        step=0.01
    ),
    "width": 100,
    "height": 100,
    'get_away': UserSettableParameter(
        param_type='choice',
        name='move methode',
        value='jump',
        choices=['jump', 'teleport'],
    ),
    'num_chip_types': UserSettableParameter(
        param_type='choice',
        name='chips types',
        value=1,
        choices=[1,2]
    )
}

server = ModularServer(
    Nest,
    [canvas_element],
    "Termites",
    model_kwargs,
)
