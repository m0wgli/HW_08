import collections
from datetime import datetime, timedelta

from collections import defaultdict

from pprint import pprint


def prepare_birthday(text: str):
    try:
        bd = datetime.strptime(text, '%d, %m, %Y')
        return bd.replace(year=datetime.now().year).date()
    except ValueError:
        if text.startswith('29, 2'):
            return datetime.now().date().replace(day=1, month=3)
        else:
            raise ValueError("Некоректний формат дати народження")


def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days=diff_days)


def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    today = datetime.now().date()

    nex_week_start = get_next_week_start(today)
    start_period = nex_week_start - timedelta(2)
    end_period = nex_week_start + timedelta(4)

    happy_users = [user for user in users if start_period <= prepare_birthday(user['birthday']) <= end_period]

    for user in happy_users:
        current_bd = prepare_birthday(user['birthday'])
        if current_bd.weekday() in (5, 6):
            birthdays['Monday'].append(user['name'])
        else:
            birthdays[current_bd.strftime('%A')].append(user['name'])

    return collections.OrderedDict(birthdays)


if __name__ == "__main__":
    users = [{'name': 'Jude', 'birthday': '27, 3, 1990'},
             {'name': 'Andrew', 'birthday': '28, 3, 1990'},
             {'name': 'Ibrahim', 'birthday': '29, 3, 1990'},
             {'name': 'Virgil', 'birthday': '30, 3, 1990'},
             {'name': 'Roberto', 'birthday': '31, 3, 1990'},
             {'name': 'Mohamed', 'birthday': '1, 4, 1990'},
             {'name': 'Darwin', 'birthday': '2, 4, 1990'},
             {'name': 'Luis', 'birthday': '26, 3, 1990'},
             {'name': 'Cody', 'birthday': '25, 3, 1990'},
             {'name': 'Stefan', 'birthday': '24, 3, 1990'},
             {'name': 'James', 'birthday': '29, 2, 1990'}]

    result = get_birthdays_per_week(users)
    pprint(result)
