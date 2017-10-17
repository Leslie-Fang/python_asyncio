import ccxt.async as ccxt
# print(getattr(ccxt, 'bittrex')())
# # print(ccxt.exchanges)
for market in ccxt.exchanges:
    print("The market is {}.".format(market))

# import ccxt
exchange = ccxt.okcoinusd ()
print(exchange)

