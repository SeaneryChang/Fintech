def rsi(stock):
    l = len(stock)        
    date_rsi = [[0]*256 for _ in range(l-255)]
    up = 0
    down = 0
    for i in range(1,l-254):                 #i代表每個訓練天數
        for j in range(1,257):        #j代表訓練天數
            for k in range(j,-1,0):      #k計算
                if(stock[255+i-k]>stock[254+i-k]):    #i = 1 j = 1 k = 1
                    up += stock[255+i-k] - stock[254+i-k]
                elif(stock[255+i-k]<stock[254+i-k]):
                    down += stock[254+i-k] - stock[255+i-k]     
            date_rsi[i-1][j-1] = (up/up+down)/j*100
    return date_rsi,l