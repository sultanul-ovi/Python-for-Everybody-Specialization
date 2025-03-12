import re
name = input("enter the file name:")
if len(name)<1 : name = "regex_sum_445833.txt"
handle=open(name)
x=list()
for line in handle:
    y=re.findall('[0-9]+',line)
    x=x+y
sum=0
for i in x:
    sum=sum+int(i)
print(sum)
