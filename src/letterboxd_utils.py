import datetime

MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


def parse_date(my_date):
    return datetime.date.fromisoformat(my_date)


def parse_tags(my_tags):
    return my_tags.replace('"', '').strip().split(",")


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


def to_simple_movie(entry):
    return {
        "name": entry.name,
        "rating": entry.rating,
        "watched": entry.watched_date.strftime('%Y-%m-%d'),
        "review_link": entry.uri,
        "tags": entry.tags,
        "runtime": format_duration(entry.runtime),
        "tmdb_id": entry.tmdb_id,
        "imdb_id": entry.imdb_id
    }


def identity_transformer(data):
    return data


def to_month_transformer(data):
    return MONTHS[data - 1]


def format_duration(duration):
    return str(datetime.timedelta(minutes=duration))
