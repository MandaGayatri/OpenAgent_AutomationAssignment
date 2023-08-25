from ModelUsed import ModelUsedFunction
from LoginPage import LoginPageFunction

def test_ModelUsedFunction():
    driver = LoginPageFunction()
    modelParameters = ModelUsedFunction(driver)
    print(modelParameters)