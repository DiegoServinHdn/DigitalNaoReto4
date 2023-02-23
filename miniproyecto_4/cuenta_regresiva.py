import time
from datetime import datetime

NEW_YEAR = datetime.now().replace(
    year=datetime.now().year + 1,
    month=1,
    day=1,
    hour=0,
    minute=0,
    second=1,
    microsecond=0,
)


def is_new_year(current_datetime: datetime) -> bool:
    return NEW_YEAR < current_datetime


if __name__ == "__main__":
    while True:
        current_datetime = datetime.now()
        if is_new_year(current_datetime):
            print("*" * 100)
            print("Happy New Year !!!!!!!")
            print("*" * 100)
            break
        time.sleep(1)

        delta = NEW_YEAR - current_datetime

        days_left = delta.days
        seconds_left = delta.seconds + (days_left * 24 * 60 * 60)
        minutes_left = seconds_left // 60
        hours_left = minutes_left // 60

        print(
            f"Days:{days_left} Hours:{hours_left} Minutes:{minutes_left} Seconds: {seconds_left}"
        )
        print("Left to New Year!! \n")
