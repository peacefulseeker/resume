AUTHOR = 'Alexey Vorobyov'
SITENAME = "Senior Software Engineer"
SITE_DESCRIPTION = "Senior full-stack engineer specializing in Python (FastAPI, Django) and JavaScript (React, Vue) with 7+ years of experience building scalable web applications and AI-powered solutions."
SITEURL = ""

PATH = "content"
TIMEZONE = 'Europe/Riga'
DEFAULT_LANG = 'en'

# Theme
THEME = "resume"

# Resume-specific settings
PROFILE_TITLE = "Senior Software Engineer"
PROFILE_IMAGE = "images/profile.jpg"
CONTACT_LOCATION = "Remote / Latvia"

SOCIAL_LINKS = (
    ("LinkedIn", "https://www.linkedin.com/in/vorobyovalexey/"),
    ("GitHub", "https://github.com/peacefulseeker"),
)

TECHNOLOGIES = [
    "Python, FastAPI, SQLAlchemy",
    "JS/TS, React, Node.js",
    "AWS, Azure, Terraform",
    "Sentry, Grafana, Opentelemetry",
]

LANGUAGES = [
    "English (C1)", "Latvian (C1)", "Russian (Native)"
]

HOBBIES = [
    "Hiking/Trekking",
    "Functional workouts & running",
    "Playing Piano",
    "Landscape photography",
    "Reading books"
]

# Content settings - minimal configuration, not needed for a resume site
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

# Disable feeds -
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disable subpages
ARCHIVE_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARTICLE_URL = ''
ARTICLE_SAVE_AS = ''

DEFAULT_METADATA = {
    'date': '2000-01-01', # A fixed date far in the past, required for Pelican to generate the site without errors
}
ARTICLE_ORDER_BY = 'basename' # Order articles by filename

# SERVER
BIND='localhost'
PORT=8123
