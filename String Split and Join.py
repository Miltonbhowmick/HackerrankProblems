##using string As List and loop to reassign on that index 

string=list(input())
for idx in range(len(string)):
    if string[idx]==' ':
        string[idx]='-'

string=''.join(string)
print(string)

##using built-in function to replace all ' ' space character

string=input()
string=string.replace(' ','-')
print(string)

