a =int(input())
b1= input()
b=[]
b = b1.split()
if len(b) == a :
    if int(b[0])<0 or int(b[0]) == int(min(b)) :
        
        m =[]
        n = []
        x=0
        while x < len(b):
            if int(b[x]) < 0:
                m.append(b[x])
            else:
                n.append(b[x])
            x+=1
        if len(m) != 0 :
            print(min(m),end='')
        else:
            print(min(n),end='')
    elif int(b[0])== int(max(b)) and int(b[1]) < 0:
       print(0)
    else:
        x=0
        y=0
        while int(b.index(int(b[x]))) <len(b):
            y = y+int(b[x])
            x+=1
        print(y)