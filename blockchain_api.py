# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:20:21 2021

@author: gxw
"""
from urllib import request
# blockheight = 100000
# url = "https://blockchain.info/block-height/" + str(blockheight) + "?format=json"
# header = {
#     'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
#     }
# rq = request.Request(url, headers = header)
# resp = request.urlopen(rq)
# print(resp.read().decode('utf-8'))

def api_blockchain(blockheight):
    """
    调用blockchian.info网站的API
    """
    #请求头构建
    header = {
        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko)' +
        ' Chrome/86.0.4240.75 Safari/537.36'
    }
    url = "https://blockchain.info/block-height/" + str(blockheight) + "?format=json"
    rq = request.Request(url, headers=header)
    resp = request.urlopen(rq)
    print(resp.read().decode('utf-8'))

api_blockchain(100000)