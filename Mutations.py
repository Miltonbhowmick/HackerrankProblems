string=list(input()) #convert string to list because list is no mutable
a,ch=input().split()
string[int(a)]=ch #replacing that a index character to ch
ans=''.join(string)
print(ans)
