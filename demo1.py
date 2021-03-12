# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 10:17:52 2021

@author: gxw
"""

import plotly.graph_objects as go
import networkx as nx
import json

with open('layers.json') as f:
     layers = json.load(f)

tx = []
edges = []
for i in range(len(layers) - 2):
    print("第{0}层".format(i))
    layer = layers[i]
    recipients = []
    value = []
    for nodes_group in layer:
        for node in nodes_group:
            recipients.append(node['addr'])
            value.append(node['value'])
            
    next_layer = layers[i+1]
    for j in range(len(recipients)):
        for node in next_layer[j]:
            tx.append((node['addr'], recipients[j], value[j]))
            edges.append((node['addr'], recipients[j]))

