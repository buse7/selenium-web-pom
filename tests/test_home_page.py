import pytest
import time
from pages.HomePage import HomePage
from pages.GNB import GNB
from tests.test_base import BaseTest

class TestHome(BaseTest):

  def test_page_load(self):
    home_page = HomePage(self.driver)
    home_page.open_home_page()
    assert 'WEBZEN | Free to Play MMORPG Portal' in home_page.get_title()

  def test_bi_click(self):
    home_page = HomePage(self.driver)
    gnb= GNB(self.driver)
    home_page.open_home_page()
    # home_page.test()
    home_page.is_maintenance()
    # gnb.click_nav_games()
    # print(gnb.get_games_layer_title())
      