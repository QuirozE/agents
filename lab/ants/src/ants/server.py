"""
Configure visualization elements and instantiate a server
"""


from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from .model import Ant, Colony

def ant_portrayal(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5,
    }
    if agent.energy > 0:
        portrayal['Color'] = 'Red'
    else:
        portrayal['Color'] = 'Blue'
    return portrayal

canvas_element = CanvasGrid(ant_portrayal, 10, 10, 500, 500)

chart = ChartModule(
    [{'Label': 'active_count','Color': 'Black'}],
    data_collector_name='datacollector'
)

model_kwargs = {
    "density": UserSettableParameter(
        param_type='slider',
        name="density",
        value=0.2,
        min_value=0,
        max_value=1,
        step=0.001
    ),
    "gain": UserSettableParameter(
        param_type='slider',
        name="gain",
        value=0.01,
        min_value=0.005,
        max_value=0.5,
        step=0.001
    ),
    "width": 10,
    "height": 10
}

server = ModularServer(
    Colony,
    [canvas_element, chart],
    "Shelling",
    model_kwargs,
)
