import allure
from pages.gp.LoginPage import LoginPage
from pages.gp.GNB import GNB
from tests.test_base import BaseTest
from locators.gp.maintenance_locators import MaintenanceLocators

@allure.feature("Test Login Page")
class TestLogin(BaseTest):

  @allure.story('Test Page Open')
  def test_login_page_load(self):
    login_page = LoginPage(self.driver)
    login_page.open_login_page()
    assert 'login.webzen.com' in login_page.get_url()

  @allure.story('UI Loading Check') 
  def test_login_page_ui_loaded(self):
    login_page = LoginPage(self.driver)

    with allure.step('Step 1 - ID field check'):
      assert login_page.is_visible_id_field()
    with allure.step('Step 2 - Password field check'):
      assert login_page.is_visible_password_field()
    with allure.step('Step 3 - News Letter btn cehck'):
      assert login_page.is_visible_news_letter_btn()
    with allure.step('Step 4 - Login btn check'):
      assert login_page.is_visible_login_btn()
    with allure.step('Step 5 - Facebook btn check'):
      assert login_page.is_visible_facebook_btn()
    with allure.step('Step 6 - Google btn check'):
      assert login_page.is_visible_google_btn()
    with allure.step('Step 7 - Recover Account btn check'):
      assert login_page.is_visible_recover_account()
    with allure.step('Step 8 - Create Account btn check'):
      assert login_page.is_visible_create_account()
    with allure.step('Step 9 - Update Account btn check'):
      assert login_page.is_visible_update_account()
  
  @allure.story('Invalid Login Check')
  def test_invalid_login(self, id):
    login_page = LoginPage(self.driver)

    expect_err_msg = "We couldn't match the entered username or password to a webzen.com account."

    login_page.set_id(id)
    login_page.set_password('invalid')
    login_page.click_login_btn()

    with allure.step('Step 1  - Password Error msg check'):
      assert login_page.is_visible_password_err_msg()
    with allure.step('Step 2 - Error msg validation'):
      assert expect_err_msg == login_page.get_password_err_msg()
    
  @allure.story('Valid Login Check')
  def test_valid_login(self, id, password):
    login_page = LoginPage(self.driver)

    expect_title = "WEBZEN | Free to Play MMORPG Portal"

    login_page.login(id, password)

    with allure.step('Step 1 - Page redirect check'):
      assert expect_title == login_page.get_title()
    with allure.step('Step 2 - Auth Token Check'):
      cookie = login_page.get_cookie('WZ_AUTH')
      assert len(cookie) > 0


