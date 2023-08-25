from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from ExtractedFile import write_list_to_file

file_path = "output.txt"
def UserNameFunction(driver):


    user_picture_icon = driver.find_element(By.XPATH, "//img[@class  = 'user-picture-icon']")
    user_picture_icon.click()
    time.sleep(2)

    user_profile_name = driver.find_element(By.XPATH, "//*[@class = 'user-profile-pic']//following::h1[1]")
    time.sleep(2)
    print(user_profile_name.text)
    l = ["UserName Function"," ",user_profile_name.text]
    write_list_to_file(file_path, l)

    driver.close()



#from LoginPage import LoginPageFunction
#driver = LoginPageFunction()
#UserNameFunction(driver)



