import random
from datetime import datetime
from itertools import permutations

def get_daily_sorted_digits(target_date=None):
    if target_date is None:
        target_date = datetime.now()    
    date_str = target_date.strftime("%Y-%m-%d")
    random.seed(date_str)
    digits = random.sample(range(10), 3)
    sorted_digits = sorted(digits, key=lambda x: 10 if x == 0 else x)
    random.seed(None)
    return sorted_digits

def get_2_digit_permutations(arr):
    perms = list(permutations(arr, 2)) 
    return [int(f"{a}{b}") for a, b in perms]