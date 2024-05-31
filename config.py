import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "21194358"))
API_HASH = getenv("API_HASH", "9623f07eca023e4e3c561c966513a642")
BOT_TOKEN = getenv("BOT_TOKEN", "7123283070:AAH9kkVtrBbky4zkCXpwhgEP6suzr-_yerg")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mongoguess:guessmongo@cluster0.zcwklzz.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002065943011"))
OWNER_ID = int(getenv("OWNER_ID", 7036733368))
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/WCGKING/BrandedXMention",
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/masaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kurulummm")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
STRING1 = getenv("STRING_SESSION", "BAGi8fAAXASVAooSxGHqPO27TvGwVsWfGfxnCoNT1N6r6jA7T-Du2UPK4g5-ouYv0Wg8Vu8LN2itSo6m0z1Mb-HE-WuUYW3AwOf8CVpSnCwoPgm7g8TL_1q8KPpsqWlnPrhnDQaxmBr6HFdn9SqMfv_lCOrrVoibFUrQnItbFlpGlcKkjredZnfx9jQYCYxlWO730pkhyo0cMvxA4mB8VQv3rPSaZ9sDY1RdiuMOkPnCCbuncohnypW2aj_AU1DiZbQY8o_raA-grmhKFEDUidJtHjDdGqvISyxjDQhrahVX4cDlIbHI7-F90brRPfYpITyolQrQi8CkXJE0IQiBo3_B0nJ0AQAAAAGhFXjPAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
)
PLAYLIST_IMG_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
STATS_IMG_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
TELEGRAM_AUDIO_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
TELEGRAM_VIDEO_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
STREAM_IMG_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
SOUNCLOUD_IMG_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
YOUTUBE_IMG_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/S%C3%BCmeyye-yard%C4%B1m-05-20"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
