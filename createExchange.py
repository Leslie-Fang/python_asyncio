# import ccxt  # use sync ccxt
import ccxt.async as ccxt # use async ccxt

## several ways to create the exchanges
exchange = ccxt.okcoinusd () # default id
okcoin1 = ccxt.okcoinusd ({ 'id': 'okcoin1' })
okcoin2 = ccxt.okcoinusd ({ 'id': 'okcoin2' })

# second way
id = 'btcchina'
btcchina = eval ('ccxt.%s ()' % id)

# thrid way
gdax = getattr (ccxt, 'gdax') ()