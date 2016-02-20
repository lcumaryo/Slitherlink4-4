#スリザーリンク4*4のmaster
M=4
N=4

print('Welcome to the SlitherLink ',M,'*',N,'!')

#DEFINITION BEGIN


col=[[1 for i in range(N)] for j in range(M+1)]

row=[[1 for i in range(N+1)] for j in range(M)]


numbers = {}    #DICTIONARY

for s in range(M):
    for t in range(N):
        numbers[(s,t)] = False

for n in range(4):  #DEFINE NUMBERS 0~3

    while True:     
        print('Please enter the x-coordinate of a figure "',n,'". Or enter "q" to go next step.')
    
        i = input("")
    
        if i == "q":
            break
    
        elif 0 <= int(i) <= M-1:
        
            x = int(i)
        
            print('Please enter the y-coordinate of the figure.')
        
            i = int(input())
        
            if 0 <= i <=  N-1:

                y = i

                numbers[(x,y)] = n

                print('(',x,',',y,') = ',n)

            else:
                print('You entered a wrong number.It must be 0 to ',N,'.')

        else:
            print('You entered a wrong number.It must be 0 to ',M,'.')

#DEFINITION END

keys = list(numbers.keys())     #KEY LIST

values = list(numbers.values())     #VALUE LIST

judge_col = {}

judge_row = {}

def judge_zero(tuple):

    s = tuple[0]

    t = tuple[1]

    judge_col[(s,t)] = False

    judge_col[(s,t+1)] = False

    judge_row[(s,t)] = False

    judge_row[(s+1,t)] = False

for i in range(len(values)):

    if values[i] == 0:      #最後に０を判定
        judge_zero(keys[i])

    if values[i] == 3:              #数字が３で
        if numbers[(keys[i][0]+1,keys[i][1])] == 3:     #右が3ならば
            judge_row[(keys[i][0],keys[i][1])] == True
            judge_row[(keys[i][0]+1,keys[i][1])] == True
            judge_row[(keys[i][0]+2,keys[i][1])] == True
            judge_row[(keys[i][0]+1,keys[i][1]+1)] == False
            judge_row[(keys[i][0]+1,keys[i][1]-1)] == False

        if numbers[(keys[i][0]+1,keys[i][1]+1)] == 3:   #右上が3ならば
            judge_col[(keys[i][0],keys[i][1])] == True
            judge_col[(keys[i][0]+1,keys[i][1]+2)] == True
            judge_row[(keys[i][0],keys[i][1])] == True
            judge_row[(keys[i][0]+2,keys[i][1]+1)] == True

        if numbers[(keys[i][0],keys[i][1]+1)] == 3:     #上が3ならば
            judge_col[(keys[i][0],keys[i][1])] == True
            judge_col[(keys[i][0],keys[i][1]+1)] == True
            judge_col[(keys[i][0],keys[i][1]+2)] == True
            judge_col[(keys[i][0]+1,keys[i][1]+1)] == False
            judge_col[(keys[i][0]-1,keys[i][1]+1)] == False

        if numbers[(keys[i][0]-1,keys[i][1]+1)] == 3:   #左上が3ならば
            judge_col[(keys[i][0],keys[i][1])] == True
            judge_col[(keys[i][0]-1,keys[i][1]+2)] == True
            judge_row[(keys[i][0]+1,keys[i][1])] == True
            judge_row[(keys[i][0]-2,keys[i][1]+1)] == True

        if numbers[(keys[i][0]-1,keys[i][1])] == 3:     #左が3ならば
            judge_row[(keys[i][0],keys[i][1])] == True
            judge_row[(keys[i][0]+1,keys[i][1])] == True
            judge_row[(keys[i][0]-1,keys[i][1])] == True
            judge_row[(keys[i][0],keys[i][1]+1)] == False
            judge_row[(keys[i][0],keys[i][1]-1)] == False

        if numbers[(keys[i][0]-1,keys[i][1]-1)] == 3:   #左下が3ならば
            judge_col[(keys[i][0],keys[i][1]+1)] == True
            judge_col[(keys[i][0]-1,keys[i][1]-1)] == True
            judge_row[(keys[i][0]+1,keys[i][1])] == True
            judge_row[(keys[i][0]-1,keys[i][1]-1)] == True

        if numbers[(keys[i][0],keys[i][1]-1)] == 3:     #下が3ならば
            judge_col[(keys[i][0],keys[i][1])] == True
            judge_col[(keys[i][0],keys[i][1]+1)] == True
            judge_col[(keys[i][0],keys[i][1]-1)] == True
            judge_col[(keys[i][0]+1,keys[i][1])] == False
            judge_col[(keys[i][0]-1,keys[i][1])] == False
          
        if numbers[(keys[i][0]+1,keys[i][1]-1)] == 3:   #右下が3ならば
            judge_col[(keys[i][0],keys[i][1]+1)] == True
            judge_col[(keys[i][0]+1,keys[i][1])] == True
            judge_row[(keys[i][0],keys[i][1])] == True
            judge_row[(keys[i][0]+2,keys[i][1]-1)] == True

        
    elif values[i] == max(values):
        P = keys[i]

#最後に定義されていない線をすべてFalseにする予定

#SOLVE BEGIN

#(x1,y1)から(x2,y2)に移動した

x1 = 1

y1 = 1

x2 = 1

y2 = 2



if x2 - x1 == 1: #右に移動した
    if numbers[(x1,y1)] == 1:
        if judge_col[(x1,y1+1)] == True or judge_row[(x1,y1)] == True or judge_row[(x1+1,y1)] == True:
            judge_col[(x1,y1)] == False
    if y1 != 0:
        if numbers[(x1,y1-1)] == 1:
            if judge_col[(x1,y1-1)] == True or judge_row[(x1,y1-1)] == True or judge_row[(x1+1,y1-1)] == True:
                judge_col[(x1,y1)] == False

if x1 - x2 == 1: #左に移動した
    if numbers[(x1-1,y1)] == 1:
        if judge_col[(x1-1,y1+1)] == True or judge_row[(x1,y1)] == True or judge_row[(x1-1,y1)] == True:
            judge_col[(x1-1,y1)] == False
    if y1 != 0:
        if numbers[(x1-1,y1-1)] == 1:
            if judge_col[(x1-1,y1-1)] == True or judge_row[(x1-1,y1-1)] == True or judge_row[(x1,y1-1)] == True:
                judge_col[(x1-1,y1)] == False

if y2 - y1 == 1: #上に移動した
    if numbers[(x1,y1)] == 1:
        if judge_col[(x1,y1)] == True or judge_col[(x1,y1+1)] == True or judge_row[(x1+1,y1)] == True:
            judge_row[(x1,y1)] == False
    if x1 != 0:
        if numbers[(x1-1,y1)] == 1:
            if judge_col[(x1,y1)] == True or judge_col[(x1,y1+1)] == True or judge_row[(x1,y1)] == True:
                judge_row[(x1,y1)] == False

if y1 - y2 == 1: #下に移動した
    if numbers[(x1,y1-1)] == 1:
        if judge_col[(x1,y1-1)] == True or judge_col[(x1,y1)] == True or judge_row[(x1+1,y1-1)] == True:
            judge_row[(x1,y1-1)] == False
    if x1 != 0:
        if numbers[(x1-1,y1-1)] == 1:
            if judge_col[(x1-1,y1)] == True or judge_col[(x1-1,y1-1)] == True or judge_row[(x1-1,y1-1)] == True:
                judge_row[(x1,y1-1)] == False


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

def solved(a):
    if a==None:
        print(col)
        print(row)
    else:
        print("unsolved")

solved(allink(N+1,M+1))
