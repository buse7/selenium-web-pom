import pytest
import allure
from pages.gp.HomePage import HomePage
from pages.gp.GNB import GNB
from pages.gp.Footer import Footer
from tests.test_base import BaseTest

@allure.feature("Test Home Page")
class TestHome(BaseTest):

  @allure.story('test open home page')
  @pytest.mark.gp
  def test_page_load(self):
    home_page = HomePage(self.driver)
    home_page.open_home_page()
    assert 'WEBZEN | Free to Play MMORPG Portal' in home_page.get_title()

  @allure.step
  @pytest.mark.gp
  def test_something(self):
    home_page = HomePage(self.driver)
    assert 'asdasd' in home_page.get_title()

  @allure.step
  @pytest.mark.gp
  def test_bi_click(self):
    home_page = HomePage(self.driver)
    gnb= GNB(self.driver)
    home_page.open_home_page()
    # home_page.test()
    home_page.is_maintenance()
    # gnb.click_nav_games()
    # print(gnb.get_games_layer_title())
      