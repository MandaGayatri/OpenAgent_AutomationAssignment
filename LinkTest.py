from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LoginPage import LoginPageFunction
from ExtractedFile import write_list_to_file

file_path = "output.txt"
def LinkTestFunction(driver):
    links =[]
    links.append("Link Function")
    links.append("  ")
    image_elements = driver.find_elements(By.XPATH, "//img")
    for ele in image_elements:
        x = ele.get_attribute("src")
        print(x)
        links.append(x)
    links.append("  ")
    links.append("  ")
    links.append("  ")

    write_list_to_file(file_path, links)


#driver = LoginPageFunction()
#LinkTestFunction(driver)