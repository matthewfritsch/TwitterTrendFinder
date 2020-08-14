from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class pageReader:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def crawl(self, site):
        self.driver.get(site)

        if "404 NOT FOUND"  in self.driver.page_source:
            return "No values."

        self.driver.maximize_window()
        button = self.driver.find_element_by_link_text("More")
        button.click()
        topelems = self.driver.find_elements_by_css_selector("ol > li > a")
        for i in range(len(topelems)):
            if topelems[i].text == "":
                break
        topelems = topelems[0:i]

        results = '\n'.join([b.text for b in topelems])

        for e in topelems:
            print(e.text)
        botelems = self.driver.find_elements_by_xpath("//ol[@id='readmore1']/li/a")

        results += '\n'.join([b.text for b in botelems])
        
        return results