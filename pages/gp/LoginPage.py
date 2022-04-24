from pages.BasePage import BasePage
from locators.gp.login_locators import LoginLocators

class LoginPage(BasePage):

  def __init__(self, driver):
      super().__init__(driver)

  def open_login_page(self):
    self.open_url(LoginLocators.PATH)

  def test():
    return