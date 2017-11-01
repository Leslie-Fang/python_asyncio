
import ccxt
import config as config
import json
# create the exchange instance
# bittrex = getattr (ccxt, 'bittrex') ({
#             'apiKey': config.apiKey,
#             'secret': config.secret
#         })
# symbol = 'MANA/ETH'
# # print(bittrex.fetch_trades(symbol))
# trades = bittrex.fetch_trades(symbol)
#
# print(ccxt.exchanges)
#
binance = getattr (ccxt, 'binance') ({
            'apiKey': config.apiKey,
            'secret': config.secret
        })
symbol = 'BNB/BTC'
# print(_1btcxe.markets)
#  print(binance.fetch_trades(symbol))
trades = binance.fetch_trades(symbol)
for trade in trades:
    print(trade)
    # print("tarde_id:{}".format(trade['info']['Id']))

    # document = {'Id': trade['info']['Id'], 'TimeStamp': trade['info']['TimeStamp'],
    #             'Quantity': trade['info']['Quantity'],
    #             'Price': trade['info']['Price'], 'Total': trade['info']['Total'], 'FillType': trade['info']['FillType'],
    #             'OrderType': trade['info']['OrderType'],
    #             'timestamp': trade['timestamp'], 'datetime': trade['datetime'], 'symbol': trade['symbol'],
    #             'type': trade['type'], 'side': trade['side'], 'price': trade['price'],
    #             'amount': trade['amount']}
    # document = json.loads(trade)
    document = trade
    print("document is {}".format(document))
    '''
    {'id': '475220',
     'info': {'Id': 475220, 'TimeStamp': '2017-10-25T13:43:50.373', 'Quantity': 10698.04760631, 'Price': 3.739e-05,
              'Total': 0.39999999, 'FillType': 'FILL', 'OrderType': 'BUY'}, 'timestamp': 1508939030000,
     'datetime': '2017-10-25T13:43:50.000Z', 'symbol': 'MANA/ETH', 'type': 'limit', 'side': 'buy', 'price': 3.739e-05,
     'amount': 10698.04760631}
    '''
    # time.sleep()

# markets = bittrex.fetchMarkets ()
# for item in markets:
#     print(item['symbol'])

# print(bittrex.fetch_trades('MANA/ETH')) # same as print(bittrex.fetchTrades('MANA/ETH'))
# trades = bittrex.fetch_trades('MANA/ETH')
# for item in trades:
#     print(item)
#
# get the order book for a specific symbol
# print(bittrex.fetch_order_book('MANA/ETH'))
#
# # get the Market Price
#
# # Price Tickers
# # print(bittrex.markets)
# print(bittrex.fetch_ticker('MANA/ETH')) # ticker for LTC/ZEC
# # symbols = list(bittrex.markets.keys())


# print(bittrex.accountGetDepositaddress({'currency': 'BTC'}))

# get trades
# print (bittrex.fetch_trades (symbol)[0])
