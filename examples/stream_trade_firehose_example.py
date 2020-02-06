import cryptowatch as cw
import time


cw.stream.subscriptions = ["markets:*:trades"]


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


cw.stream.connect()

# Stop receiving after 10 seconds
time.sleep(10)
cw.stream.disconnect()
