string=input()
chk=False
for i in string:
    if i.isalnum():
        chk=True
if chk : print(chk)
else: print(False)
chk=False
for i in string:
    if i.isalpha() :
        chk=True
if chk : print(chk)
else: print(False)
chk=False
for i in string:
    if i.isdigit():
        chk=True
if chk : print(chk)
else: print(False)
chk=False
for i in string:
    if i.islower():
        chk=True
if chk : print(chk)
else: print(False)
chk=False
for i in string:
    if i.isupper():
        chk=True
if chk : print(chk)
else: print(False)




