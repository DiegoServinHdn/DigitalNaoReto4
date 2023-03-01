from typing import List
from bs4 import BeautifulSoup
from lxml import etree
from utils.request_utils import RequestUtils


class MangaScraper:
    def __init__(self, images_xpath: str, chapters_xpath: str) -> None:
        self.images_xpath = images_xpath
        self.chapters_xpath = chapters_xpath

    def crawl_chapters(self, chapters_url: str) -> List[dict]:
        """
        Gets manga chapters

        Args:
            chapter_url (str): Chapter url

        Returns:
            List[dict]: List of chapters
        """
        chapters: List[dict] = []
        chapters_response = RequestUtils.call_get_request(chapters_url)
        chapters_doc = BeautifulSoup(chapters_response.text, "html.parser")
        chapters_dom = etree.HTML(str(chapters_doc))

        chapters_elements = chapters_dom.xpath(self.chapters_xpath)
        chapter = {}
        
        for a in chapters_elements:
            chapter = {
                "name": a.text,
                "url": a.get("href")
            }
            chapters.append(chapter)

        return chapters

    def crawl_images(self, chapter_url: str) -> List[str]:
        """
        Gets manga images

        Args:
            chapter_url (str): _description_

        Returns:
            List[dict]: List of chapters
        """
        images: List[str] = []
        images_response = RequestUtils.call_get_request(chapter_url)
        images_doc = BeautifulSoup(images_response.text, "html.parser")
        images_dom = etree.HTML(str(images_doc))

        images_element = images_dom.xpath(self.images_xpath)
        images = [img.get("src") for img in images_element]

        return images
