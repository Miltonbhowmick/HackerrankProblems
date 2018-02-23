string=list(input())

for i in range(len(string)):
    if(string[i].isalpha()):
        if string[i]>='a' and string[i]<='z':
            string[i]=string[i].upper()
        else:
            string[i]=string[i].lower()
string=''.join(string)
print(string)
            

