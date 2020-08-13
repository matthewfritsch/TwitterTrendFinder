from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("")
driver.maximize_window()
assert "Trend Calendar" in driver.title
topelems = driver.find_elements_by_css_selector("ol > li > a")
for i in range(len(topelems)):
    if topelems[i].text == "":
        break
topelems = topelems[0:i]
for e in topelems:
    print(e.text)

#elem.clear()
#elem.send_keys(Keys.RETURN)
# elem[0].click()
assert "No results found." not in driver.page_source