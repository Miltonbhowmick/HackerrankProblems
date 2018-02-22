n=int(input())
a=input()
a=set(map(int,a.split())) # set is for ingoring deuplicate value
# 'set' doesn't support index(0...n) value!
# To print second last value i used a list to access by a index!
a=list(a)
a.sort()
l=len(a)
print(a[-2])
