from datetime import datetime, timedelta
import config
import tweet
import pytz


def datediff(d1, d2):
    if d2 > d1:
        return d2 - d1
    return d1 - d2


def format_msg(left, passed, total):
    return f"D-{left.days} ({passed.days}/{total.days})"


def main():
    start_date = datetime.strptime(config.START_DATE, "%Y%m%d").date()
    end_date = datetime.strptime(config.END_DATE, "%Y%m%d").date()
    today = datetime.now(tz=pytz.timezone(config.TIMEZONE)).date()

    total_days = datediff(start_date, end_date) + timedelta(days=1)
    passed_days = datediff(start_date, today) + timedelta(days=1)
    left_days = datediff(today, end_date)

    msg = format_msg(left_days, passed_days, total_days)
    tweet.post(msg)
    

if __name__ == "__main__":
    main()
