"""CLI Script"""

from sys import argv

import termites.server as t
import ants.server as a
import langton.server as l
import shelling.server as s

options = {
    'termites': t.server,
    'ants': a.server,
    'langton': l.server,
    'schelling': s.server
}

server = options[argv[1]]

server.launch()
