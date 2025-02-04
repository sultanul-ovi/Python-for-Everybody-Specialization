
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))


if hours > 40:
    overtime_hours = hours - 40
    gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)
else:
    gross_pay = hours * rate


print(gross_pay)
