#!/usr/bin/python3
GET_BALANCE_METHOD = "eth_getBalance"
GET_BLOCK_BY_NUMBER_METHOD = "eth_getBlockByNumber"
GET_BLOCK_BY_HASH_METHOD = "eth_getBlockByHash"
GET_TRANSACTION_BY_HASH_METHOD = "eth_getTransactionByHash"
GET_TRANSACTION_COUNT_METHOD = "eth_getTransactionCount"
GET_GAS_PRICE_METHOD = "eth_gasPrice"
GET_TRANSACTION_RECEIPT_METHOD = "eth_getTransactionReceipt"
SEND_RAW_TRANSACTION_METHOD = "eth_sendRawTransaction"
ESTIMATE_GAS_METHOD = "eth_estimateGas"
SUBSCRIBE_METHOD = "eth_subscribe"
SYNCING_METHOD = "eth_syncing"
CALL_METHOD = "eth_call"
TXPOOL_CONTENT = "txpool_content"

NEW_HEADS_SUBSCRIPTION = "newHeads"

RPC_JSON_SCHEMA_FOLDER = "eth/rpcschemas/"
WS_JSON_SCHEMA_FOLDER = "eth/wsschemas/"
SCHEMA_CHAR_SEPARATOR = "_"
REQUEST = "request"
RESPONSE = "response"
SCHEMA_EXTENSION = ".json"

GET_ADDRESS_BALANCE = "getaddressbalance"
GET_ADDRESSES_BALANCE = "getaddressesbalance"
GET_HEIGHT = "getheight"
BROADCAST_TRANSACTION = "broadcasttransaction"
GET_BLOCK_BY_HASH = "getblockbyhash"
GET_BLOCK_BY_NUMBER = "getblockbynumber"
GET_ADDRESS_TRANSACTION_COUNT = "getaddresstransactioncount"
GET_ADDRESSES_TRANSACTION_COUNT = "getaddressestransactioncount"
GET_GAS_PRICE = "getgasprice"
ESTIMATE_GAS = "estimategas"
GET_TRANSACTION = "gettransaction"
GET_TRANSACTIONS = "gettransactions"
GET_TRANSACTION_RECEIPT = "gettransactionreceipt"
SUBSCRIBE_ADDRESS_BALANCE = "subscribetoaddressbalance"
UNSUBSCRIBE_ADDRESS_BALANCE = "unsubscribefromaddressbalance"
SYNCING = "syncing"
CALL = "call"
GET_ADDRESS_HISTORY = "getaddresshistory"
GET_ADDRESSES_HISTORY = "getaddresseshistory"
SUBSCRIBE_TO_NEW_BLOCKS = "subscribetonewblocks"
UNSUBSCRIBE_FROM_NEW_BLOCKS = "unsubscribefromnewblocks"
GET_PENDING_TRANSACTIONS = "getpendingtransactions"

INDEXER_TXS_PATH = "/ethtxs"
GRAPHQL_PATH = "/graphql"

COIN_SYMBOL = "eth"
DEFAULT_PKG_CONF = "defaultConf.json"
