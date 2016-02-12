#スリザーリンク4*4のmaster
M=4
N=4

print('Welcome to the SlitherLink ',M,'*',N,'!')

#DEFINITION BEGIN

numbers = {}    #DICTIONARY

while True:     #DEF3
    print('Please enter the x-coordinate of a figure "3". Or enter "q" to go next step.')
    
    i = input("")
    
    if i == "q":
        break
    
    elif 0 <= int(i) <= M:
        
        x = int(i)
        
        print('Please enter the y-coordinate of the figure.')
        
        i = input("")
        
        if 0 <= int(i) <=  N:
            y = int(i)
            def number(x,y):
                return 3
            numbers[x,y] = 3
            print('(',x,',',y,') = ',number(x,y))

        else:
            print('You entered a wrong number.It must be 0 to ',N,'.')

    else:
        print('You entered a wrong number.It must be 0 to ',M,'.')


while True:     #DEF2
    print('Please enter the x-coordinate of a figure "2". Or enter "q" to go next step.')
    
    i = input("")
    
    if i == "q":
        break
    
    elif 0 <= int(i) <= M:
        
        x = int(i)
        
        print('Please enter the y-coordinate of the figure.')
        
        i = input("")
        
        if 0 <= int(i) <=  N:
            y = int(i)
            def number(x,y):
                return 2
            numbers[x,y] = 2
            print('(',x,',',y,') = ',number(x,y))

        else:
            print('You entered a wrong number.It must be 0 to ',N,'.')

    else:
        print('You entered a wrong number.It must be 0 to ',M,'.')

while True:     #DEF1
    print('Please enter the x-coordinate of a figure "1". Or enter "q" to go next step.')
    
    i = input("")
    
    if i == "q":
        break
    
    elif 0 <= int(i) <= M:
        
        x = int(i)
        
        print('Please enter the y-coordinate of the figure.')
        
        i = input("")
        
        if 0 <= int(i) <=  N:
            y = int(i)
            def number(x,y):
                return 1
            numbers[x,y] = 1
            print('(',x,',',y,') = ',number(x,y))

        else:
            print('You entered a wrong number.It must be 0 to ',N,'.')

    else:
        print('You entered a wrong number.It must be 0 to ',M,'.')

while True:     #DEF0
    print('Please enter the x-coordinate of a figure "0". Or enter "q" to go next step.')
    
    i = input("")
    
    if i == "q":
        break
    
    elif 0 <= int(i) <= M:
        
        x = int(i)
        
        print('Please enter the y-coordinate of the figure.')
        
        i = input("")
        
        if 0 <= int(i) <=  N:
            y = int(i)
            def number(x,y):
                return 0
            numbers[x,y] = 0
            print('(',x,',',y,') = ',number(x,y))

        else:
            print('You entered a wrong number.It must be 0 to ',N,'.')

    else:
        print('You entered a wrong number.It must be 0 to ',M,'.')

col=[[1 for i in range(N)] for j in range(M+1)]

row=[[1 for i in range(N+1)] for j in range(M)]

#DEFINITION END

#SOLVE BEGIN



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
