import csv
import random
stock = []
with open('C:/Users/acus/Desktop/比賽/QTS/AAPL.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        stock.append(row['Close'])


def ma(stock):                                                     #計算訓練期每天的MA(1-256) 回傳二維陣列,stock長度
    l = len(stock)        
    date_ma = [[0]*256 for _ in range(l-255)]
    numer = 0
    denomi = 0
    for i in range(1,l-254):                 #i代表每個訓練天數
        for j in range(1,257):        #j代表訓練天數的MA(1-256)
            for k in range(1,j+1):      #k計算MA[j]
                numer += float(stock[255+i-j])
                denomi += 1
            date_ma[i-1][j-1] = numer/denomi
            numer = 0
            denomi = 0
    return date_ma,l
def fitness(stock,stre):                                           #給策略參數  回傳持有區間,收益
    date_ma,l = ma(stock)
    fund = 1000000                                                #資金
    hold = []
    b = 0
    for d in range(256,l):    #訓練期開始
        if(b == 0):
            tmp = 0
        else:
            tmp = 1
        if(date_ma[d-256][int(stre[0])] <= date_ma[d-256][int(stre[1])] and 
        date_ma[d-255][int(stre[0])] > date_ma[d-255][int(stre[1])] and b == 0):
            remain = float(fund%float(stock[d]))
            shares = int((fund-remain)/float(stock[d]))
            fund -= shares*float(stock[d])
            b = 1
        elif(date_ma[d-256][int(stre[2])] >= date_ma[d-256][int(stre[3])] and 
        date_ma[d-255][int(stre[2])] < date_ma[d-255][int(stre[3])] and b == 1):
            fund += float(stock[d])*shares + remain
            b = 0
        elif(d == l-1 and b == 1):
            fund += float(stock[d])*shares + remain
            b = 0
        if(b == 1):
            hold.append(float(stock[d]))
        else:
            if(tmp == 1):
                hold.append(float(stock[d]))
            else:
                hold.append('NaN')
    return hold,fund
def QTS(stock):                                         #給股價 回傳最佳策略,收益,持有
    date_ma,l = ma(stock)
    fund = 1000000                     #
    beta = [0.5]*32
    theta = 0.002
    partical = 30
    generation = 1000
    pm = [[0]*32 for _ in range(partical)]
    gbest = [0]*32
    gbest_prof = 0
    pworst = [0]*32
    pworst_prof = 2000000

    stre = [0]*4
    best_stre = [0]*4
    hold = []
    b = 0                             #
    stre_sum = 0
    for _ in range(generation):                 #代數
        # print("generation:" + str(g+1))
        for p in range(partical):               #粒子
            # print("partical:" + str(p+1))
            for s in range(32):                 #32bit策略   
                if(random.random() > beta[s]):
                    pm[p][s] = 0
                    if(s%8 == 7):
                        stre[int(s/8)] = stre_sum
                        stre_sum = 0
                else:
                    pm[p][s] = 1
                    stre_sum += pow(2,s%8) 
                    if(s%8 == 7):
                        stre[int(s/8)] = stre_sum
                        stre_sum = 0
            for d in range(256,l):    #訓練期開始
                if(b == 0):
                    tmp = 0
                else:
                    tmp = 1
                if(date_ma[d-256][int(stre[0])] <= date_ma[d-256][int(stre[1])] and 
                date_ma[d-255][int(stre[0])] > date_ma[d-255][int(stre[1])] and b == 0):
                    remain = float(fund%float(stock[d]))
                    shares = int((fund-remain)/float(stock[d]))
                    fund -= shares*float(stock[d])
                    b = 1
                elif(date_ma[d-256][int(stre[2])] >= date_ma[d-256][int(stre[3])] and 
                date_ma[d-255][int(stre[2])] < date_ma[d-255][int(stre[3])] and b == 1):
                    fund += float(stock[d])*shares + remain
                    b = 0
                elif(d == l-1 and b == 1):
                    fund += float(stock[d])*shares + remain
                    b = 0
                if(b == 1):
                    hold.append(float(stock[d]))
                else:
                    if(tmp == 1):
                        hold.append(float(stock[d]))
                    else:
                        hold.append('NaN')
            # hold,fund = fitness(date_ma,stre)
            if(fund > gbest_prof):
                gbest_prof = fund
                best_stre = stre
                best_hold = hold
                gbest = pm[p]
            if(fund < pworst_prof):
                pworst = pm[p]
            hold = []                                  #
            fund = 1000000                               #
        for i in range(32):
            if(gbest[i] == 1 and pworst[i] == 0):
                beta[i] += theta
            elif(gbest[i] == 0 and pworst[i] == 1):
                beta[i] -= theta
        # if(){
        #     jump
        # }        
        pworst = [0]*32
        pworst_prof = 2000000
        
    return best_stre,gbest_prof,best_hold
def re():
    stretagies,prof,hp = QTS(stock)
    rdict = {"Buy_1":stretagies[0],"Buy_2":stretagies[1],"Sell_1":stretagies[2],"Sell2":stretagies[3],
    "profit":prof,"holding period":hp}
    return rdict
d = re()