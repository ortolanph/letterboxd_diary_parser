from src.letterboxd_utils import calculate_review_time


def same_rating(entry, rating):
    return entry.rating == rating


def contains_tag(entry, tag):
    return tag in entry.tags


def same_year(entry, year):
    return entry.year == year


def same_review_time(entry, review_time):
    entry_review_time = calculate_review_time(entry.date, entry.watched_date)
    return entry_review_time == review_time


def same_review_month(entry, review_month):
    return entry.date.month == review_month


def same_watched_month(entry, watched_month):
    return entry.watched_date.month == watched_month
