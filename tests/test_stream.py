import decimal

from cryptowatch.stream.resources import TradeMarketUpdateSchema
from cryptowatch.stream.resources import CandleMarketUpdateSchema
from cryptowatch.stream.resources import OrderbookSpreadMarketUpdateSchema
from cryptowatch.stream.resources import OrderbookSnapshotMarketUpdateSchema
from cryptowatch.stream.resources import OrderbookDeltaMarketUpdateSchema


def test_orderbook_delta_object_serialization():
    delta_samples = [
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "3",
                    "currencyPairId": "232",
                    "marketId": "75",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 995552,
                    "bids": {
                        "set": [
                            {"priceStr": "8298.15", "amountStr": "2.06"},
                            {"priceStr": "8298.19", "amountStr": "2"},
                            {"priceStr": "8298.2", "amountStr": "0.043"},
                            {"priceStr": "8298.23", "amountStr": "2"},
                            {"priceStr": "8298.24", "amountStr": "0.06"},
                        ],
                        "removeStr": [
                            "8298.08",
                            "8296.52",
                            "8296.49",
                            "8295",
                            "8298.18",
                        ],
                    },
                    "asks": {"set": [{"priceStr": "8327.17", "amountStr": "0.75"}]},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "1",
                    "currencyPairId": "232",
                    "marketId": "415",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 7027193,
                    "bids": {
                        "set": [
                            {"priceStr": "8325.3", "amountStr": "22.88719825"},
                            {"priceStr": "8298.6", "amountStr": "0.0053719"},
                        ],
                        "removeStr": ["8325"],
                    },
                    "asks": {
                        "set": [
                            {"priceStr": "8331.9", "amountStr": "0.005"},
                            {"priceStr": "8343.2", "amountStr": "0.84536225"},
                            {"priceStr": "8332", "amountStr": "0.04360893"},
                        ],
                        "removeStr": ["8341.4"],
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "16",
                    "currencyPairId": "109",
                    "marketId": "246",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 3609507,
                    "bids": {
                        "set": [
                            {"priceStr": "9382", "amountStr": "25179"},
                            {"priceStr": "9378", "amountStr": "56880"},
                            {"priceStr": "9376.5", "amountStr": "600"},
                            {"priceStr": "9379.5", "amountStr": "2851"},
                            {"priceStr": "9381", "amountStr": "106444"},
                            {"priceStr": "9380.5", "amountStr": "6266"},
                        ]
                    },
                    "asks": {
                        "set": [
                            {"priceStr": "9397", "amountStr": "115"},
                            {"priceStr": "9411.5", "amountStr": "3735"},
                        ]
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "2",
                    "currencyPairId": "103",
                    "marketId": "67",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 7285379,
                    "bids": {
                        "set": [
                            {"priceStr": "7056.93", "amountStr": "1.05572315"},
                            {"priceStr": "7056.92", "amountStr": "0.43295743"},
                        ],
                        "removeStr": ["7056.91"],
                    },
                    "asks": {
                        "set": [{"priceStr": "7066.82", "amountStr": "0.11194638"}],
                        "removeStr": ["7074.86"],
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "27",
                    "currencyPairId": "1556",
                    "marketId": "6630",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 806380,
                    "bids": {
                        "set": [
                            {"priceStr": "9161.28", "amountStr": "1"},
                            {"priceStr": "9172.88", "amountStr": "0.01422"},
                            {"priceStr": "9169.12", "amountStr": "0.697717"},
                        ],
                        "removeStr": ["9156.02", "9158.78", "9177.1"],
                    },
                    "asks": {
                        "set": [
                            {"priceStr": "9186.66", "amountStr": "0.469194"},
                            {"priceStr": "9182.79", "amountStr": "0.005446"},
                            {"priceStr": "9184.5", "amountStr": "2"},
                            {"priceStr": "9186.65", "amountStr": "0.102588"},
                            {"priceStr": "9181.7", "amountStr": "1"},
                        ],
                        "removeStr": ["9183.61", "9194.73", "9183.57", "9180.85"],
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "21",
                    "currencyPairId": "231",
                    "marketId": "282",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 6520899,
                    "bids": {
                        "set": [{"priceStr": "9192.82740747", "amountStr": "0.04"}]
                    },
                    "asks": {
                        "set": [
                            {"priceStr": "9204.25385595", "amountStr": "0.18394547"}
                        ]
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "63",
                    "currencyPairId": "1721",
                    "marketId": "28361",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 496046,
                    "bids": {},
                    "asks": {
                        "set": [
                            {"priceStr": "9317.57", "amountStr": "0.758"},
                            {"priceStr": "9322.16", "amountStr": "0.016"},
                        ],
                        "removeStr": ["9314.6", "9310.01"],
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "27",
                    "currencyPairId": "5086",
                    "marketId": "61239",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 819165,
                    "bids": {
                        "set": [
                            {"priceStr": "9175.9", "amountStr": "0.027244"},
                            {"priceStr": "9176.08", "amountStr": "0.001145"},
                            {"priceStr": "9176.09", "amountStr": "0.026094"},
                        ],
                        "removeStr": ["9176.07", "9168.56", "9170.57", "9173.5"],
                    },
                    "asks": {
                        "set": [
                            {"priceStr": "9179.32", "amountStr": "0.009145"},
                            {"priceStr": "9180.89", "amountStr": "0.406975"},
                            {"priceStr": "9179.33", "amountStr": "0.035234"},
                            {"priceStr": "9183.83", "amountStr": "0.12"},
                        ],
                        "removeStr": [
                            "9185.86",
                            "9179.5",
                            "9180.9",
                            "9183.84",
                            "9179.43",
                        ],
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "orderBookDeltaUpdate": {
                    "seqNum": 7077469,
                    "bids": {
                        "set": [
                            {"priceStr": "9202.1", "amountStr": "24.0127859"},
                            {"priceStr": "9172.9", "amountStr": "0.05"},
                        ],
                        "removeStr": ["9201.8"],
                    },
                    "asks": {
                        "set": [
                            {"priceStr": "9221.8", "amountStr": "0.84536225"},
                            {"priceStr": "9227", "amountStr": "1.29"},
                            {"priceStr": "9211.9", "amountStr": "0.04700273"},
                        ],
                        "removeStr": ["9219.8"],
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 5933534,
                    "bids": {
                        "set": [{"priceStr": "8282.5", "amountStr": "1.48419067"}]
                    },
                    "asks": {
                        "set": [
                            {"priceStr": "8321.5", "amountStr": "2.79"},
                            {"priceStr": "8317.5", "amountStr": "4"},
                        ]
                    },
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "27",
                    "currencyPairId": "231",
                    "marketId": "579",
                },
                "orderBookDeltaUpdate": {
                    "seqNum": 858512,
                    "bids": {
                        "set": [
                            {"priceStr": "9197.4", "amountStr": "6.5"},
                            {"priceStr": "9197.16", "amountStr": "5.2"},
                            {"priceStr": "9191.61", "amountStr": "0.155403"},
                            {"priceStr": "9192.33", "amountStr": "0.06"},
                            {"priceStr": "9190.9", "amountStr": "0.453726"},
                            {"priceStr": "9197.33", "amountStr": "0.51854"},
                            {"priceStr": "9194", "amountStr": "0.1"},
                            {"priceStr": "9197.18", "amountStr": "0.6"},
                            {"priceStr": "9197.26", "amountStr": "0.753498"},
                            {"priceStr": "9197.48", "amountStr": "2"},
                            {"priceStr": "9197.44", "amountStr": "2"},
                            {"priceStr": "9197.49", "amountStr": "1.3"},
                            {"priceStr": "9197.21", "amountStr": "0.016306"},
                            {"priceStr": "9183.39", "amountStr": "1.078016"},
                            {"priceStr": "9197.19", "amountStr": "0.9"},
                            {"priceStr": "9197.5", "amountStr": "0.135924"},
                            {"priceStr": "9197.45", "amountStr": "1"},
                            {"priceStr": "9197.29", "amountStr": "0.4"},
                            {"priceStr": "9195.46", "amountStr": "0.065634"},
                            {"priceStr": "9189.73", "amountStr": "0.081612"},
                            {"priceStr": "9180.01", "amountStr": "0.217865"},
                        ],
                        "removeStr": [
                            "9176.39",
                            "9189.98",
                            "9190.96",
                            "9192.3",
                            "9193.92",
                            "9192.24",
                            "9196.84",
                            "9192.32",
                            "9190.24",
                            "9193.91",
                            "9197.13",
                            "9191.68",
                            "9197.12",
                            "9193.93",
                            "9197.11",
                            "9197.14",
                            "9187.79",
                            "9196.43",
                            "9190.22",
                            "9190.97",
                        ],
                    },
                    "asks": {
                        "set": [
                            {"priceStr": "9700", "amountStr": "63.107053"},
                            {"priceStr": "9204.46", "amountStr": "0.189693"},
                            {"priceStr": "11760", "amountStr": "0.060432"},
                            {"priceStr": "9209.95", "amountStr": "0.170137"},
                            {"priceStr": "9216.32", "amountStr": "0.24"},
                            {"priceStr": "9208.16", "amountStr": "4.376738"},
                            {"priceStr": "30500", "amountStr": "0.001605"},
                            {"priceStr": "9205", "amountStr": "0.002723"},
                            {"priceStr": "9199.82", "amountStr": "0.151916"},
                            {"priceStr": "9208.02", "amountStr": "0.113424"},
                            {"priceStr": "11710", "amountStr": "0.025174"},
                            {"priceStr": "11810", "amountStr": "0.010277"},
                            {"priceStr": "9201.47", "amountStr": "0.06"},
                            {"priceStr": "9207.02", "amountStr": "1.25"},
                            {"priceStr": "9201.49", "amountStr": "0.252"},
                            {"priceStr": "9204.19", "amountStr": "0.008"},
                            {"priceStr": "9198.87", "amountStr": "0.152629"},
                            {"priceStr": "9666.81", "amountStr": "0.00997"},
                        ],
                        "removeStr": [
                            "9198.06",
                            "9213.7",
                            "9204.22",
                            "9198.27",
                            "9206.92",
                            "9198.89",
                            "9205.59",
                            "9208.95",
                            "9207.6",
                            "9198.26",
                            "9202.52",
                            "9198.53",
                            "9213.91",
                            "9224.1",
                        ],
                    },
                },
            }
        },
    ]
    for delta in delta_samples:
        schema = OrderbookDeltaMarketUpdateSchema()
        delta_obj = schema.load(delta)
        assert hasattr(delta_obj, "exchange_id")
        assert hasattr(delta_obj, "currency_pair_id")
        assert hasattr(delta_obj, "market_id")
        assert hasattr(delta_obj, "book")
        assert hasattr(delta_obj.book, "seq_num")
        assert hasattr(delta_obj.book, "bids")
        assert hasattr(delta_obj.book.bids, "set")
        assert hasattr(delta_obj.book.bids, "remove")
        for x in delta_obj.book.bids.set:
            assert hasattr(x, "price")
            assert type(x.price) == decimal.Decimal
            assert hasattr(x, "amount")
            assert type(x.amount) == decimal.Decimal
        assert hasattr(delta_obj.book, "asks")
        assert hasattr(delta_obj.book.asks, "set")
        assert hasattr(delta_obj.book.asks, "remove")
        for x in delta_obj.book.asks.set:
            assert hasattr(x, "price")
            assert type(x.price) == decimal.Decimal
            assert hasattr(x, "amount")
            assert type(x.amount) == decimal.Decimal


def test_orderbook_snapshot_object_serialization():
    snapshot_sample = {
        "marketUpdate": {
            "market": {"exchangeId": "25", "currencyPairId": "231", "marketId": "390"},
            "orderBookUpdate": {
                "seqNum": 2147260,
                "bids": [
                    {"priceStr": "9185.22175946", "amountStr": "0.3"},
                    {"priceStr": "9185.22175944", "amountStr": "0.47231439"},
                    {"priceStr": "9185.12175941", "amountStr": "0.59113565"},
                    {"priceStr": "9184.1625296", "amountStr": "0.06683305"},
                    {"priceStr": "9184.00036206", "amountStr": "0.58883"},
                    {"priceStr": "9183.17633724", "amountStr": "0.00074465"},
                    {"priceStr": "9181.82240463", "amountStr": "0.775446"},
                    {"priceStr": "9181.82240462", "amountStr": "0.245"},
                    {"priceStr": "9177.80000009", "amountStr": "0.121"},
                    {"priceStr": "9177.80000008", "amountStr": "0.19935291"},
                    {"priceStr": "9177.80000006", "amountStr": "0.10883055"},
                    {"priceStr": "9177.8", "amountStr": "2"},
                    {"priceStr": "9175.29300304", "amountStr": "0.0425"},
                    {"priceStr": "9175.29299528", "amountStr": "0.3659"},
                    {"priceStr": "9175.29299211", "amountStr": "0.2"},
                    {"priceStr": "9173.36246769", "amountStr": "0.1"},
                    {"priceStr": "9172.96", "amountStr": "0.073"},
                    {"priceStr": "9168.89877611", "amountStr": "1.1883"},
                    {"priceStr": "9168.8987761", "amountStr": "0.26"},
                    {"priceStr": "9162.79", "amountStr": "0.005456"},
                    {"priceStr": "9162", "amountStr": "0.5"},
                    {"priceStr": "9161.91", "amountStr": "0.005457"},
                    {"priceStr": "9161.21264046", "amountStr": "0.26"},
                    {"priceStr": "9160.82", "amountStr": "0.005458"},
                    {"priceStr": "9160", "amountStr": "0.0055"},
                    {"priceStr": "9159.66793885", "amountStr": "0.00107602"},
                    {"priceStr": "9158.55", "amountStr": "0.005459"},
                    {"priceStr": "9157.8", "amountStr": "0.005459"},
                    {"priceStr": "9157.20000001", "amountStr": "0.99999998"},
                    {"priceStr": "9157.2", "amountStr": "0.50546"},
                    {"priceStr": "9157.18165881", "amountStr": "0.00042515"},
                    {"priceStr": "9155", "amountStr": "0.055461"},
                    {"priceStr": "9154.87588201", "amountStr": "0.001"},
                    {"priceStr": "9154.87", "amountStr": "0.005461"},
                    {"priceStr": "9153.99344374", "amountStr": "0.00226524"},
                    {"priceStr": "9153", "amountStr": "0.5"},
                    {"priceStr": "9151.1", "amountStr": "0.07564563"},
                    {"priceStr": "9151", "amountStr": "0.0044"},
                    {"priceStr": "9150.79304603", "amountStr": "0.014413"},
                    {"priceStr": "9150.42", "amountStr": "0.001962"},
                    {"priceStr": "9150", "amountStr": "9.88398891"},
                    {"priceStr": "9147.2417971", "amountStr": "0.00044314"},
                    {"priceStr": "9146.27628022", "amountStr": "0.06811656"},
                    {"priceStr": "9143.92584126", "amountStr": "0.0036691"},
                    {"priceStr": "9143.20800788", "amountStr": "12.2289"},
                    {"priceStr": "9143.09116403", "amountStr": "0.00054686"},
                    {"priceStr": "9142.32403879", "amountStr": "0.00218762"},
                    {"priceStr": "9141", "amountStr": "0.01"},
                    {"priceStr": "9140", "amountStr": "0.00628644"},
                    {"priceStr": "9139.81", "amountStr": "1"},
                    {"priceStr": "9139.58926003", "amountStr": "0.03314521"},
                    {"priceStr": "9138.96022133", "amountStr": "0.00386593"},
                    {"priceStr": "9138.58", "amountStr": "0.000789"},
                    {"priceStr": "9138.38995966", "amountStr": "0.00712187"},
                    {"priceStr": "9136.15", "amountStr": "0.07211961"},
                    {"priceStr": "9136.08", "amountStr": "0.00678628"},
                    {"priceStr": "9130", "amountStr": "0.02825466"},
                    {"priceStr": "9129.81", "amountStr": "1"},
                    {"priceStr": "9128.78131021", "amountStr": "0.0004"},
                    {"priceStr": "9128", "amountStr": "0.5"},
                    {"priceStr": "9126.40178274", "amountStr": "0.0027265"},
                    {"priceStr": "9123.52412332", "amountStr": "0.00045812"},
                    {"priceStr": "9122", "amountStr": "0.01"},
                    {"priceStr": "9120", "amountStr": "0.01707165"},
                    {"priceStr": "9119", "amountStr": "0.04"},
                    {"priceStr": "9118.47947906", "amountStr": "0.02741685"},
                    {"priceStr": "9118.47947826", "amountStr": "0.00548337"},
                    {"priceStr": "9118.47947608", "amountStr": "0.00329002"},
                    {"priceStr": "9116.7758", "amountStr": "0.0015"},
                    {"priceStr": "9115.81693818", "amountStr": "0.04984748"},
                    {"priceStr": "9115.66366555", "amountStr": "0.00108535"},
                    {"priceStr": "9114.17200919", "amountStr": "0.00201215"},
                    {"priceStr": "9114", "amountStr": "0.01795296"},
                    {"priceStr": "9112.48", "amountStr": "0.01"},
                    {"priceStr": "9112.05037393", "amountStr": "0.00134675"},
                    {"priceStr": "9111.885", "amountStr": "0.01088139"},
                    {"priceStr": "9110", "amountStr": "0.0350826"},
                    {"priceStr": "9109", "amountStr": "0.010143"},
                    {"priceStr": "9108", "amountStr": "0.01"},
                    {"priceStr": "9106.04481984", "amountStr": "0.00387118"},
                    {"priceStr": "9103", "amountStr": "0.003"},
                    {"priceStr": "9102.70364896", "amountStr": "0.00241686"},
                    {"priceStr": "9102.59", "amountStr": "0.00054"},
                    {"priceStr": "9102.0320364", "amountStr": "0.03"},
                    {"priceStr": "9101.56928784", "amountStr": "0.00328073"},
                    {"priceStr": "9101.34927246", "amountStr": "0.01643997"},
                    {"priceStr": "9100", "amountStr": "10.13347437"},
                    {"priceStr": "9098.96479491", "amountStr": "0.0004732"},
                    {"priceStr": "9095.84818783", "amountStr": "0.07493537"},
                    {"priceStr": "9095", "amountStr": "0.13733702"},
                    {"priceStr": "9094.77609935", "amountStr": "0.00026138"},
                    {"priceStr": "9094.23", "amountStr": "0.026607"},
                    {"priceStr": "9094.00903673", "amountStr": "0.00121402"},
                    {"priceStr": "9091", "amountStr": "0.13508978"},
                    {"priceStr": "9090", "amountStr": "0.11229153"},
                    {"priceStr": "9086.68523661", "amountStr": "0.00220102"},
                    {"priceStr": "9084.77609935", "amountStr": "0.00026138"},
                    {"priceStr": "9081.45693299", "amountStr": "0.39953527"},
                    {"priceStr": "9080", "amountStr": "0.86199376"},
                    {"priceStr": "9079.94895671", "amountStr": "0.11711751"},
                    {"priceStr": "9079.22004243", "amountStr": "0.00394657"},
                    {"priceStr": "7800", "amountStr": "3.99628938"},
                    {"priceStr": "7797.73066823", "amountStr": "0.00155266"},
                    {"priceStr": "7790", "amountStr": "0.0683762"},
                ],
                "asks": [
                    {"priceStr": "9193.82310317", "amountStr": "0.889453"},
                    {"priceStr": "9193.82310318", "amountStr": "0.12768561"},
                    {"priceStr": "9193.8231032", "amountStr": "0.08488"},
                    {"priceStr": "9194.42310336", "amountStr": "0.01470314"},
                    {"priceStr": "9194.54", "amountStr": "0.077"},
                    {"priceStr": "9194.98462646", "amountStr": "0.08048"},
                    {"priceStr": "9195.18462646", "amountStr": "0.26683305"},
                    {"priceStr": "9195.59164348", "amountStr": "0.16689074"},
                    {"priceStr": "9195.59164349", "amountStr": "0.245"},
                    {"priceStr": "9198", "amountStr": "0.03424724"},
                    {"priceStr": "9201.41963745", "amountStr": "1.04010226"},
                    {"priceStr": "9201.41964276", "amountStr": "0.2"},
                    {"priceStr": "9203.07961883", "amountStr": "0.3658"},
                    {"priceStr": "9203.07961884", "amountStr": "0.1"},
                    {"priceStr": "9203.24466193", "amountStr": "0.1"},
                    {"priceStr": "9203.53151607", "amountStr": "0.9751017"},
                    {"priceStr": "9209.4", "amountStr": "2"},
                    {"priceStr": "9209.53826291", "amountStr": "1.1882"},
                    {"priceStr": "9209.53826292", "amountStr": "0.26"},
                    {"priceStr": "9209.84559752", "amountStr": "0.26"},
                    {"priceStr": "9214.17925438", "amountStr": "1"},
                    {"priceStr": "9223.86928569", "amountStr": "0.10883893"},
                    {"priceStr": "9223.8692857", "amountStr": "5.76212469"},
                    {"priceStr": "9233.26700623", "amountStr": "0.21716695"},
                    {"priceStr": "9233.84", "amountStr": "0.011"},
                    {"priceStr": "9236.49426294", "amountStr": "12.2289"},
                    {"priceStr": "9246.03511979", "amountStr": "0.00286124"},
                    {"priceStr": "9247.43396216", "amountStr": "0.00218931"},
                    {"priceStr": "9248.9171163", "amountStr": "0.01081207"},
                    {"priceStr": "9265.71938177", "amountStr": "0.01088676"},
                    {"priceStr": "9268.70588235", "amountStr": "0.00026"},
                    {"priceStr": "9268.87795003", "amountStr": "0.00519948"},
                    {"priceStr": "9270", "amountStr": "0.16197403"},
                    {"priceStr": "9271.19400002", "amountStr": "6.2497"},
                    {"priceStr": "9273.53808198", "amountStr": "0.03"},
                    {"priceStr": "9275.52975922", "amountStr": "0.12561749"},
                    {"priceStr": "9277.45", "amountStr": "0.00054"},
                    {"priceStr": "9282.89758804", "amountStr": "0.0043884"},
                    {"priceStr": "9287.62387203", "amountStr": "0.0004"},
                    {"priceStr": "9289.4117647", "amountStr": "0.00026"},
                    {"priceStr": "9293.37", "amountStr": "0.00539517"},
                    {"priceStr": "9298.12059549", "amountStr": "0.00139705"},
                    {"priceStr": "9310.11764704", "amountStr": "0.2258131"},
                    {"priceStr": "9310.11764705", "amountStr": "0.00026"},
                    {"priceStr": "9315.63093954", "amountStr": "0.0056116"},
                    {"priceStr": "9322", "amountStr": "0.1"},
                    {"priceStr": "9330.82352941", "amountStr": "0.00026"},
                    {"priceStr": "9340.4905531", "amountStr": "0.01070607"},
                    {"priceStr": "9344.23", "amountStr": "0.00537146"},
                    {"priceStr": "9346.17365994", "amountStr": "0.09953402"},
                    {"priceStr": "9350.49", "amountStr": "0.0054165"},
                    {"priceStr": "9351.52941176", "amountStr": "0.00026"},
                    {"priceStr": "9358.99999988", "amountStr": "5"},
                    {"priceStr": "9361.1132975", "amountStr": "0.00688664"},
                    {"priceStr": "9367.23186817", "amountStr": "0.13845937"},
                    {"priceStr": "9372.23529411", "amountStr": "0.00026"},
                    {"priceStr": "9374", "amountStr": "0.1"},
                    {"priceStr": "9378.4287821", "amountStr": "0.00106627"},
                    {"priceStr": "9384.33296383", "amountStr": "0.14322286"},
                    {"priceStr": "9387.2561613", "amountStr": "3.6843"},
                    {"priceStr": "9388.99999988", "amountStr": "5"},
                    {"priceStr": "9392.94117647", "amountStr": "0.00026"},
                    {"priceStr": "9393.68093", "amountStr": "0.00288498"},
                    {"priceStr": "9394.8851", "amountStr": "0.00041502"},
                    {"priceStr": "9396.95904764", "amountStr": "0.21266406"},
                    {"priceStr": "9397.95078", "amountStr": "0.00216275"},
                    {"priceStr": "9398", "amountStr": "0.00893114"},
                    {"priceStr": "9399.5", "amountStr": "0.00095395"},
                    {"priceStr": "9402.22063", "amountStr": "0.00172941"},
                    {"priceStr": "9406.49049", "amountStr": "0.00144052"},
                    {"priceStr": "9408.5590317", "amountStr": "0.02740185"},
                    {"priceStr": "9408.59331543", "amountStr": "0.00124258"},
                    {"priceStr": "9410.76034", "amountStr": "0.00231359"},
                    {"priceStr": "9413.64705882", "amountStr": "0.00026"},
                    {"priceStr": "9419.30005", "amountStr": "0.00182179"},
                    {"priceStr": "9420", "amountStr": "0.00099876"},
                    {"priceStr": "9420.28336369", "amountStr": "0.00032011"},
                    {"priceStr": "9421.1990346", "amountStr": "0.01156636"},
                    {"priceStr": "9423.1423", "amountStr": "0.003"},
                    {"priceStr": "9427.83976", "amountStr": "0.00150227"},
                    {"priceStr": "9428.9714003", "amountStr": "0.06362851"},
                    {"priceStr": "9432.0639899", "amountStr": "0.01060213"},
                    {"priceStr": "9434.35294117", "amountStr": "0.00026"},
                    {"priceStr": "9434.85742012", "amountStr": "0.00029454"},
                    {"priceStr": "9435.74229186", "amountStr": "0.007"},
                    {"priceStr": "9436.37947", "amountStr": "0.00127788"},
                    {"priceStr": "9436.6480562", "amountStr": "0.00987807"},
                    {"priceStr": "9438.59783", "amountStr": "0.0557389"},
                    {"priceStr": "9439.46896", "amountStr": "0.02268942"},
                    {"priceStr": "9440", "amountStr": "0.02646892"},
                    {"priceStr": "9440.9166", "amountStr": "0.00622011"},
                    {"priceStr": "9441.08167", "amountStr": "0.04179318"},
                    {"priceStr": "9443.56551", "amountStr": "0.03342575"},
                    {"priceStr": "9444.21112", "amountStr": "0.00354254"},
                    {"priceStr": "9444.93267075", "amountStr": "0.00029454"},
                    {"priceStr": "9446.04935", "amountStr": "0.02784746"},
                    {"priceStr": "9446.21143", "amountStr": "0.01700492"},
                    {"priceStr": "9447.66011", "amountStr": "0.00466176"},
                    {"priceStr": "11041", "amountStr": "0.00944644"},
                    {"priceStr": "11045.45279", "amountStr": "0.0132"},
                    {"priceStr": "11049.48959399", "amountStr": "0.00690982"},
                    {"priceStr": "11050", "amountStr": "0.007"},
                ],
            },
        }
    }
    schema = OrderbookSnapshotMarketUpdateSchema()
    snapshot_obj = schema.load(snapshot_sample)
    assert hasattr(snapshot_obj, "exchange_id")
    assert hasattr(snapshot_obj, "currency_pair_id")
    assert hasattr(snapshot_obj, "market_id")
    assert hasattr(snapshot_obj, "book")
    assert hasattr(snapshot_obj.book, "seq_num")
    assert hasattr(snapshot_obj.book, "bids")
    assert type(snapshot_obj.book.bids) == type(list())
    for bid in snapshot_obj.book.bids:
        assert hasattr(bid, "price")
        assert type(bid.price) == decimal.Decimal
        assert hasattr(bid, "amount")
        assert type(bid.amount) == decimal.Decimal
    assert hasattr(snapshot_obj.book, "asks")
    assert type(snapshot_obj.book.asks) == type(list())
    for ask in snapshot_obj.book.asks:
        assert hasattr(ask, "price")
        assert type(ask.price) == decimal.Decimal
        assert hasattr(ask, "amount")
        assert type(ask.amount) == decimal.Decimal


def test_orderbook_spread_object_serialization():
    spread_samples = [
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810993130",
                    "bid": {"priceStr": "8302.8", "amountStr": "0.01"},
                    "ask": {"priceStr": "8304.5", "amountStr": "0.295"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810993227",
                    "bid": {"priceStr": "8302.8", "amountStr": "0.01"},
                    "ask": {"priceStr": "8304.4", "amountStr": "0.1"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810993622",
                    "bid": {"priceStr": "8302.9", "amountStr": "2"},
                    "ask": {"priceStr": "8304.3", "amountStr": "1.99"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810993722",
                    "bid": {"priceStr": "8302.9", "amountStr": "2"},
                    "ask": {"priceStr": "8304.2", "amountStr": "0.19"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810994221",
                    "bid": {"priceStr": "8302.8", "amountStr": "0.01"},
                    "ask": {"priceStr": "8304.2", "amountStr": "0.19"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810994822",
                    "bid": {"priceStr": "8302.8", "amountStr": "0.01"},
                    "ask": {"priceStr": "8304.6", "amountStr": "0.28"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810995321",
                    "bid": {"priceStr": "8302.9", "amountStr": "2"},
                    "ask": {"priceStr": "8304.7", "amountStr": "0.01667114"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810996259",
                    "bid": {"priceStr": "9189", "amountStr": "1.22197064"},
                    "ask": {"priceStr": "9189.1", "amountStr": "0.92300686"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810996500",
                    "bid": {"priceStr": "9189", "amountStr": "1.43026972"},
                    "ask": {"priceStr": "9189.1", "amountStr": "0.92300686"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810996900",
                    "bid": {"priceStr": "9189", "amountStr": "1.43026972"},
                    "ask": {"priceStr": "9189.1", "amountStr": "0.92218209"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810997501",
                    "bid": {"priceStr": "9189", "amountStr": "1.13026972"},
                    "ask": {"priceStr": "9189.1", "amountStr": "0.92218209"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810997726",
                    "bid": {"priceStr": "8302.8", "amountStr": "0.01"},
                    "ask": {"priceStr": "8304.7", "amountStr": "0.01667114"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810997822",
                    "bid": {"priceStr": "8302.8", "amountStr": "0.11"},
                    "ask": {"priceStr": "8304.7", "amountStr": "0.01667114"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810998698",
                    "bid": {"priceStr": "9189", "amountStr": "1.12562559"},
                    "ask": {"priceStr": "9189.1", "amountStr": "0.92218209"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810998725",
                    "bid": {"priceStr": "8302.8", "amountStr": "0.01"},
                    "ask": {"priceStr": "8304.7", "amountStr": "0.01667114"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810999198",
                    "bid": {"priceStr": "9189", "amountStr": "0.82562559"},
                    "ask": {"priceStr": "9189.1", "amountStr": "10.92218209"},
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "orderBookSpreadUpdate": {
                    "timestamp": "1580810999502",
                    "bid": {"priceStr": "9189", "amountStr": "0.82562559"},
                    "ask": {"priceStr": "9189.1", "amountStr": "11.12218209"},
                },
            }
        },
    ]
    for spread in spread_samples:
        schema = OrderbookSpreadMarketUpdateSchema()
        spread_obj = schema.load(spread)
        assert hasattr(spread_obj, "exchange_id")
        assert hasattr(spread_obj, "currency_pair_id")
        assert hasattr(spread_obj, "market_id")
        assert hasattr(spread_obj, "spread")
        assert hasattr(spread_obj.spread, "timestamp")
        assert hasattr(spread_obj.spread, "bid")
        assert hasattr(spread_obj.spread.bid, "price")
        assert type(spread_obj.spread.bid.price) == decimal.Decimal
        assert hasattr(spread_obj.spread.bid, "amount")
        assert type(spread_obj.spread.bid.amount) == decimal.Decimal
        assert hasattr(spread_obj.spread, "ask")
        assert hasattr(spread_obj.spread.ask, "price")
        assert type(spread_obj.spread.ask.price) == decimal.Decimal
        assert hasattr(spread_obj.spread.ask, "amount")
        assert type(spread_obj.spread.ask.amount) == decimal.Decimal


def test_candles_object_serialization():
    ohlc_samples = [
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "intervalsUpdate": {
                    "intervals": [
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "9279.71091052",
                                "highStr": "9292.70812492",
                                "lowStr": "9272",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "32.11921013",
                            "volumeQuoteStr": "298159.368656038592933",
                            "periodName": "1800",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "9283",
                                "highStr": "9319.2935979",
                                "lowStr": "9252.1",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "318.90191267",
                            "volumeQuoteStr": "2963077.0232921426612511",
                            "periodName": "21600",
                        },
                        {
                            "closetime": "1581292800",
                            "ohlc": {
                                "openStr": "9271.618922",
                                "highStr": "9319.2935979",
                                "lowStr": "9244.9",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "486.17026599",
                            "volumeQuoteStr": "4510845.5973263880307325",
                            "periodName": "604800_Monday",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "9292",
                                "highStr": "9292.70812492",
                                "lowStr": "9272",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "18.1844151",
                            "volumeQuoteStr": "168788.4061804364735871",
                            "periodName": "900",
                        },
                        {
                            "closetime": "1580806800",
                            "ohlc": {
                                "openStr": "9279.71091052",
                                "highStr": "9292.70812492",
                                "lowStr": "9272",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "32.11921013",
                            "volumeQuoteStr": "298159.368656038592933",
                            "periodName": "3600",
                        },
                        {
                            "closetime": "1580860800",
                            "ohlc": {
                                "openStr": "9271.618922",
                                "highStr": "9319.2935979",
                                "lowStr": "9244.9",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "486.17026599",
                            "volumeQuoteStr": "4510845.5973263880307325",
                            "periodName": "86400",
                        },
                        {
                            "closetime": "1580804940",
                            "ohlc": {
                                "openStr": "9272",
                                "highStr": "9272",
                                "lowStr": "9272",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "1.01047814",
                            "volumeQuoteStr": "9369.15331408",
                            "periodName": "60",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "9280.34407383",
                                "highStr": "9280.34407383",
                                "lowStr": "9272",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "11.88591742",
                            "volumeQuoteStr": "110280.7075737668263442",
                            "periodName": "300",
                        },
                        {
                            "closetime": "1580810400",
                            "ohlc": {
                                "openStr": "9279.71091052",
                                "highStr": "9292.70812492",
                                "lowStr": "9272",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "32.11921013",
                            "volumeQuoteStr": "298159.368656038592933",
                            "periodName": "7200",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "9279.71091052",
                                "highStr": "9292.70812492",
                                "lowStr": "9272",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "32.11921013",
                            "volumeQuoteStr": "298159.368656038592933",
                            "periodName": "14400",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "9271.618922",
                                "highStr": "9319.2935979",
                                "lowStr": "9244.9",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "486.17026599",
                            "volumeQuoteStr": "4510845.5973263880307325",
                            "periodName": "43200",
                        },
                        {
                            "closetime": "1580860800",
                            "ohlc": {
                                "openStr": "9271.618922",
                                "highStr": "9319.2935979",
                                "lowStr": "9244.9",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "486.17026599",
                            "volumeQuoteStr": "4510845.5973263880307325",
                            "periodName": "259200",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "9272.00482607",
                                "highStr": "9272.00482607",
                                "lowStr": "9272",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "1.0466083",
                            "volumeQuoteStr": "9704.1523319666812712",
                            "periodName": "180",
                        },
                        {
                            "closetime": "1580947200",
                            "ohlc": {
                                "openStr": "9305.2",
                                "highStr": "9550",
                                "lowStr": "9122.8",
                                "closeStr": "9272",
                            },
                            "volumeBaseStr": "14964.09618298",
                            "volumeQuoteStr": "140613596.6534487952860238",
                            "periodName": "604800",
                        },
                    ]
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "intervalsUpdate": {
                    "intervals": [
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "8388.5",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "25.95897185",
                            "volumeQuoteStr": "217806.839515391",
                            "periodName": "1800",
                        },
                        {
                            "closetime": "1580806800",
                            "ohlc": {
                                "openStr": "8388.5",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "25.95897185",
                            "volumeQuoteStr": "217806.839515391",
                            "periodName": "3600",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "8388.5",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "25.95897185",
                            "volumeQuoteStr": "217806.839515391",
                            "periodName": "14400",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "8383.1",
                                "highStr": "8432",
                                "lowStr": "8356.7",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "317.08540679",
                            "volumeQuoteStr": "2660157.977734642",
                            "periodName": "21600",
                        },
                        {
                            "closetime": "1580860800",
                            "ohlc": {
                                "openStr": "8408",
                                "highStr": "8432",
                                "lowStr": "8343",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "419.08385822",
                            "volumeQuoteStr": "3513922.059843848",
                            "periodName": "86400",
                        },
                        {
                            "closetime": "1580804940",
                            "ohlc": {
                                "openStr": "8372.5",
                                "highStr": "8372.5",
                                "lowStr": "8370.7",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "0.88839196",
                            "volumeQuoteStr": "7437.144479572",
                            "periodName": "60",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "8372",
                                "highStr": "8372.6",
                                "lowStr": "8370.1",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "1.67020801",
                            "volumeQuoteStr": "13981.790627173",
                            "periodName": "180",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "8394.9",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "17.08016068",
                            "volumeQuoteStr": "143289.437942495",
                            "periodName": "900",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "8386",
                                "highStr": "8386",
                                "lowStr": "8370.1",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "6.15052915",
                            "volumeQuoteStr": "51533.299631742",
                            "periodName": "300",
                        },
                        {
                            "closetime": "1580810400",
                            "ohlc": {
                                "openStr": "8388.5",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "25.95897185",
                            "volumeQuoteStr": "217806.839515391",
                            "periodName": "7200",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "8408",
                                "highStr": "8432",
                                "lowStr": "8343",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "419.08385822",
                            "volumeQuoteStr": "3513922.059843848",
                            "periodName": "43200",
                        },
                        {
                            "closetime": "1580860800",
                            "ohlc": {
                                "openStr": "8408",
                                "highStr": "8432",
                                "lowStr": "8343",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "419.08385822",
                            "volumeQuoteStr": "3513922.059843848",
                            "periodName": "259200",
                        },
                        {
                            "closetime": "1580947200",
                            "ohlc": {
                                "openStr": "8475",
                                "highStr": "8525",
                                "lowStr": "8343",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "701.65911147",
                            "volumeQuoteStr": "5907045.984871676",
                            "periodName": "604800",
                        },
                        {
                            "closetime": "1581292800",
                            "ohlc": {
                                "openStr": "8408",
                                "highStr": "8432",
                                "lowStr": "8343",
                                "closeStr": "8371.6",
                            },
                            "volumeBaseStr": "419.08385822",
                            "volumeQuoteStr": "3513922.059843848",
                            "periodName": "604800_Monday",
                        },
                    ]
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "intervalsUpdate": {
                    "intervals": [
                        {
                            "closetime": "1580804940",
                            "ohlc": {
                                "openStr": "8372.5",
                                "highStr": "8372.5",
                                "lowStr": "8370.7",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "0.90696254",
                            "volumeQuoteStr": "7592.624803564",
                            "periodName": "60",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "8372",
                                "highStr": "8372.6",
                                "lowStr": "8370.1",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "1.68877859",
                            "volumeQuoteStr": "14137.270951165",
                            "periodName": "180",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "8394.9",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "17.09873126",
                            "volumeQuoteStr": "143444.918266487",
                            "periodName": "900",
                        },
                        {
                            "closetime": "1580860800",
                            "ohlc": {
                                "openStr": "8408",
                                "highStr": "8432",
                                "lowStr": "8343",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "419.1024288",
                            "volumeQuoteStr": "3514077.54016784",
                            "periodName": "259200",
                        },
                        {
                            "closetime": "1580947200",
                            "ohlc": {
                                "openStr": "8475",
                                "highStr": "8525",
                                "lowStr": "8343",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "701.67768205",
                            "volumeQuoteStr": "5907201.465195668",
                            "periodName": "604800",
                        },
                        {
                            "closetime": "1581292800",
                            "ohlc": {
                                "openStr": "8408",
                                "highStr": "8432",
                                "lowStr": "8343",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "419.1024288",
                            "volumeQuoteStr": "3514077.54016784",
                            "periodName": "604800_Monday",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "8386",
                                "highStr": "8386",
                                "lowStr": "8370.1",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "6.16909973",
                            "volumeQuoteStr": "51688.779955734",
                            "periodName": "300",
                        },
                        {
                            "closetime": "1580810400",
                            "ohlc": {
                                "openStr": "8388.5",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "25.97754243",
                            "volumeQuoteStr": "217962.319839383",
                            "periodName": "7200",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "8408",
                                "highStr": "8432",
                                "lowStr": "8343",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "419.1024288",
                            "volumeQuoteStr": "3514077.54016784",
                            "periodName": "43200",
                        },
                        {
                            "closetime": "1580805000",
                            "ohlc": {
                                "openStr": "8388.5",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "25.97754243",
                            "volumeQuoteStr": "217962.319839383",
                            "periodName": "1800",
                        },
                        {
                            "closetime": "1580860800",
                            "ohlc": {
                                "openStr": "8408",
                                "highStr": "8432",
                                "lowStr": "8343",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "419.1024288",
                            "volumeQuoteStr": "3514077.54016784",
                            "periodName": "86400",
                        },
                        {
                            "closetime": "1580806800",
                            "ohlc": {
                                "openStr": "8388.5",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "25.97754243",
                            "volumeQuoteStr": "217962.319839383",
                            "periodName": "3600",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "8388.5",
                                "highStr": "8400.4",
                                "lowStr": "8370.1",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "25.97754243",
                            "volumeQuoteStr": "217962.319839383",
                            "periodName": "14400",
                        },
                        {
                            "closetime": "1580817600",
                            "ohlc": {
                                "openStr": "8383.1",
                                "highStr": "8432",
                                "lowStr": "8356.7",
                                "closeStr": "8372.4",
                            },
                            "volumeBaseStr": "317.10397737",
                            "volumeQuoteStr": "2660313.458058634",
                            "periodName": "21600",
                        },
                    ]
                },
            }
        },
    ]
    for ohlc in ohlc_samples:
        schema = CandleMarketUpdateSchema()
        candle_obj = schema.load(ohlc)
        assert hasattr(candle_obj, "exchange_id")
        assert hasattr(candle_obj, "currency_pair_id")
        assert hasattr(candle_obj, "market_id")
        assert hasattr(candle_obj, "candles")
        assert type(candle_obj.candles) == type(list())
        assert hasattr(candle_obj.candles[0], "close_timestamp")
        assert hasattr(candle_obj.candles[0], "period")
        assert hasattr(candle_obj.candles[0], "open")
        assert type(candle_obj.candles[0].open) == decimal.Decimal
        assert hasattr(candle_obj.candles[0], "high")
        assert type(candle_obj.candles[0].high) == decimal.Decimal
        assert hasattr(candle_obj.candles[0], "low")
        assert type(candle_obj.candles[0].low) == decimal.Decimal
        assert hasattr(candle_obj.candles[0], "close")
        assert type(candle_obj.candles[0].close) == decimal.Decimal
        assert hasattr(candle_obj.candles[0], "volume")
        assert type(candle_obj.candles[0].volume) == decimal.Decimal
        assert hasattr(candle_obj.candles[0], "volume_base")
        assert type(candle_obj.candles[0].volume_base) == decimal.Decimal


def test_trade_object_serialization():
    trade_samples = [
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "tradesUpdate": {
                    "trades": [
                        {
                            "externalId": "413896616",
                            "timestamp": "1580797709",
                            "timestampNano": "1580797709249000000",
                            "priceStr": "9262.12059165",
                            "amountStr": "0.025",
                            "orderSide": "BUYSIDE",
                        }
                    ]
                },
            }
        },
        {
            "marketUpdate": {
                "market": {"exchangeId": "1", "currencyPairId": "9", "marketId": "1"},
                "tradesUpdate": {
                    "trades": [
                        {
                            "externalId": "413896618",
                            "timestamp": "1580797721",
                            "timestampNano": "1580797721479000000",
                            "priceStr": "9261.8199171",
                            "amountStr": "0.01",
                            "orderSide": "BUYSIDE",
                        }
                    ]
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "tradesUpdate": {
                    "trades": [
                        {
                            "externalId": "1580797738987400000",
                            "timestamp": "1580797738",
                            "timestampNano": "1580797738987400000",
                            "priceStr": "8366.3",
                            "amountStr": "0.00497936",
                            "orderSide": "SELLSIDE",
                        }
                    ]
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "tradesUpdate": {
                    "trades": [
                        {
                            "externalId": "1580797739989400000",
                            "timestamp": "1580797739",
                            "timestampNano": "1580797739989400000",
                            "priceStr": "8366.3",
                            "amountStr": "0.00325274",
                            "orderSide": "SELLSIDE",
                        }
                    ]
                },
            }
        },
        {
            "marketUpdate": {
                "market": {
                    "exchangeId": "4",
                    "currencyPairId": "232",
                    "marketId": "86",
                },
                "tradesUpdate": {
                    "trades": [
                        {
                            "externalId": "1580797742499300000",
                            "timestamp": "1580797742",
                            "timestampNano": "1580797742499300000",
                            "priceStr": "8366.3",
                            "amountStr": "0.00497936",
                            "orderSide": "SELLSIDE",
                        },
                        {
                            "externalId": "1580797742499300000",
                            "timestamp": "1580797722",
                            "timestampNano": "1580797722499300000",
                            "priceStr": "1111.3",
                            "amountStr": "4.00497936",
                            "orderSide": "SELLSIDE",
                        },
                    ]
                },
            }
        },
    ]
    for trade in trade_samples:
        schema = TradeMarketUpdateSchema()
        trade_obj = schema.load(trade)
        assert hasattr(trade_obj, "exchange_id")
        assert hasattr(trade_obj, "currency_pair_id")
        assert hasattr(trade_obj, "market_id")
        assert hasattr(trade_obj, "trades")
        assert type(trade_obj.trades) == type(list())
        assert hasattr(trade_obj.trades[0], "timestamp")
        assert hasattr(trade_obj.trades[0], "timestamp_nano")
        assert hasattr(trade_obj.trades[0], "price")
        assert type(trade_obj.trades[0].price) == decimal.Decimal
        assert hasattr(trade_obj.trades[0], "amount")
        assert type(trade_obj.trades[0].amount) == decimal.Decimal
        assert hasattr(trade_obj.trades[0], "order_side")
