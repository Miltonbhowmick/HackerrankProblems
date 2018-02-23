n=int(input())
store={}
for i in range(n):
    name,m,p,c=input().split()
    store.update({name:[float(m),float(p),float(c)]})
checkName=input()
ans = (store[checkName][0]+store[checkName][1]+store[checkName][2])/3.00
ans="%.2f" % round(ans,2)
print(ans)
