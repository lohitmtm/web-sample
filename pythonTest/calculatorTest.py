from selenium import webdriver
#from selenium.webdriver.geckodriver.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


options = Options();
options.add_argument("--headless");
first = "9"
second = "10"
#driver = webdriver.geckodriver(executable_path=r"C:\Users\132803\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe",options=options)
driver = webdriver.Firefox(executable_path=r"C:\Users\132803\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe",options=options)
#driver = webdriver.Firefox(firefox_options=options);
driver.get("http://localhost:8090/websample/index.jsp")
current_url=driver.current_url
assert "Addition" in driver.title
elem = driver.find_element_by_name("first")
elem.send_keys(first)
elem = driver.find_element_by_name("second")
elem.send_keys(second)
elem.send_keys(Keys.RETURN)

# wait for URL to change with 15 seconds timeout
WebDriverWait(driver, 15).until(EC.url_changes(current_url))

# print new URL
new_url = driver.current_url
print(new_url)
element=driver.find_element_by_id("result")
print(element.text)
assert element.text == 'Sum is 19'
driver.close()
