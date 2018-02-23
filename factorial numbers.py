##A program to show factorial less than 6

##Using Iteration
i=int(input())
fact=1
while(i):
    fact*=i
    i-=1

print(fact)

#Using recursion

def fact(a):
    if(a==0):   
        return 1 
    else:
        return a*fact(a-1)
      
a=int(input())
print (fact(a))
