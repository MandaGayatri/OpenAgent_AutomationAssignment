from LoginPage import LoginPageFunction
from PromptContent import PromptContentFunction

def test_PromptContentFunction():

    driver = LoginPageFunction()
    content = PromptContentFunction(driver)
    print(content)