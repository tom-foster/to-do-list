#Created first function test in python.
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")
#Makes a test assertion (assumption) that Django should be listed in the title
assert 'Django' in browser.title
