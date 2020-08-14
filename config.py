import os

START_DATE = os.environ.get("START_DATE") or "20200101"
END_DATE = os.environ.get("END_DATE") or "20201231"
TIMEZONE = os.environ.get("TIMEZONE") or "Asia/Seoul"

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN_KEY = os.environ.get("TWITTER_ACCESS_TOKEN_KEY")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_API_SET = True

if (
    TWITTER_CONSUMER_KEY is None
    or TWITTER_CONSUMER_SECRET is None
    or TWITTER_ACCESS_TOKEN_KEY is None
    or TWITTER_ACCESS_TOKEN_SECRET is None
):
    TWITTER_API_SET = False
    print("[WARNING] Twitter Api Key is not set, message will not be posted")
