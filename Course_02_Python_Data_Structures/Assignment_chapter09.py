'''
9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.
'''

# Program to find the sender with the highest number of emails in 'mbox-short.txt'

# Prompt user for file name, default to 'mbox-short.txt' if no input is given
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

# Open the file for reading
handle = open(name)

# Initialize a list to store email senders and a dictionary for counting occurrences
senders1 = list()
senders = dict()

# Read through the file line by line
for line in handle:
    line = line.split()  # Split the line into words
    if len(line) < 3 or line[0] != 'From':  # Ignore lines that don't start with 'From'
        continue
    senders1.append(line[1])  # Extract the sender's email and store it in the list

# Count occurrences of each sender
for sender in senders1:
    senders[sender] = senders.get(sender, 0) + 1  # Increment count using dictionary

# Determine the sender with the highest count
maximum = None
theone = None
for sender, count in senders.items():
    if maximum is None or count > maximum:  # Update maximum if a higher count is found
        maximum = count
        theone = sender

# Print the sender with the highest count and the corresponding number of emails
print(theone, maximum)
