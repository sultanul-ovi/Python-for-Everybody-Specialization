fname = input("Enter file name: ")
fh = open(fname)

number_of_lines = 0
values = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        values += float(line.replace("X-DSPAM-Confidence:", "").lstrip())
        number_of_lines = number_of_lines +1
        
print("Average spam confidence:" , values/number_of_lines)
