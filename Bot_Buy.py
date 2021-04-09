from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome(executable_path=r"/home/anonymous/ChromeDriver")
site = "https://m.notebooksbilliger.de"

browser.get(site)