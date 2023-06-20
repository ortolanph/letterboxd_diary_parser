SOURCE_PATH = "templates"
TARGET_PATH = "target"
TEMPLATE_FILE = "letterboxd.template"
TARGET_FILE = "letterboxd.html"
STYLE_FILE = "letterboxd.css"

GRAPH_DICT = {
    "RATINGS": {
        "data": {
            "statistics": {},
            "sort": True
        },
        "graph": {
            "title": "Movies by Ratings",
            "ylabel": "Number of Movies",
            "xlabel": "Ratings",
            "filename": "ratings.png",
            "width": 6.4,
            "height": 5
        }
    },
    # "TAGS": {
    #     "data": {
    #         "statistics": {},
    #         "sort": False
    #     },
    #     "graph": {
    #         "title": "Movies by Tags",
    #         "ylabel": "Number of Movies",
    #         "xlabel": "Tags",
    #         "filename": "tags.png",
    #         "width": 9,
    #         "height": 7
    #     }
    # },
    # "YEAR": {
    #     "data": {
    #         "statistics": {},
    #         "sort": True
    #     },
    #     "graph": {
    #         "title": "Movies by Years",
    #         "ylabel": "Number of Movies",
    #         "xlabel": "Years",
    #         "filename": "years.png",
    #         "width": 17,
    #         "height": 6.4
    #     }
    # },
    # "LAZY_REVIEWS": {
    #     "data": {
    #         "statistics": {},
    #         "sort": True
    #     },
    #     "graph": {
    #         "title": "Lazy Reviews",
    #         "ylabel": "Number of Movies",
    #         "xlabel": "Days that I took to review",
    #         "filename": "lazyreviews.png",
    #         "width": 10,
    #         "height": 4.8
    #     }
    # },
    # "REVIEWS_MONTH": {
    #     "data": {
    #         "statistics": {},
    #         "sort": False
    #     },
    #     "graph": {
    #         "title": "Reviews by Month",
    #         "ylabel": "Number of Reviews",
    #         "xlabel": "Months",
    #         "filename": "reviews_months.png",
    #         "width": 10,
    #         "height": 6
    #     }
    # },
    "WATCHES_MONTH": {
        "data": {
            "statistics": {},
            "sort": False
        },
        "graph": {
            "title": "Watches by Month",
            "ylabel": "Number of Watches",
            "xlabel": "Months",
            "filename": "watches_months.png",
            "width": 10,
            "height": 6
        }
    },
    "WATCHED_GENRES": {
        "data": {
            "statistics": {},
            "sort": False
        },
        "graph": {
            "title": "Watched Genres",
            "ylabel": "Movies",
            "xlabel": "Genres",
            "filename": "watched_genres.png",
            "width": 10,
            "height": 6
        }
    },
    "WATCHED_SOURCES": {
        "data": {
            "statistics": {},
            "sort": False
        },
        "graph": {
            "title": "Sources",
            "ylabel": "Number of Watches",
            "xlabel": "Sources",
            "filename": "watched_sources.png",
            "width": 10,
            "height": 6
        }
    },
    "WATCHED_ADAPTATIONS": {
        "data": {
            "statistics": {},
            "sort": False
        },
        "graph": {
            "title": "Adaptations",
            "ylabel": "Number of Watches",
            "xlabel": "Kinds of Adaptations",
            "filename": "watched_adaptations.png",
            "width": 10,
            "height": 6
        }
    },
}

TEMPLATE_GRAPH_DATA = [
    {"id": "graphics_movies_by_ratings", "title": "Movies By Ratings", "file": "ratings.png"},
    # {"id": "graphics_movies_by_tags", "title": "Movies By Tags", "file": "tags.png"},
    # {"id": "graphics_movies_by_year", "title": "Movies By Year", "file": "years.png"},
    # {"id": "graphics_lazy_reviews", "title": "Lazy Reviews", "file": "lazyreviews.png"},
    # {"id": "graphics_reviews_by_month", "title": "Reviews By Month", "file": "reviews_months.png"},
    {"id": "graphics_watches_by_month", "title": "Watches By Month", "file": "watches_months.png"},
    {"id": "graphics_most_watched_genres", "title": "Most Watched Genres", "file": "watched_genres.png"},
    {"id": "graphics_most_watched_sources", "title": "Most Watched Sources", "file": "watched_sources.png"},
    {"id": "graphics_most_watched_adaptations", "title": "Most Watched Adaptations", "file": "watched_adaptations.png"},
]
