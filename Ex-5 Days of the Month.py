# Print all months with their numbers
print("JANUARY : 1","FEBRUARY : 2", "MARCH : 3", "APRIL : 4", "MAY : 5", "JUNE : 6", "JULY : 7", "AUGUST : 8", "SEPTEMBER : 9", "OCTOBER : 10", "NOVEMBER : 11", "DECEMBER : 12",sep="\n")

# Dictionary of days in each month
days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Get month number from user
month = int(input("\nEnter the month number [1-12]: "))

if 1 <= month <= 12:
    if month == 2:
        # Handle February separately for leap years
        leap = input("\nIs it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("\nFebruary has 29 days.")
        elif leap == "no":
            print("\nFebruary has 28 days.")
        else:
            print("\nEnter a valid input")
    else:
        print(f"\nThis month has {days_in_month[month]} days.")
else:
    print("\nInvalid month number.")