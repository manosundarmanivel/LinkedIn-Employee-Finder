from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/login")
email = "Example@gmail.com"
password = "Example@123"

email_input = driver.find_element("name","session_key")
password_input = driver.find_element("name","session_password")

email_input.send_keys(email)
password_input.send_keys(password)

password_input.send_keys(Keys.ENTER)
search_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,"search-global-typeahead__input")))


search_box.send_keys("app developer")
search_box.send_keys(Keys.RETURN)

people_filter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"li.search-reusables__primary-filter:nth-child(2) > button:nth-child(1)")))
people_filter.click()

all_filter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".search-reusables__all-filters-pill-button")))
all_filter.click()

check1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"li.search-reusables__secondary-filters-filter:nth-child(12) > fieldset:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > label:nth-child(2)")))
check1.click()
check2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"li.search-reusables__secondary-filters-filter:nth-child(12) > fieldset:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(3) > label:nth-child(2)")))
check2.click()

show_res = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"reusable-search-filters-buttons")))
show_res.send_keys(Keys.RETURN)

ul = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"reusable-search__entity-result-list")))
li = ul.find_elements(By.CLASS_NAME,"reusable-search__result-container")
prof = []
for i in li:
    profile_link = i.find_element(By.TAG_NAME, "a")
    prof.append(profile_link.get_attribute("href"))
    print(profile_link.get_attribute("href"))

image = []
for j in li:
    img = j.find_element(By.CLASS_NAME,"presence-entity__image")
    image.append(img.get_attribute("src"))

dict = {'profile links' : prof ,'image link': image}
dataframe = pd.DataFrame(dict)
dataframe.to_csv('profile.csv')



# driver.quit()







