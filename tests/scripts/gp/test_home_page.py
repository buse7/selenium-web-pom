import pytest
import allure
from pages.gp.HomePage import HomePage
from pages.gp.GNB import GNB
from pages.gp.Footer import Footer
from tests.test_base import BaseTest

@allure.feature("Test Home Page")
class TestHome(BaseTest):

  @allure.story('Test Home Page Open')
  @pytest.mark.gp
  def test_page_load(self):
    home_page = HomePage(self.driver)
    home_page.open_home_page()
    assert 'WEBZEN | Free to Play MMORPG Portal' in home_page.get_title()

  @allure.story('Test UI Loading')
  @pytest.mark.gp
  def test_main_page_ui_loaded(self):
    home_page = HomePage(self.driver)
    home_page.open_home_page()

    with allure.step('Step 1 - GNB check'):
      assert GNB(self.driver).is_visible_gnb()
    with allure.step('Step 2 - Main Banner check'):
      assert home_page.is_visible_main_banner()
    with allure.step('Step 3 - Line Up cehck'):
      assert home_page.is_visible_line_up()
    with allure.step('Step 4 - Footer check'):
      assert Footer(self.driver).is_visible_footer()

