SOURCE_PATH = "templates"
TARGET_PATH = "target"
TEMPLATE_FILE = "letterboxd.template.html"
TARGET_FILE = "letterboxd.html"
STYLE_FILE = "letterboxd.css"
CONFIG_FILE = "config.yml"

GRAPH_DICT = {
    "WATCHES_MONTH": {
        "data": [],
        "labels": [],
        "title": "Watches by Month",
        "filename": "watches_months.png",
    },
    "WATCHED_GENRES": {
        "data": [],
        "labels": [],
        "title": "Watched Genres",
        "filename": "watched_genres.png",
    },
    "WATCHED_SOURCES": {
        "data": [],
        "labels": [],
        "title": "Sources",
        "filename": "watched_sources.png",
    },
    "WATCHED_ADAPTATIONS": {
        "data": [],
        "labels": [],
        "title": "Adaptations",
        "filename": "watched_adaptations.png",
    },
    "ANIMATION_LIVE_ACTION": {
        "data": [],
        "labels": [],
        "title": "Animation vs Live Action",
        "filename": "animation_live_action.png",
    }
}

TEMPLATE_GRAPH_DATA = [
    {"id": "graphics_watches_by_month", "title": "Watches By Month", "file": "watches_months.png"},
    {"id": "graphics_most_watched_genres", "title": "Most Watched Genres", "file": "watched_genres.png"},
    {"id": "graphics_most_watched_sources", "title": "Most Watched Sources", "file": "watched_sources.png"},
    {"id": "graphics_most_watched_adaptations", "title": "Most Watched Adaptations", "file": "watched_adaptations.png"},
    {"id": "graphics_animation_vs_live_action", "title": "Animation vs Live Action Movies", "file": "animation_live_action.png"},
]
