from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_until_birthday = birthday_this_year.toordinal() - today.toordinal()
        if 0 <= days_until_birthday <= 7:
            greeting_date = birthday_this_year
            if greeting_date.weekday() == 5:  # Sat
                greeting_date += timedelta(days=2)
            elif greeting_date.weekday() == 6:  # Sun
                greeting_date += timedelta(days=1)

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "greeting_date": greeting_date.strftime("%m.%d"),
                }
            )
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Sarah Thomas", "birthday": "1983.07.25"},
    {"name": "Jane Smith", "birthday": "1990.03.01"},
    {"name": "Katie Taylor", "birthday": "1987.09.09"},
    {"name": "Daniel Martinez", "birthday": "1994.02.20"},
    {"name": "Alice Johnson", "birthday": "1988.03.02"},
    {"name": "Michael Brown", "birthday": "1985.01.28"},
    {"name": "Emily Davis", "birthday": "1980.02.22"},
    {"name": "Chris Wilson", "birthday": "1995.04.12"},
    {"name": "David Anderson", "birthday": "1991.02.26"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Current week greetings list:", upcoming_birthdays)
