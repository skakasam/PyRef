"""Python Requests Library Practice - API Constants"""

API_TOKEN = "2b4a73aae496910ffb3ef45423668db14023f8aac3db84c42b360d16edfec8d2"
API_BASE_URL = "https://gorest.co.in/"
API_BASE_PATH = "public/"
API_BASE_VERSION = "v2/"

USER_RESOURCE = API_BASE_URL + API_BASE_PATH + API_BASE_VERSION + "users/"
BEARER_TOKEN = f"Bearer {API_TOKEN}"

RETRIES = 3
TIMEOUT = 5  # seconds
