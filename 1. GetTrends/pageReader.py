from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class pageReader:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def crawl(self, site):
        self.driver.get(site)

        if "404 NOT FOUND"  in self.driver.page_source or "No data found." in self.driver.page_source:
            return None

        self.driver.maximize_window()
        button = ""
        try:
            button = self.driver.find_element_by_link_text("More")
        except NoSuchElementException:
            return None
        button.click()
        topelems = self.driver.find_elements_by_css_selector("ol > li > a")
        for i in range(len(topelems)):
            if topelems[i].text == "":
                break
        topelems = topelems[0:i]

        botelems = self.driver.find_elements_by_xpath("//ol[@id='readmore1']/li/a")

        results = [t.text for t in topelems] + [b.text for b in botelems]

        return results[:50]