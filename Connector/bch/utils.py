#!/usr/bin/python3
from decimal import Decimal
from .constants import *


def convertToSatoshi(strAmount):
    return str(int(Decimal(strAmount) * 100000000))


def getMethodSchemas(name):
    return getRequestMethodSchema(name), getResponseMethodSchema(name)


def getRequestMethodSchema(name):
    return RPC_JSON_SCHEMA_FOLDER + name + SCHEMA_CHAR_SEPARATOR + REQUEST + SCHEMA_EXTENSION


def getResponseMethodSchema(name):
    return RPC_JSON_SCHEMA_FOLDER + name + SCHEMA_CHAR_SEPARATOR + RESPONSE + SCHEMA_EXTENSION


def parseBalancesToTransfers(vin, vout, fee, amount):

    transfers = []
    diff = 0

    for utxo in vout:

        if utxo["category"] == "send":

            for address in list(vin.keys()):

                voutAmount = -utxo[AMOUNT]
                vinAmount = vin[address]

                if vinAmount <= (voutAmount + diff):
                    transfer = {
                        "from": address,
                        "to": utxo[ADDRESS],
                        AMOUNT: vinAmount,
                        "fee": round(vinAmount * fee / amount, BTC_CASH_PRECISION)
                    }
                    del vin[address]
                else:
                    transfer = {
                        "from": address,
                        "to": utxo[ADDRESS],
                        AMOUNT: voutAmount,
                        "fee": round(voutAmount * fee / amount, BTC_CASH_PRECISION)
                    }

                diff = diff + voutAmount - vinAmount
                transfers.append(transfer)

        if utxo["category"] in ["generate", "immature", "orphan"]:
            transfers.append(
                {
                    "to": utxo[ADDRESS],
                    "fee": 0,
                    AMOUNT: utxo[AMOUNT]
                }
            )

    return transfers
