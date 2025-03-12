largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done' :
        break
    try:
        number = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = number
    elif largest < number:
        largest = number
    if smallest is None:
        smallest = number
    elif smallest > number:
        smallest = number


print("Maximum is", int(largest))
print("Minimum is", int(smallest))