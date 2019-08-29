from django.test import TestCase
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://futerovka.by')
assert 'Django' in browser.title

# Create your tests here.
