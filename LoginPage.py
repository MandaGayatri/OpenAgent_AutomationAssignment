from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def LoginPageFunction():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://prompthero.com/")
    time.sleep(2)

    driver.find_element(By.XPATH, "(//a[text() = 'Log in'])[1]").click()
    time.sleep(2)

    email_input = driver.find_element(By.XPATH, "//input[@type = 'email']")
    email_input.send_keys("gayatri.manda2199@gmail.com")
    time.sleep(2)

    password_input = driver.find_element(By.XPATH, "//input[@type = 'password']")
    password_input.send_keys("RAMAdevi@1")
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, "//input[@value = 'Log in']")
    login_button.click()
    time.sleep(5)

    search_input = driver.find_element(By.XPATH, "(//*[@type = 'text'])[2]")
    search_input.send_keys("darkness,scary,atmospheric")
    time.sleep(2)

    search_button = driver.find_element(By.XPATH, "//*[text() = 'Search']")
    search_button.submit()
    time.sleep(4)

    image_link = driver.find_element(By.XPATH,
                                     "(//*[@id='prompt-card-image-backdrop-4ae9caa7ad7'])[2]")
    image_link.click()
    time.sleep(5)
    return driver
