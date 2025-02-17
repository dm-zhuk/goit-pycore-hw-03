import random


def get_numbers_ticket(min_int, max_int, ln_quantity):
    if min_int < 1 or max_int > 1000:
        return []

    try:
        return sorted(random.sample(range(min_int, max_int + 1), ln_quantity))
    except ValueError:
        return []


min_int = 1
max_int = 49
ln_quantity = 6

lottery_numbers = get_numbers_ticket(min_int, max_int, ln_quantity)

print("Ваші лотерейні числа:", lottery_numbers)
