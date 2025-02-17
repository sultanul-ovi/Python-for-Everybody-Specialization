'''
7.1 Write a program that prompts for a file name, then opens that file and
reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
'''
fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for line in fh :
    line = line.upper()
    line = line.rstrip()
    print(line)



'''
7.2 Write a program that prompts for a file name, then opens that file and
reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Invalid input')

count = 0
total = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    fpos = line.find(':')
    fval = float(line[fpos+2:].strip())
    count = count + 1
    total = total + fval
    
avg = total/count
print('Average spam confidence:' , avg)
