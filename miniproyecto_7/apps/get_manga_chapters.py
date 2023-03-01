from services.manganelo_scraper import ManganeloScraper

from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


@timeit
def scraper_handler(event: dict, context: str) -> dict:
    """
    Get manga chapters GET method handler

    Args:
        event (dict): lambda event
        context (str): lambda context

    Returns:
        dict: Manga chapters response
    """
    print(event)
    print(context)

    request_body = event.get("body")
    chapters_url = request_body.get("url")

    scraper = ManganeloScraper()
    return scraper.crawl_chapters(chapters_url)
