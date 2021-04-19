# TODO day step in modes
def general_data(requested_stock):
    outputlist = []
    for x in requested_stock:
        outputlist.append(
            {'date': str(x.date),
             'open': x.open,
             'high': x.high,
             'low': x.low,
             'adjClose': x.adjClose,
             'value': x.value,
             'volume': x.volume,
             'count': x.count,
             'close': x.close}
        )
    return outputlist

def clients_data(requested_stock):
    outputlist = []
    for x in requested_stock:
        outputlist.append(
            {'individual_buy_count': str(x.individual_buy_count),
             'individual_sell_count': x.individual_sell_count,
             'individual_buy_vol': x.individual_buy_vol,
             'individual_sell_vol': x.individual_sell_vol,
             'individual_buy_value': x.individual_buy_value,
             'individual_sell_value': x.individual_sell_value,
             'corporate_buy_count': str(x.corporate_buy_count),
             'corporate_sell_count': x.corporate_sell_count,
             'corporate_buy_vol': x.corporate_buy_vol,
             'corporate_sell_vol': x.corporate_sell_vol,
             'corporate_buy_value': x.corporate_buy_value,
             'corporate_sell_value': x.corporate_sell_value,
             'individual_buy_mean_price': x.individual_buy_mean_price,
             'individual_sell_mean_price': x.individual_sell_mean_price,
             'corporate_buy_mean_price': x.corporate_buy_mean_price,
             'corporate_sell_mean_price': x.corporate_sell_mean_price,
             'individual_ownership_change': x.individual_ownership_change,
             'jdate': x.jdate}
        )
    return outputlist

def test_data(requested_stock):
    outputlist = []
    for x in requested_stock:
        outputlist.append(
            [str(x.date),
             x.open,
             x.high,
             x.low,
             x.adjClose,
             x.value,
             x.volume,
             x.count,
             x.close]
        )
    return outputlist
