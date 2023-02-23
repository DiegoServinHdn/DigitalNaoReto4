from datetime import datetime

NEW_YEAR = datetime.now().replace(
    year=datetime.now().year + 1, month=1, day=1, hour=0, minute=0, second=1, microsecond=0
)


def is_new_year(current_datetime: datetime) -> bool:
    return NEW_YEAR == current_datetime


if __name__ == "__main__":
    while True:
        current_datetime = datetime.now()
        if is_new_year(current_datetime):
            print("*" * 100)
            print("Happy New Year !!!!!!!")
            print("*" * 100)
            break
        print(NEW_YEAR)