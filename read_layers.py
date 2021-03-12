# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:00:16 2021
将backtracking.py存储的layers转换为数组对格式
便于之后的绘图
@author: gxw
"""
import json
import networkx as nx

with open('layers.json') as f:
     layers = json.load(f)

tx = []
for i in range(len(layers) - 2):
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

DG = nx.MultiDiGraph()
DG.add_weighted_edges_from(tx)
nx.draw_kamada_kawai(DG, 
                     node_color='r', 
                     with_labels=False, 
                     edge_color='b')
#x = nx.kamada_kawai_layout(DG)
#nx.draw_networkx_edge_labels(DG, pos=nx.kamada_kawai_layout(DG))
