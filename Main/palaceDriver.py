from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Main.items import category


def palaceDriver():

    # Intializes the web driver
    driver = webdriver.Firefox()

    #goes to supreme new york
    driver.get("https://shop-usa.palaceskateboards.com/")

    products = driver.find_elements_by_class_name("title")
    for i in range(len(products)):
        print(products[i].text)




palaceDriver()
