import re

pattern=re.compile("ab")
matcher=pattern.finditer("abaababa")
count=0
for match in matcher:
	print("match is available at the start index:",match.start())
	count+=1

print("the number of occurances", count)



# ___________________________________________________________________________________________________________________

print("*"*100)
print("Understanding Each function")
print("*"*100)


import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaabab")
for m in matcher:
	count=count+1
	print(f"start:{m.start()}, end:{m.end()} ,group:{m.group()}" )

print("the number of occurances", count)

# ___________________________________________________________________________________________________________________
# without using compile function we can pass the pattern inside finditer. 
print("*"*100)

matcher=re.finditer("ab", "abaabab") 
for m in matcher:
	count=count+1
	print(f"start:{m.start()}, end:{m.end()} ,group:{m.group()}" )

print("the number of occurances", count)

# ___________________________________________________________________________________________________________________
# available- Character classes. 
print("*"*100)

matcher=re.finditer("[abc]",'a7b@k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('[^abc]','a7b@k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('[^a-z]','a7b@k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('[a-z]','a7b@k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('[a-z0-9]','a7b@k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('[^a-z0-9]','a7b@k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('[0-9]','a7b@k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

# ___________________________________________________________________________________________________________________
# Predefined- Character classes. 

print("*"*100)
matcher=re.finditer('\s','a7b @k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('\S','a7b @k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('\d','a7b @k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('\D','a7b @k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('\w','a7b @k9z')
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('\W','a7b @k9z') #\W ==> any character except word (special Character) [^a-zA-Z0-9]
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('.','a7b @k9z') #. ==> any or every character.
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

# ___________________________________________________________________________________________________________________
# Quantifiers- Character classes. 

print("*"*100)
matcher=re.finditer('a','abaabaaab') 
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('a+','abaabaaab') #. 
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('a*','abaabaaab') #. 
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('a?','abaabaaab') #. 
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('a{3}','abaabaaab') #. 
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('a{2,3}','abaabaaab') #. 
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('^a','abaabaaab') #. 
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )

print("*"*100)
matcher=re.finditer('b$','abaabaaab') #. 
for m in matcher:
	print(f"start:{m.start()} ........ group:{m.group()}" )


# ___________________________________________________________________________________________________________________
# Important Functions. 

print("*"*100)
s=input("Enter the pattern to check match function:")

m=re.match(s,"abcdefghij")

if m!=None: 
	print("match is available at the begining fo the string")
	print(f"Start Index:{m.start()}, End Index {m.end()}")
else:
	print("match is not avaiable at the beginingof the string")

print("*"*100)
s=input("Enter the pattern to check fullmatch:")

m=re.fullmatch(s,"abcdefghij")

if m!=None: 
	print("full string matched")
else:
	print("full string not matched")

print("*"*100)
s=input("Enter the pattern to check search function:")

m=re.search(s,"abaabaaab")

if m!=None: 
	print("Match is available")
	print(f"first aoccurnce with the start index {m.start()} and end index {m.end()}")
else:
	print("full string not matched")

print("*"*100)

l=re.findall("[0-9]","a7b9c6")

print(l)

print("*"*100)
l=re.findall("\W","PaVi@12##_$")

print(l)

print("*"*100)

matcher=re.finditer('\D',"a7bk9z6")

for m in matcher:
	print(m.start(), m.end(),m.group())
