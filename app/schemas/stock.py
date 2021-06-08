from marshmallow import Schema, fields


class StockAllSchema(Schema):
    # class Meta:
    #     load_only = ('password',)
    #     dump_only = ('id',)
    date = fields.Date()
    open = fields.Float()
    adjClose = fields.Float()
    volume = fields.Int()
    high = fields.Float()
    low = fields.Float()
    count = fields.Int()
    value = fields.Int()
    close = fields.Float()
    individual_buy_count = fields.Int()
    individual_sell_count = fields.Int()
    individual_buy_vol = fields.Int()
    individual_sell_vol = fields.Int()
    individual_buy_value = fields.Int()
    individual_sell_value = fields.Int()
    corporate_buy_count = fields.Int()
    corporate_sell_count = fields.Int()
    corporate_buy_vol = fields.Int()
    corporate_sell_vol = fields.Int()
    corporate_buy_value = fields.Int()
    corporate_sell_value = fields.Int()
    individual_buy_mean_price = fields.Float()
    individual_sell_mean_price = fields.Float()
    corporate_buy_mean_price = fields.Float()
    corporate_sell_mean_price = fields.Float()
    individual_ownership_change = fields.Int()


class StockChartSchema(Schema):
    # class Meta:
    #     load_only = ('password',)
    #     dump_only = ('id',)
    date = fields.Date()
    open = fields.Float()
    close = fields.Float()
    high = fields.Float()
    low = fields.Float()
    volume = fields.Int()


class StockGeneralSchema(Schema):
    # class Meta:
    #     load_only = ('password',)
    #     dump_only = ('id',)
    date = fields.Date()
    open = fields.Float()
    adjClose = fields.Float()
    volume = fields.Int()
    high = fields.Float()
    low = fields.Float()
    count = fields.Int()
    value = fields.Int()
    close = fields.Float()


class StockClientsSchema(Schema):
    # class Meta:
    #     load_only = ('password',)
    #     dump_only = ('id',)
    date = fields.Date()
    individual_buy_count = fields.Int()
    individual_sell_count = fields.Int()
    individual_buy_vol = fields.Int()
    individual_sell_vol = fields.Int()
    individual_buy_value = fields.Int()
    individual_sell_value = fields.Int()
    corporate_buy_count = fields.Int()
    corporate_sell_count = fields.Int()
    corporate_buy_vol = fields.Int()
    corporate_sell_vol = fields.Int()
    corporate_buy_value = fields.Int()
    corporate_sell_value = fields.Int()
    individual_buy_mean_price = fields.Float()
    individual_sell_mean_price = fields.Float()
    corporate_buy_mean_price = fields.Float()
    corporate_sell_mean_price = fields.Float()
    individual_ownership_change = fields.Int()
