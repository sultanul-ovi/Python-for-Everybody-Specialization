def computepay(hours, rate):
    """Compute gross pay based on hours and rate.lol"""
    if hours > 40:
        overtime_hours = hours - 40
        return (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        return hours * rate


hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))


gross_pay = computepay(hours, rate)
print("Pay", gross_pay)
