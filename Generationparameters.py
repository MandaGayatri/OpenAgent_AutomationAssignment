from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LoginPage import LoginPageFunction
from ExtractedFile import write_list_to_file

file_path = "output.txt"
def GenerationParametersFunction(driver):

    a = driver.find_element(By.XPATH, "//*[text() = ' 512x512']")
    b = driver.find_element(By.XPATH, "(//*[@data-toggle='tooltip'])[2]")
    c = driver.find_element(By.XPATH, "(//*[@data-toggle='tooltip'])[3]")
    d = driver.find_element(By.XPATH, "(//*[@data-toggle='tooltip'])[4]")
    g = driver.find_element(By.XPATH, "(//*[@data-toggle='tooltip'])[5]")

    print(a.text)
    print(b.text)
    print(c.text)
    print(d.text)
    print(g.text)
    links = ["Generate parameter function"," "]
    links.append(a.text)
    links.append(b.text)
    links.append(c.text)
    links.append(d.text)
    links.append(g.text)
    links.append(" ")
    write_list_to_file(file_path,links)


#driver = LoginPageFunction()
#GenerationParametersFunction(driver)







