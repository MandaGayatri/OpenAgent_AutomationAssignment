from UserName import UserNameFunction
from LoginPage import LoginPageFunction

def test_UserNameFunction():
    driver = LoginPageFunction()
    name = UserNameFunction(driver)
    print(name)