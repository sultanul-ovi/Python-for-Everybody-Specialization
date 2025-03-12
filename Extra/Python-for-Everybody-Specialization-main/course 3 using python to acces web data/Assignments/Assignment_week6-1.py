import json
import urllib.request,urllib.parse,urllib.error

count = 0
sum = 0
link = input("Enter Url: ")
data = urllib.request.urlopen(link).read().decode()

print ("retrieved",len(data),'characters')

try:
  js=json.loads(data)

except:
  js=None



for i in js['comments']:
    count = count+1
    sum = sum + int(i['count'])
print ("Sum : ",sum)  
print("count : ",count)
