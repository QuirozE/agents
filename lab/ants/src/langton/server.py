"""
Configure visualization elements and instantiate a server
"""

from .model import Cell, Grid

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter


def cell_portrayal(agent):
    if agent is None:
        return None

    colors = [
        'White', # dead
        '#AB47BC', # core
        '#37474F', # armor
        '#FF7043', # channels
        # the rest are data
        '#E91E63',
        '#673AB7',
        '#2196F3',
        '#26C6DA'
    ]

    portrayal = {
        'Shape': 'rect',
        'Filled': 'true',
        'w': 0.9,
        'h': 0.9,
        'Layer': 0,
        'Color': colors[agent.state],
    }
    return portrayal

side = 150

canvas_element = CanvasGrid(
    cell_portrayal,
    side, side,
    4*side, 4*side
)

model_kwargs = {
    'side': side,
    'x_off': UserSettableParameter(
        param_type='slider',
        name='x offset',
        value=side//2-1,
        min_value=0,
        max_value=side,
        description='Initial x position of the first loop'
    ),
    'y_off': UserSettableParameter(
        param_type='slider',
        name='y offset',
        value=side//2-1,
        min_value=0,
        max_value=side,
        description='Initial y position of the first loop'
    )
}

server = ModularServer(
    Grid,
    [canvas_element],
    'Langton',
    model_kwargs,
)
