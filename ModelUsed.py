
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LoginPage import LoginPageFunction
from ExtractedFile import write_list_to_file

file_path = "output.txt"
def ModelUsedFunction(driver):
    f = driver.find_element(By.XPATH, "//*[contains(@href,'openjourney--4-prompts')]")
    print(f.text)
    l = []
    l.append("Model Used Functions")
    l.append(" ")
    l.append(f.text)
    l.append(" ")
    l.append(" ")
    write_list_to_file(file_path,l)


#driver = LoginPageFunction()
#ModelUsedFunction(driver)







