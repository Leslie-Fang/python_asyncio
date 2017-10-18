# import ccxt.async as ccxt

import ccxt

# create the exchange instance
bittrex = getattr (ccxt, 'bittrex') ({
            'apiKey': 'a644796b09144d7a9e88102b7f113fe7',
            'secret': 'bef51b9a1c3342b596c3c208fb4d44c0'
        })

# # print(bittrex)
#
# # load all of the markets in the exchanges
# markets = bittrex.load_markets ()
# print (bittrex.id, markets)
#
# etheur1 = bittrex.markets['SALT/ETH']      # get market structure by symbol; 'SALT/ETH' is the symbol and should be in the markets
# print("etheur1 is {0}".format(etheur1))
# # etheur2 = bittrex.market ('SALT/ETH')      # same result in a slightly different way
# # print("etheur2 is {0}".format(etheur2))
#
# etheurId = bittrex.market_id ('SALT/ETH')  # get market id by symbol; Market ids are used during the REST request-response process to reference trading pairs within exchanges
# print("etheurId is {0}.".format(etheurId))
#
# symbols = bittrex.symbols                 # get a list of symbols
# print("symbols is {0}".format(symbols))
#
# symbols2 = list (bittrex.markets.keys ()) # same as previous line
# print("symbols2 is {0}".format(symbols2))

currencies = bittrex.currencies           # a list of currencies
print("currencies is {0}".format(currencies))


# kraken = ccxt.kraken ()
# kraken.load_markets ()
#
# kraken.markets['BTC/USD']                  # symbol → market (get market by symbol)
# kraken.markets_by_id['XXRPZUSD']           # id → market (get market by id)
#
# kraken.markets['BTC/USD']['id']            # symbol → id (get id by symbol)
# kraken.markets_by_id['XXRPZUSD']['symbol'] # id → symbol (get symbol by id)