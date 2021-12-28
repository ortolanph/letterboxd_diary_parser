import datetime

MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


def parse_date(my_date):
    return datetime.date.fromisoformat(my_date)


def parse_tags(my_tags):
    return my_tags.replace('"', '').strip().split(",")


def calculate_review_time(date, watched_date):
    delta = date - watched_date
    return delta.days


def is_rewatch(rewatch_flag):
    if not rewatch_flag:
        return False
    else:
        if rewatch_flag == "Yes":
            return True
        else:
            return False


def create_table(title, header, values):
    print(title)
    print("------------------")
    print(header)
    for key in values:
        print(f"{key},{values[key]}")
    print()


def identity_transformer(data):
    return data


def to_month_transformer(data):
    return MONTHS[data - 1]
