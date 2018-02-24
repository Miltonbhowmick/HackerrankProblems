string =input()
check = input()
l=len(check)
cnt=0
for i in range(len(string)-(l-1)):
    if string[i:i+l]==check:
        cnt+=1
print(cnt)
