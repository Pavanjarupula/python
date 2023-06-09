import random
lad_s=[8,12,18]
print("ladder starting point ",lad_s)
lad_e=[19,22,30]
print("ladder ending point  ",lad_e)
w=36
sn_s=[20,35]
print("snake starting :",sn_s)
sn_e=[10,19]
print("snake starting :",sn_e)
print("winnig point ",w)
s=0
c=0
while(True):
    r=random.randint(1,6)
    print("dice value :",r)
    c=c+1
    s=s+r
    if s in lad_s:
        for i in range(len(lad_s)):
            if lad_s[i]==s:
                print("ladder")
                s=lad_e[i]
                print("present position",s)
            break
    if s in sn_s:
        for i in range(len(sn_s)):
            if sn_s[i]==s:
                print("snake")
                s=sn_e[i]
                print("present position",s)
                
            break
    if s>w:
        s=s-r
        print("value not condider enter again")
        c=c-1
    elif s==w:
        print("your win with ",c,"steps")
        break
    else:
        print("continue")
        
                
    
