#!/usr/bin/python3
from .constants import *


def ensureHash(hashAddr):
    if isinstance(hashAddr, str):
        if hashAddr.startswith('0x'):
            return hashAddr.lower()
        else:
            return '0x' + hashAddr.lower()
    else:
        return hashAddr.lower()


def getMethodSchemas(name):
    return getRequestMethodSchema(name), getResponseMethodSchema(name)


def getRequestMethodSchema(name):
    return RPC_JSON_SCHEMA_FOLDER + name + SCHEMA_CHAR_SEPARATOR + REQUEST + SCHEMA_EXTENSION


def getResponseMethodSchema(name):
    return RPC_JSON_SCHEMA_FOLDER + name + SCHEMA_CHAR_SEPARATOR + RESPONSE + SCHEMA_EXTENSION


def getWSMethodSchemas(name):
    return getWSRequestMethodSchema(name), getWSResponseMethodSchema(name)


def getWSRequestMethodSchema(name):
    return WS_JSON_SCHEMA_FOLDER + name + SCHEMA_CHAR_SEPARATOR + REQUEST + SCHEMA_EXTENSION


def getWSResponseMethodSchema(name):
    return WS_JSON_SCHEMA_FOLDER + name + SCHEMA_CHAR_SEPARATOR + RESPONSE + SCHEMA_EXTENSION


def isAdressInBlock(address, block):
    for transaction in block[TRANSACTIONS]:
        if address.lower() == transaction[FROM].lower() or address.lower() == transaction[TO].lower():
            return True
    return False


def getSyncPercentage(currentBlock, latestBlock):
    return (currentBlock * 100) / latestBlock
