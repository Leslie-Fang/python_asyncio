
import ccxt
import config as config
# create the exchange instance
bittrex = getattr (ccxt, 'bittrex') ({
            'apiKey': config.apiKey,
            'secret': config.secret
        })
symbol = 'MANA/ETH'
# print all the supported method
# print (dir(bittrex))
#
# print (dir(bittrex.api))
#
print(bittrex.fetchMarkets ())
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
