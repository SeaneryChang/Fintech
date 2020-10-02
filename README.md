# fintech
本程式可以用QTS計算股票交易策略

目前有SMA WMA EMA RSI 四個技術指標

初始資金:1,000,000

世代粒子數:10

世代數:30

旋轉角度:0.002

1.輸入股價list

呼叫QTS(股價的list,技術指標)  QTS.py的函式 

回傳交易策略buy1 buy2 sell1 sell2 和 持有股票區間

2.輸入策略

呼叫(股價list,交易策略,技術指標) QTS.py函式

回傳持有區間
