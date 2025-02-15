from datetime import datetime

today = datetime.today().date()

date_search = input("Enter the date in the 'YYYY-MM-DD' format: ")

try:
    date_obj = datetime.strptime(date_search, "%Y-%m-%d")
    get_days_from_today = date_obj.toordinal() - today.toordinal()

    print(
        f"Days from today, {today} until the date you entered: {get_days_from_today}."
    )

except ValueError:
    print("Error: Can't read the date. Please follow the 'YYYY-MM-DD' format.")
