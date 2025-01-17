a = int(input())
b = input()
b=str(b)
b = b.split()
x=0
i =0
s= 0
if len(b) == a:
    if len(b) % 2 == 0:
        while s < len(b)/2:
            n = []
            n.append(b[i])
            n.append(b[i+1])
            i += 2
            if int(n[1]) == int(min(n)):
                i+=1
                s+=1
            x = x + int(min(n))
            
            s +=1
    else:
        b.append(0)
        while s < len(b)/2:
            n = []
            n.append(b[i])
            n.append(b[i+1])
            i += 2
            if int(n[1]) == int(min(n)):
                i+=1
                s+=1
            x = x + int(min(n))
            
            s +=1
    print(x)