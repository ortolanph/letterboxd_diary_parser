def contains_tag(entry, tag):
    return tag in entry.tags


def same_year(entry, year):
    return entry.year == year


def same_watched_month(entry, watched_month):
    return entry.watched_date.month == watched_month
