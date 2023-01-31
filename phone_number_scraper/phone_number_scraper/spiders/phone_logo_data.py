from selenium import webdriver
import re


driver = webdriver.Chrome()
driver.get('https://www.mossyford.com/')
doc = driver.page_source

phones = re.findall(r'[(][\d]{3}[)]\s[\d]{3}-[\d]{4}', doc)

for phone in phones:
    print(phone)
