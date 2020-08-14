import config
import twitter


def post(message):
    if not config.TWITTER_API_SET:
        print(message)
        return

    api = twitter.Api(
        consumer_key=config.TWITTER_CONSUMER_KEY,
        consumer_secret=config.TWITTER_CONSUMER_SECRET,
        access_token_key=config.TWITTER_ACCESS_TOKEN_KEY,
        access_token_secret=config.TWITTER_ACCESS_TOKEN_SECRET,
    )

    try:
        api.VerifyCredentials()
    except:
        print("[ERROR] Invalid API token")
        print(message)
        return

    api.PostUpdate(status=message)
