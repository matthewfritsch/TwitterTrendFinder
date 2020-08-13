from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class pageReader:

    def crawl(self, site):

        driver = webdriver.Chrome()
        driver.get(site)

        if "404 NOT FOUND"  in driver.page_source:
            return "No values."

        driver.maximize_window()
        button = driver.find_element_by_link_text("More")
        button.click()
        topelems = driver.find_elements_by_css_selector("ol > li > a")
        for i in range(len(topelems)):
            if topelems[i].text == "":
                break
        topelems = topelems[0:i]

        results = '\n'.join([b.text for b in topelems])

        for e in topelems:
            print(e.text)
        botelems = driver.find_elements_by_xpath("//ol[@id='readmore1']/li/a")

        results += '\n'.join([b.text for b in botelems])
        return results