string=input()
chk=False
for i in string:
    if (i >='a' and i<='z')or(i>='A' and i<='Z') or(i>='0' and i<='9'):
        chk=True
if chk : print(chk)
else: print(False)
chk=False
for i in string:
    if (i >='a' and i<='z')or(i>='A' and i<='Z'):
        chk=True
if chk : print(chk)
else: print(False)
chk=False
for i in string:
    if i >='0' and i<='9':
        chk=True
if chk : print(chk)
else: print(False)
chk=False
for i in string:
    if i >='a' and i<='z':
        chk=True
if chk : print(chk)
else: print(False)
chk=False
for i in string:
    if i >='A' and i<='Z':
        chk=True
if chk : print(chk)
else: print(False)




