n=int(input())
student={}
for i in range(n):
    name=input()
    a=input()
    a=float(a)
    student.update({name:a})
mark=set(student.values())
mark=list(mark)
mark.sort()
ck=mark[1]
ans=[]
for key,value in student.items():
    if ck == value:
        ans.append(key)

ans.sort()
for i in ans:
    print(i)
