import pytest
import time
import allure
from pages.gp.LoginPage import LoginPage
from pages.gp.GNB import GNB
from tests.test_base import BaseTest

class TestLogin(BaseTest):

  @allure.step
  def test_page_load(self):
    home_page = LoginPage(self.driver)
    home_page.open_home_page()
    assert 'WEBZEN | Free to Play MMORPG Portal' in home_page.get_title()

  @allure.step
  #@pytest.mark.skip('skip test')
  def test_something(self):
    home_page = LoginPage(self.driver)
    assert 'asdasd' in home_page.get_title()
      