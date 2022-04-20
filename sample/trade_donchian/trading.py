class trading:
    def entry_signal(exchange:string,symbol:string) -> dict:
      '''
      解释：
      PRICE_USD：当前价格(USD)
      MA350D：350日均线
      MA25D：25日均线
      DON20D_BREAK：是否突破唐奇安通道？（0未突破；1向上突破；-1向下突破）
      TOTAL_POS: 当前总仓位(USD)
      MARGIN：可用保证金余额
      RISK: 每ATR波动对应的风险百分比
      ATRP20D: 20日ATR波动百分比
      '''
      e,s = exchange,symbol
      if TOTAL_POS > 0:
        return None
      pos = MARGIN * RISK / ATRP20D(e,s)
      if DON20D_BREAK(e,s) == 1 and MA25D(e,s) > MA350D(e,s):
        strategy = {
        "sign":1.0, #信号强度
        "side":"buy" #方向：做多buy或做空sell
        "pos":pos #头寸大小：（以USD为单位）
        }
      elif DON20D_BREAK(e,s) == -1 and MA25D(e,s) < MA350D(e,s):
        strategy = {
        "sign":1.0, #信号强度
        "side":"sell" #方向：做多buy或做空sell
        "pos":pos #头寸大小：（以USD为单位）
        }
      else:
        return None
      #strategy策略对象
      return strategy
        
    def exit_signal(order:"order") -> tuple:
        '''
        #order订单对象
        order = {
        "exchange":"bitfinex", #交易所
        "symbol":"BTC/USDT", #币种
        "side":"buy", #方向：做多buy或做空sell
        "order_id":"xxxxxxxxxxxxx", #订单编号
        "entry_price":50000.0, #平均成交价格
        "best_price":50010.0, #盈利最大价格
        "stop_price":49010.0, #止损价格(对于动态止损策略，stop_price会根据best_price动态变化)
        "current_price: 50008.0 #当前价格
        "total_amount":"0.1", #数量
        "executed_amount":"0.04", #已执行数量
        "unexecuted_amount":"0.06", #未执行数量
        "status":1, #0未执行;1部分执行;2全部执行
        "timestamp":1650176916.000, #订单创建时间（秒）
        "fees":2.0, #已产生的手续费（美元）
        "ATR": 2500.0, #ATR
        "ATRP": 5.0 #ATR%
        }
        '''
        exit_sign = 0  #退出信号强度（介于[0,1]之间）
        etype = 0 #退出类型：0信号退出 1止损退出
        if order.side == 'buy':
          if order.current_price < order.entry_price - order.ATR * 2:
            exit_sign = 1
            etype = 1
          elif DON10D_BREAK(e,s) == -1:
            exit_sign = 1
            etype = 0
        elif order.side == 'sell':
          if order.current_price > order.entry_price + order.ATR * 2:
            exit_sign = 1
            etype = 1
          elif DON10D_BREAK(e,s) == 1:
            exit_sign = 1
            etype = 0
        return exit_sign, etype
