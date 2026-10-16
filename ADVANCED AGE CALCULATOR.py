from datetime import date, datetime
import calendar

def calculate_age(dob, on_date):
    if dob > on_date:
        raise ValueError("Date of birth cannot be in the future!")

    years = on_date.year - dob.year
    months = on_date.month - dob.month
    days = on_date.day - dob.day

    if days < 0:
        months -= 1
        previous_month = on_date.month - 1 or 12
        previous_year = on_date.year if on_date.month > 1 else on_date.year - 1
        days += calendar.monthrange(
            previous_year, previous_month
        )[1]

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def zodiac_sign(dob):
    m, d = dob.month, dob.day

    signs = [
        ((1, 20), "Capricorn"), ((2, 19), "Aquarius"),
        ((3, 21), "Pisces"), ((4, 20), "Aries"),
        ((5, 21), "Taurus"), ((6, 21), "Gemini"),
        ((7, 23), "Cancer"), ((8, 23), "Leo"),
        ((9, 23), "Virgo"), ((10, 23), "Libra"),
        ((11, 22), "Scorpio"), ((12, 22), "Sagittarius")
    ]

    if (m, d) >= (12, 22) or (m, d) <= (1, 19):
        return "Capricorn" if m == 12 or (m == 1 and d <= 19) else "Capricorn"

    for (sm, sd), sign in signs:
        if (m, d) < (sm, sd):
            return sign

    return "Sagittarius"


def next_birthday(dob, today):
    year = today.year

    while True:
        try:
            birthday = date(year, dob.month, dob.day)
        except ValueError:
            # Treat Feb 29 as Feb 28 in non-leap years
            birthday = date(year, 2, 28)

        if birthday >= today:
            return birthday
        year += 1


def main():
    print("=" * 38)
    print("       ADVANCED AGE CALCULATOR")
    print("=" * 38)

    try:
        dob_text = input("Enter DOB (DD-MM-YYYY): ")
        dob = datetime.strptime(dob_text, "%d-%m-%Y").date()

        today = date.today()

        if dob > today:
            print("Error: DOB cannot be in the future.")
            return

        print("\n1. Age today")
        print("2. Age on a specific date")
        choice = input("Choose option (1/2): ")

        if choice == "2":
            target_text = input("Enter date (DD-MM-YYYY): ")
            target = datetime.strptime(
                target_text, "%d-%m-%Y"
            ).date()
        elif choice == "1":
            target = today
        else:
            print("Invalid choice!")
            return

        if target < dob:
            print("Error: Selected date is before DOB.")
            return

        years, months, days = calculate_age(dob, target)
        total_days = (target - dob).days
        next_bday = next_birthday(dob, target)

        print("\n" + "=" * 38)
        print("           YOUR AGE REPORT")
        print("=" * 38)

        print(f"Date of Birth : {dob.strftime('%d-%m-%Y')}")
        print(f"Calculated On : {target.strftime('%d-%m-%Y')}")
        print(f"Exact Age     : {years} years, {months} months, {days} days")
        print(f"Total Months  : {years * 12 + months}")
        print(f"Total Weeks   : {total_days // 7}")
        print(f"Total Days    : {total_days}")
        print(f"Approx Hours  : {total_days * 24}")
        print(f"Born On       : {dob.strftime('%A')}")
        print(f"Zodiac Sign   : {zodiac_sign(dob)}")
        print(f"Next Birthday : {next_bday.strftime('%d-%m-%Y')}")
        print(f"Days Until Birthday: {(next_bday - target).days}")

        print("=" * 38)

    except ValueError as error:
        print("Invalid input:", error)
        print("Please enter a valid date in DD-MM-YYYY format.")


if __name__ == "__main__":
    main()
