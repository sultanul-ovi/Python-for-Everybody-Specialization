def find_largest_and_smallest():
    largest = None
    smallest = None

    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == "done":
            break
        try:
            num = int(user_input)
            if largest is None or num > largest:
                largest = num
            if smallest is None or num < smallest:
                smallest = num
        except ValueError:
            print("Invalid input")

    print("Maximum is", largest)
    print("Minimum is", smallest)


find_largest_and_smallest()
