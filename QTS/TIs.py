import csv

# def write_csv(date_ma,ID):
#     with open('C:/Users/acus/Desktop/Fintech/stock/AAPL/' + ID + '_sma.csv','w',newline='')as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(date_ma)
def sma(stock):                                                     #計算訓練期每天的MA(1-256) 回傳二維陣列,stock長度
    l = len(stock)        
    date_ma = [[0]*256 for _ in range(l-255)]
    numer = 0
    denomi = 0
    for i in range(1,l-254):                 #i代表每個訓練天數
        for j in range(1,257):        #j代表訓練天數的MA(1-256)
            for k in range(1,j+1):      #k計算MA[j]
                numer += float(stock[255+i-k])
                denomi += 1
            date_ma[i-1][j-1] = numer/denomi
            numer = 0
            denomi = 0
    # write_csv(date_ma,ID)       
    return date_ma,l
def wma(stock):                                                     #計算訓練期每天的MA(1-256) 回傳二維陣列,stock長度
    l = len(stock)        
    date_ma = [[0]*256 for _ in range(l-255)]
    numer = 0
    denomi = 0
    for i in range(1,l-254):                 #i代表每個訓練天數
        for j in range(1,257):        #j代表訓練天數的MA(1-256)
            for k in range(1,j+1):      #k計算MA[j]
                numer += float(stock[255+i-k])*(j-k+1)
                denomi += k
            date_ma[i-1][j-1] = numer/denomi
            numer = 0
            denomi = 0
    return date_ma,l
def ema(stock):                                                     #計算訓練期每天的MA(1-256) 回傳二維陣列,stock長度
    l = len(stock)        
    date_ma = [[0]*256 for _ in range(l-255)]
    numer = 0
    denomi = 0
    for i in range(1,l-254):                 #i代表每個訓練天數
        for j in range(1,257):        #j代表訓練天數的MA(1-256)
            for k in range(1,j+1):      #k計算MA[j]
                numer += float(stock[255+i-k])
                denomi += 1
            date_ma[i-1][j-1] = numer/denomi
            numer = 0
            denomi = 0
    # write_csv(date_ma,ID)       
    return date_ma,l    