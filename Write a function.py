def is_leap(year):
    if year%4==0 or year%400==0:
        if year%4==0 and year%400==0:
            return True
        elif year%100==0:
            return False
        else:
            return True
    else:
        return False
        
year = int(input())
print(is_leap(year))
