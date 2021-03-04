"""
Configuraciones para la visualización del modelo
"""

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from .model import City, Groups

def color(g):
    """Defining group colots"""
    colors = {
        Groups.GREEN : 'Green',
        Groups.RED : 'Red',
        Groups.BLUE: 'Blue'
    }
    return colors[g]

def circle_portrayal_example(agent):
    """Citizen appereance"""
    if agent is None:
        return None

    portrayal = {
        'Shape': 'circle',
        'Filled': 'true',
        'Layer': 0,
        'r': 0.5,
        'Color': color(agent.group),
    }
    return portrayal

grid_side = 50

canvas_element = CanvasGrid(
    circle_portrayal_example,
    grid_side,
    grid_side
)

chart = ChartModule(
    [{'Label': 'satisfied_citizens','Color': 'Black'}],
    data_collector_name='datacollector'
)

def build_per_slider(name, value):
    return UserSettableParameter(
        param_type='slider',
        name=name,
        value=value,
        min_value=0,
        max_value=1,
        step=0.001
    )

def build_choice(name,  chs):
    return UserSettableParameter(
        param_type='choice',
        name=name,
        value=chs[0],
        choices=chs
    )

model_kwargs = {
    'density': build_per_slider('Population density', 0.9),
    'width': grid_side,
    'height': grid_side,
    'num_groups': build_choice('Number of groups', [2, 3]),
    'sim_type': build_choice('Similitud distribution', ['constant', 'normal']),
    'sim_percentage': build_per_slider('Similitud percentage', 0.7),
    'mean': build_per_slider('Similitud mean', 0.5),
    'deviation': build_per_slider('Similitud deviation', 0.1)
}

server = ModularServer(
    City,
    [canvas_element, chart],
    'Shelling Segregation',
    model_kwargs,
)
