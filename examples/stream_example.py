import cryptowatch as cw
import logging

logging.basicConfig()
logging.getLogger("cryptowatch").setLevel(logging.DEBUG)


# Set your API Key
# cw.api_key = "XXXXXXXXXXXXXXXXXXXX"

cw.stream.subscriptions = ["markets:*:trades", "markets:*:ohlc"]
# cw.stream.subscriptions = ["assets:60:book:snapshots"]
# cw.stream.subscriptions = ["assets:60:book:spread"]
# cw.stream.subscriptions = ["assets:60:book:deltas"]
# cw.stream.subscriptions = ["markets:*:ohlc"]
# cw.stream.subscriptions = ["markets:*:trades"]


# What to do with each trade update
def handle_trades_update(trade_update):
    market_msg = ">>> Market#{} Exchange#{} Pair#{}: {} New Trades".format(
        trade_update.market_id,
        trade_update.exchange_id,
        trade_update.currency_pair_id,
        len(trade_update.trades),
    )
    print(market_msg)
    for trade in trade_update.trades:
        trade_msg = "\tID:{} TIMESTAMP:{} PRICE:{} AMOUNT:{} SIDE:{}".format(
            trade.external_id,
            trade.timestamp,
            trade.price,
            trade.amount,
            trade.order_side,
        )
        print(trade_msg)


cw.stream.on_trades_update = handle_trades_update


# What to do with each candle update
def handle_intervals_update(interval_update):
    market_msg = ">>> Market#{} Exchange#{} Pair#{}: {} New Candles".format(
        interval_update.market_id,
        interval_update.exchange_id,
        interval_update.currency_pair_id,
        len(interval_update.candles),
    )
    print(market_msg)
    for candle in interval_update.candles:
        candle_msg = "\tO:{} H:{} L:{} C:{} V:{} VB:{} PERIOD:{} CLOSE_TIMESTAMP:{}".format(
            candle.open,
            candle.high,
            candle.low,
            candle.close,
            candle.volume,
            candle.volume_base,
            candle.period,
            candle.close_timestamp,
        )
        print(candle_msg)


cw.stream.on_intervals_update = handle_intervals_update


# What to do with each orderbook spread update
def handle_orderbook_snapshot_updates(orderbook_snapshot_update):
    market_msg = ">>> Market#{} Exchange#{} Pair#{}".format(
        orderbook_snapshot_update.market_id,
        orderbook_snapshot_update.exchange_id,
        orderbook_snapshot_update.currency_pair_id,
    )
    print(market_msg)
    bids_msg = "\tBIDS:{}".format(
        ["{}@{}".format(b.price, b.amount) for b in orderbook_snapshot_update.book.bids]
    )
    print(bids_msg)
    asks_msg = "\tASKS:{}".format(
        ["{}@{}".format(a.price, a.amount) for a in orderbook_snapshot_update.book.asks]
    )
    print(asks_msg)


cw.stream.on_orderbook_snapshot_update = handle_orderbook_snapshot_updates


# What to do with each orderbook spread update
def handle_orderbook_spread_updates(orderbook_spread_update):
    market_msg = ">>> Market#{} Exchange#{} Pair#{}".format(
        orderbook_spread_update.market_id,
        orderbook_spread_update.exchange_id,
        orderbook_spread_update.currency_pair_id,
    )
    print(market_msg)
    orderbook_spread_msg = "\tBEST_BID:{} (AMOUNT:{})  BEST_ASK:{} (AMOUNT:{})  TIMESTAMP:{} ".format(
        orderbook_spread_update.spread.bid.price,
        orderbook_spread_update.spread.bid.amount,
        orderbook_spread_update.spread.ask.price,
        orderbook_spread_update.spread.ask.amount,
        orderbook_spread_update.spread.timestamp,
    )
    print(orderbook_spread_msg)


cw.stream.on_orderbook_spread_update = handle_orderbook_spread_updates


# What to do with each orderbook delta update
def handle_orderbook_delta_updates(orderbook_delta_update):
    market_msg = ">>> Market#{} Exchange#{} Pair#{}".format(
        orderbook_delta_update.market_id,
        orderbook_delta_update.exchange_id,
        orderbook_delta_update.currency_pair_id,
    )
    print(market_msg)
    bids_ops = "\tSET:{}  REMOVE:{}".format(
        orderbook_delta_update.book.bids.set, orderbook_delta_update.book.bids.remove
    )
    asks_ops = "\tSET:{}  REMOVE:{}".format(
        orderbook_delta_update.book.asks.set, orderbook_delta_update.book.asks.remove
    )
    print(bids_ops)
    print(asks_ops)


cw.stream.on_orderbook_delta_update = handle_orderbook_delta_updates


# Start receiving
cw.stream.connect()


# Stop receiving
# cw.stream.disconnect()
