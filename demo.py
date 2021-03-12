# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:03:42 2021

@author: gxw
"""
import btc_api
import pprint
import time
import json
import networkx as nx

layers = []

#初始化，构建第一个layer
txHash = str(input("请输入欲查询交易哈希:"))#'4b6ff89d262d56bb2f7d33f45cd96857e653c2531728d8470df88e3e38d6c0ec'
tx = btc_api.getSingleTx_ByHash(txHash)
last_time = time.time()

is_coinbase = tx['data']['is_coinbase']
inputs_count = tx['data']['inputs_count']
inputs_value = tx['data']['inputs_value']

inputs = tx['data']['inputs']

layer0 = []
nodes_group = []
for i in range(inputs_count):
    nodes_group.append({
        'block_height': tx['data']['block_height'],
        'addr': inputs[i]['prev_addresses'][0],
        'tx_hash': inputs[i]['prev_tx_hash'],
        'value': inputs[i]['prev_value']
        })
layer0.append(nodes_group)
layers.append(layer0)

found_coinbase = True
while(found_coinbase):
    #取出最后一层的节点
    layer = layers[-1]
    sub_layer = []
    #layer[nodes_group1, nodes_group2,...]
    for nodes_group in layer:
        #nodes_group[node1, node2,...]
        for node in nodes_group:
            #针对该节点构建下一个layer的nodes_group
            sub_nodes_group = []
            print(time.time()-last_time)
            if(time.time()-last_time < 5):
                time.sleep(5)
            tx = btc_api.getSingleTx_ByHash(node['tx_hash'])
            last_time = time.time()
            
            if(tx['data']['is_coinbase']) != True:
                inputs_count = tx['data']['inputs_count']
                inputs_value = tx['data']['inputs_value']
                inputs = tx['data']['inputs']
                
                for i in range(inputs_count):
                    sub_nodes_group.append({
                        'block_height': tx['data']['block_height'],
                        'addr': inputs[i]['prev_addresses'][0],
                        'tx_hash': inputs[i]['prev_tx_hash'],
                        'value': inputs[i]['prev_value']
                        })
                sub_layer.append(sub_nodes_group)
            else:
                found_coinbase = False
                sub_nodes_group.append({
                    'block_height': tx['data']['block_height'],
                    'tx_hash': tx['data']['hash'],
                    'value': tx['data']['outputs_value']
                    })
                sub_layer.append(sub_nodes_group)
                print("found coinbase tx!")
                print("txHash:", tx['data']['hash'])
                break
            
    layers.append(sub_layer)

with open('layers.json', 'w') as file_obj:
    json.dump(layers, file_obj)
    print("文件写入完毕.")
pprint.pprint(layers)

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

DG = nx.DiGraph()
DG.add_weighted_edges_from(tx)
nx.draw_kamada_kawai(DG, 
                     node_color='r', 
                     with_labels=False, 
                     edge_color='b')
#x = nx.kamada_kawai_layout(DG)
#nx.draw_networkx_edge_labels(DG, pos=nx.kamada_kawai_layout(DG))