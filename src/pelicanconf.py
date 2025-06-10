# Basic settings
AUTHOR = 'Alexey Vorobyov'
SITENAME = "Full-Stack Software Engineer"
SITE_DESCRIPTION = "Full-stack developer specializing in Python (Django/FastAPI) and JavaScript (React/Vue) with 7+ years of experience building scalable web applications and AI-powered solutions."
SITEURL = ""

PATH = "content"
TIMEZONE = 'Europe/Riga'
DEFAULT_LANG = 'en'

# Theme
THEME = "resume"

# Resume-specific settings
PROFILE_TITLE = "Software Engineer"
PROFILE_IMAGE = "images/profile.jpg"
CONTACT_LOCATION = "Remote / Latvia"

SOCIAL_LINKS = (
    ("LinkedIn", "https://www.linkedin.com/in/vorobyovalexey/"),
    ("GitHub", "https://github.com/peacefulseeker"),
)

TECHNOLOGIES = [
    "Python/Django/DRF/FastAPI",
    "RAG (LangChain, Azure AI Search)",
    "JavaScript/React/Vue/TypeScript",
    "AWS/Azure",
    "Sentry/Grafana",
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

# Content settings - minimal configuration
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

# Disable feeds - not needed for a resume site
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disable archives, tags, categories pages
ARCHIVES_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Clean URLs
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Sort articles by filename for proper ordering
DEFAULT_METADATA = {
    'status': 'published',
}
# Development settings
RELATIVE_URLS = True
