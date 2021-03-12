# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:02:54 2021
本文档对btc.com的api进行请求，封装为python函数
@author: gxw
"""
import json
from urllib import request


def public_request(url):
    """
    各个api请求方法的通用部分
    """
    #请求头构建
    header = {
        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko)' +
        ' Chrome/86.0.4240.75 Safari/537.36'
    }
    try:
        rq = request.Request(url, headers=header)
        resp = request.urlopen(rq, timeout=30)
        data = resp.read().decode('utf-8')
        #将string转化为dict格式
        data = json.loads(data)
        #print(data)
        return data
    
    except Exception as error:
        print(error)
    

def getBlock_ByHeight(blockheight):
    """
    通过区块高度构建API请求
    blockheight有3种形式：
    1.单个数字，如100000
    2.字符串‘latest’代表最新块
    3.以逗号连接的字符串，如'latest,1,2,3'
    """
    url = "https://chain.api.btc.com/v3/block/" + str(blockheight)
    return( public_request(url) )
    
def getBlock_ByDate(date):
    """
    通过{ymd}格式的日期获取当日的区块列表
    注意date必须是20200201，即月份和日期必须补零
    """
    url = "https://chain.api.btc.com/v3/block/date/" + str(date)
    return( public_request(url) )

def getTxlist_ByBlockHeight(blockheight):
    """
    通过区块高度构建API请求
    blockheight有2种形式：
    1.单个数字，如100000
    2.字符串‘latest’代表最新块
    注意：不支持批量请求
    """
    url = "https://chain.api.btc.com/v3/block/" + str(blockheight) + "/tx" 
    return( public_request(url) )

def getSingleTx_ByHash(txHash):
    """
    通过交易哈希获取单笔交易详情
    txHash为string
    verbose有3个级别：
    等级 1，包含交易信息；
    等级 2，包含等级 1、交易的输入、输出地址与金额；
    等级 3，包含等级 2、交易的输入、输入 script 等信息
    """
    url = "https://chain.api.btc.com/v3/tx/" + txHash + "?verbose=3"
    return( public_request(url) )

def getUnconfirmed_TxHash():
    """
    返回所有未确认交易的哈希
    规模庞大，慎用
    """
    url = "https://chain.api.btc.com/v3/tx/unconfirmed"
    return( public_request(url) )

def getSingleAddr(addr):
    """
    addr为string格式
    获取单个地址信息,包括：
    received, sent, balance, tx_count, 
    unconfirmed_tx_count, unconfirmed_received, unconfirmed_sent,
    unspent_tx_count
    """
    url = "https://chain.api.btc.com/v3/address/" + addr
    return( public_request(url) )

def getTxList_ByAddr(addr):
    """
    addr为string格式
    """
    url = "https://chain.api.btc.com/v3/address/" + addr + "/tx"
    return( public_request(url) )

def getUnspentTx_ByAddr(addr):
    """
    获取特定地址的UTXO列表
    addr为string格式
    """
    url = "https://chain.api.btc.com/v3/address/" + addr + "/unspent"
    return( public_request(url) )
    
#data = getUnspentTx_ByAddr('15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew')
#getTxList_ByAddr('15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew')
#getSingleAddr('15urYnyeJe3gwbGJ74wcX89Tz7ZtsFDVew')
#getUnconfirmed_TxHash()
#data = getSingleTx_ByHash('c91ecb2ec0e0b7b01d0f1e41963289cfcc4358d1293068ec7086e737c5533ecb')
#getTxlist_ByBlockHeight('latest')
#getBlock_ByHeight('latest,1,2,3')
#getBlock_ByDate(20200203)