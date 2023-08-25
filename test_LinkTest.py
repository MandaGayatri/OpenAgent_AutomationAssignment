from LinkTest import LinkTestFunction

from LoginPage import LoginPageFunction

def test_LinkTestFunction():
    driver = LoginPageFunction()
    links = LinkTestFunction(driver)
    print(links)

