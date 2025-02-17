'''
10.2 Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the hour
out from the 'From ' line by finding the time and then splitting the string a
second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
'''

# Open the file
filename = "mbox-short.txt"
try:
    with open(filename, 'r') as file:
        counts = {}

        # Process each line
        for line in file:
            # Look for lines that start with 'From '
            if line.startswith("From "):
                # Split the line into words
                parts = line.split()
                # Extract the time part (5th element in the line)
                time = parts[5]
                # Split the time into hour, minute, second
                hour = time.split(':')[0]
                # Count the occurrences of the hour
                counts[hour] = counts.get(hour, 0) + 1

        # Sort the dictionary by hour and print the results
        for hour, count in sorted(counts.items()):
            print(hour, count)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
