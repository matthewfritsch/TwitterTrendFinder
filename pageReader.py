from selenium import webdriver
from selenium.webdriver.common.keys import Keys

f = open('website.txt', 'r')
#website = 'trend/' + f.readline() + "2020-08-12.html"
website = f.readline()
f.close()

driver = webdriver.Chrome()
driver.get(website)

assert "404 NOT FOUND" not in driver.page_source

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
print(results)