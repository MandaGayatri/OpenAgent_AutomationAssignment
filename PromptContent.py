from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ExtractedFile import write_list_to_file

file_path = "output.txt"
def PromptContentFunction(driver):

    keyword = "prompt"
    elements_with_keyword = driver.find_elements(By.XPATH, "//*[contains(text(), '" + keyword + "')]")
    l = []
    l.append("Prompt Content ")
    for element in elements_with_keyword:
        lines = element.text
        l.append(lines)
        print("Lines containing '" + keyword + "' are: " + lines)
    l.append(" ")
  
    write_list_to_file(file_path,l)


