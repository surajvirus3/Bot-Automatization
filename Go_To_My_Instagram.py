from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to chromedriver.exe
path = r"H:\Code\GitHub_Repos\Bot_Code\chromedriver.exe"

# Initialize the browser
browser = webdriver.Chrome(executable_path=path)

# Startup page
site = "https://www.google.com"
browser.get(site)

# Accept cookies
browser.find_element_by_xpath('//*[@id="zV9nZe"]/div').click()

# Select search bar
searchbar = browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# Search google
search = "python_genius"

searchbar.click()
searchbar.send_keys(search)
searchbar.send_keys("\n")

# Click on Instagram link and accept cookies
browser.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/a/h3').click()
browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()


""" - Sites: - 

https://m.notebooksbilliger.de
https://www.mediamarkt.de
https://www.saturn.de
Amazon.de
Otto.de
https://www.caseking.de/pc-komponenten/grafikkarten/nvidia
"""