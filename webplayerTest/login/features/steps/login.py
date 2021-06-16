from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('website "{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.get("http://10.110.51.15/player/")