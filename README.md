# Cryptowatch Python SDK

The Cryptowatch Python library provides a convenient access to the [Cryptowatch API](https://docs.cryptowat.ch/home/) from applications written in the Python language.

It includes the following features:
 * Auto-serialization of API responses into Python objects
 * API credentials automatically read from your `~/.cw/credentials.yml` config file
 * Custom exceptions for API-specific issues (e.g.: Requests Allowance)
 * Smart back-off retries in case of API connectivity loss


## Installation
```
pip install cryptowatch
```

### Requirements

* python v3.7+
* requests v0.8.8+
* marshmallow v3.2.2+
* pyyaml v5.1.2+

## Usage

### REST API

```python
import cryptowatch as cw

# Authenticate the cryptowatch client
cw.api_key = "YOUR_PUBLIC_API_KEY"

# Assets
cw.assets.list()
cw.assets.get("BTC")

# Exchanges
cw.exchanges.list()
cw.exchanges.get("KRAKEN")

# Instruments
cw.instruments.list()
cw.instruments.get("BTCUSD")

# Markets
cw.markets.list() # Returns list of all markets on all exchanges
cw.markets.list("BINANCE") # Returns all markets on Binance

# Returns market summary (last, high, low, change, volume)
cw.markets.get("KRAKEN:BTCUSD")
# Return market candlestick info (open, high, low, close, volume) on some timeframes
cw.markets.get("KRAKEN:BTCUSD", "ohlc", periods=["4h", "1h", "1d"])

# Returns market last trades
cw.markets.get("KRAKEN:BTCUSD", "trades")

# Return market current orderbook
cw.markets.get("KRAKEN:BTCUSD", "orderbook")
# Return market current orderbook liquidity
cw.markets.get("KRAKEN:BTCUSD", "liquidity")
```

### Logging

Logging can be enabled through Python's `logging` module:

```python
import logging

logging.basicConfig()
logging.getLogger("cryptowatch").setLevel(logging.DEBUG)
```

### CLI

The module exposes a simple utility, via the `-m` option, to return last market prices.

#### By default it returns Kraken's BTCUSD market

```
> python -m cryptowatch
7425.0
```

#### Add another Kraken market to return this market last price

```
> python -m cryptowatch btceur
6758.1
```

#### You can also specify your own exchange

```
> python -m cryptowatch binance:ethbtc
0.020359
```

When the market doesn't exist a return code of `1` will be set (`0` otherwise):

```
> python -m cryptowatch binance:nosuchmarketusd
> echo $?
1
```



## Testing

Unit tests are under the [tests](tests) folder and use `pytest`, run them all with:

```
make test
```

Integration tests sending real HTTP requests to the Cryptowatch API can be run with:

```
make test-http-real
```

## Development

Testing and developement dependencies are in the [requirements.txt](requirements.txt) file, install them with:

```
pip install -r requirements.txt
```

The code base use the [Black](https://black.readthedocs.io/en/stable/) linter, run it with:

```
make lint
```

## License

[BSD-2-Clause](LICENSE)
