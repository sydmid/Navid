
def mode1(requested_stock):
    outputlist = []
    for x in requested_stock:
        outputlist.append(
            {'date': str(x.date),
             'open': x.open,
             'high': x.high,
             'low': x.low,
             'value': x.value,
             'volume': x.volume,
             'count': x.count,
             'close': x.close}
        )
    return outputlist


def mode2(requested_stock):
    return [str([record.name,
                record.date,
                record.open,
                record.close,
                record.value]) for record in requested_stock]