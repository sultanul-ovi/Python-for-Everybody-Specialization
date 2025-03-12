import urllib.request
import re

# Define the URL for the data file
url = "http://py4e-data.dr-chuck.net/regex_sum_2134790.txt"

# Download the file
try:
    # Open the URL and read the content
    response = urllib.request.urlopen(url)
    total_sum = 0

    # Process each line in the file
    for line in response:
        # Decode byte line to string and then find numbers using regular expressions
        line = line.decode('utf-8')  # Convert byte line to string
        numbers = re.findall('[0-9]+', line)

        # Convert found numbers to integers and sum them
        total_sum += sum([int(num) for num in numbers])

    # Print the total sum of numbers
    print("Total sum:", total_sum)

except Exception as e:
    print(f"Error: {e}")
