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


def create_graph_data(data_dict, need_sorting):
    if need_sorting:
        data_dict = dict(sorted(data_dict.items()))

    return {
        "data": list(data_dict.values()),
        "labels": list(data_dict.keys())
    }


def to_sinple_movie(entry):
    return {
        "name": entry.name,
        "rating": entry.rating,
        "watched": entry.watched_date.strftime('%Y-%m-%d'),
        "review_link": entry.uri
    }


def identity_transformer(data):
    return data


def to_month_transformer(data):
    return MONTHS[data - 1]
