from Generationparameters import GenerationParametersFunction
from LoginPage import LoginPageFunction

def test_GenerationParametersFunction():
    driver = LoginPageFunction()
    parameters = GenerationParametersFunction(driver)
    print(parameters)
