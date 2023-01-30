import random
c=0
c1=0
while(True):
    n=int(input("enter your input:"))
    l=['rack','paper','ceaser']
    p=random.randint(1,3)
    print(p)
    if n<0 and n>=3:
        print("invalid input")
    elif n==p :
        print("draw")
    elif n==1 and p==0:
        print("you win")
        c=c+1
    elif n==0 and p==2:
        print("you win")
        c=c+1
    elif n==2 and p==1:
        print("you win")
        c==c+1
    else:
        print("computer win")
        c1==c1+1
    
    if(c==5 or c1==5):
      break
if(c>c1):
        print("you won the game")
else:
        print("computer wons the game")
