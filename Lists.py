li=[]

n= int(input())
for i in  range(n):
    s=input().split()
    if s[0]=="insert":
        a=int(s[1])
        b=int(s[2])
        li.insert(a,b)        
    elif s[0]=="print":
        print(li)
    elif s[0]=="remove":
        a=int(s[1])
        li.remove(a)
    elif s[0]=="append":
        a=int(s[1])
        li.append(a)
    elif s[0]=="sort":
        li.sort()
    elif s[0]=="pop":
        li.pop()
    elif s[0]=="reverse":
        li.reverse()
