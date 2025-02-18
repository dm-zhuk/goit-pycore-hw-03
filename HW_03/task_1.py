from datetime import datetime


def get_days_from_today(date: str) -> int:
    today = datetime.today().date()
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        return (today - date_obj).days
    except ValueError:
        print("Error: Can't read the date. Please follow the 'YYYY-MM-DD' format.")
        return None


date = input("Enter the date in the 'YYYY-MM-DD' format: ")
result = get_days_from_today(date)

if result is not None:
    print(
        f"Days between today ({datetime.today().date()}) and the date you entered: {result}."
    )
