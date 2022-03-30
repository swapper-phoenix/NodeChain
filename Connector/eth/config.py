#!/usr/bin/python3
from json import JSONEncoder


class Config:

    def __init__(self, coin, networkName):

        self._coin = coin
        self._networkName = networkName

        self._rpcEndpoint = ""
        self._wsEndpoint = ""

    def loadConfig(self, config):
        self.rpcEndpoint = config["rpcEndpoint"]
        self.wsEndpoint = config["wsEndpoint"]

        return True, None

    @property
    def coin(self):
        return self._coin

    @property
    def networkName(self):
        return self._networkName

    @networkName.setter
    def networkName(self, value):
        self._networkName = value

    @property
    def rpcEndpoint(self):
        return self._rpcEndpoint

    @rpcEndpoint.setter
    def rpcEndpoint(self, value):
        self._rpcEndpoint = value

    @property
    def wsEndpoint(self):
        return self._wsEndpoint

    @wsEndpoint.setter
    def wsEndpoint(self, value):
        self._wsEndpoint = value

    def jsonEncode(self):
        return ConfigEncoder().encode(self)


class ConfigEncoder(JSONEncoder):

    def encode(self, o):
        return {
            "rpcEndpoint": o.rpcEndpoint,
            "wsEndpoint": o.wsEndpoint
        }
