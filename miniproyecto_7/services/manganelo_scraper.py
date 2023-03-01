from services.manga_scraper import MangaScraper


class ManganeloScraperException(Exception):
    pass


class ManganeloScraper(MangaScraper):
    def __init__(self) -> None:
        images_xpath = "//div[contains(@class, 'container-chapter-reader')]//img"
        chapters_xpath = "//div[contains(@class, 'panel-story-chapter-list')]/ul[contains(@class, 'row-content-chapter')]/li/a"
        MangaScraper.__init__(
            self,
            images_xpath=images_xpath,
            chapters_xpath=chapters_xpath,
        )
