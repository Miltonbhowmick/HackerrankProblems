def wrap (s,w):
    i=0
    while(i<len(s)):
        print(s[i:i+w])
        i+=w
s=input()
w=int(input())
wrap(s,w)
