#スリザーリンク4*4のmaster
M=4
N=4

#行、列の線の有無を表すリストにすべて１を代入
col=[[1 for i in range(N)] for j in range(M+1)]
row=[[1 for i in range(N+1)] for j in range(M)]

numbers = {}    #中の数字の辞書を定義

for s in range(M):
    for t in range(N):
        numbers[(s,t)] = True

#0~3の数字の座標を入力させる
for n in range(4):

    while True:     
        print(n,'のX座標を入力して下さい。無い場合はQキーを入力して下さい。')
    
        i = input("")
    
        if i == "q":
            break
    
        elif 0 <= int(i) <= M-1:
        
            x = int(i)
        
            print('Y座標を入力して下さい。')
        
            i = int(input())
        
            if 0 <= i <=  N-1:

                y = i

                numbers[(x,y)] = n

                print('(',x,',',y,') = ',n)

            else:
                print('数値が正しくありません。')

        else:
            print('数値が正しくありません。')

keys = list(numbers.keys())     #座標のリスト

values = list(numbers.values())     #数字のリスト

#辺に線が引けるか引けないかを表す辞書
judge_col = {}  
judge_row = {}

#0の周りをFalseにする関数
def judge_zero(tuple):

    s = tuple[0]
    t = tuple[1]

    judge_col[(s,t)] = False
    judge_col[(s,t+1)] = False
    judge_row[(s,t)] = False
    judge_row[(s+1,t)] = False

#すべての0について判定し辺にFalseを代入
for i in range(len(values)):

    if values[i] == 0:
        judge_zero(keys[i])

#線を上下左右に引く関数
def line_up(s,t):
    if s>N-1 or t>M:
        return False
    if (judge_row[(s,t)] == True) and (row[s][t] == 0):
        row[s][t] = 1
        return True
    else:
        return False

def line_right(s,t):
    if s>N or t>M-1:
        return False
    if (judge_col[(s,t)] == True) and (col[s][t] == 0):
        col[s][t] = 1
        return True
    else:
        return False

def line_down(s,t):
    if 1>s or s>N or t>M:
        return False
    if (judge_row[(s-1,t)] == True) and (row[s-1][t] == 0):
        row[s-1][t] = 1
        return True
    else:
        return False

def line_left(s,t):
    if s>N or t>M:
        return False
    if (judge_col[(s,t-1)] == True) and (col[s][t-1] == 0):
        col[s][t-1] = 1
        return True
    else:
        return False

#どこの点にもすすめなくなった時に１つ前の点の座標を返す関数
def line_pre_false(s,t):
    if col[s][t] == 1:
        judge_col[(s,t)] = False
        return (s,t+1)
    elif col[s][t-1] == 1:
        judge_col[(s,t-1)] = False
        return (s,t-1)
    elif row[s][t] == 1:
        judge_row[(s,t)] = False
        return (s+1,t)
    elif row[s-1][t] ==1:
        judge_row[(s-1,t)] = False
        return (s-1,t)
    else:
        print("error")
    
#ある点について線を上、右、下、左の順に引けるか試していく関数
def line_main(x,y):
    if line_up(x,y):
        print(col,row)
        print()
        return (x+1,y)
    if line_right(x,y):
        print(col,row)
        print()
        return (x,y+1)
    if line_down(x,y):
        print(col,row)
        print()
        return (x-1,y)
    if line_left(x,y):
        print(col,row)
        print()
        return (x,y-1)
    else:
        return False
        
    
#再帰定義によって次々に線を引いていく関数
def line_all(x,y):
    tmp = line_main(x,y)
    if allink(N,M):
            return
    if tmp == False:
        (x1,y1) = line_pre_false(x,y)
        line_all(x1,y1)
    else:
        (x2,y2) = tmp
        line_all(x2,y2)


#全部の線がつながっているか確認（再帰関数の終了条件）        
def link(s,t):
    if s<N and t<M:
        c=col[s][t]+col[s][t-1]+row[s][t]+row[s-1][t]
    elif s==N and t!=M:
        c=col[s][t]+col[s][t-1]+row[s-1][t]
    elif s!=N and t==M:
        c=col[s][t-1]+row[s][t]+row[s-1][t]
    else:
        c=col[s][t-1]+row[s-1][t]
    
    if c==0 or c==2:
        return True
    else:
        return False
        
def allink(s,t):
    for i in range(s):
        for j in range(t):
            if link(i,j)==False:
                return False

print(col,row)
print()
line_all(0,0)

def solved(a):
    if a==None:
        print(col)
        print(row)
    else:
        print("unsolved")


solved(allink(N+1,M+1))
