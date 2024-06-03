def is_leap_year(year):
    # Leap year is divisible by 4 and not divisible by 100
    # unless it is also divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

if __name__ == "__main__":
    main()
