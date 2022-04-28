import allure
import time
from pages.gp.LoginPage import LoginPage
from pages.gp.GNB import GNB
from tests.test_base import BaseTest
from locators.gp.maintenance_locators import MaintenanceLocators
from locators.gp.login_locators import LoginLocators
from locators.gp.recover_locators import RecoverLocators

@allure.feature("Test Login Page")
class TestLogin(BaseTest):

  @allure.story('Test Login Page Open')
  def test_login_page_load(self):
    login_page = LoginPage(self.driver)
    login_page.open_login_page()

    assert 'login.webzen.com' in login_page.get_url()

  @allure.story('Test UI Loading') 
  def test_login_page_ui_loaded(self):
    login_page = LoginPage(self.driver)
    login_page.open_login_page()

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
  
  @allure.story('Test Invalid Login')
  def test_invalid_login(self, id):
    login_page = LoginPage(self.driver)
    login_page.open_login_page()

    expect_err_msg = "We couldn't match the entered username or password to a webzen.com account."

    login_page.set_id(id)
    login_page.set_password('invalid')
    login_page.click_login_btn()

    with allure.step('Step 1  - Password Error msg check'):
      assert login_page.is_visible_password_err_msg()
    with allure.step('Step 2 - Error msg validation'):
      assert expect_err_msg == login_page.get_password_err_msg()
    
  @allure.story('Test Valid Login')
  def test_valid_login(self, id, password):
    login_page = LoginPage(self.driver)
    login_page.open_login_page()

    expect_title = "WEBZEN | Free to Play MMORPG Portal"

    login_page.login(id, password)

    with allure.step('Step 1 - Page redirect check'):
      assert expect_title == login_page.get_title()
    with allure.step('Step 2 - Auth Token Check'):
      cookie = login_page.get_cookie('WZ_AUTH')
      assert len(cookie) > 0
    
  @allure.story('Test Logout')
  def test_logout(self):
    gnb = GNB(self.driver)
    gnb.logout()
    with allure.step('Step 1 - Auth Token Delete Check'):
      cookie = gnb.get_cookie('WZ_AUTH')
      assert cookie is None

  @allure.story('Test Facebook Login Popup Open')
  def test_popup_facebook_login(self):
    login_page = LoginPage(self.driver)
    login_page.open_login_page()

    with allure.step('Step 1 - Click Facebook Login BTN'):
      login_page.click(LoginLocators.FACEBOOK_BTN)
    with allure.step('Step 2 - Wait Popup Facebook Login'):
      login_page.wait_new_window_open(10)
    with allure.step('Step 3 - Test Facebook Login Popup'):
      login_page.switch_window(1)
      assert 'Facebook' in login_page.get_title()
    with allure.step('Step 4 - Return Main Window'):
      login_page.driver.close()
      login_page.switch_window(0)

  @allure.story('Test Google Login Popup Open')
  def test_popup_google_login(self):
    login_page = LoginPage(self.driver)
    login_page.open_login_page()

    with allure.step('Step 1 - Click Google Login BTN'):
      login_page.click(LoginLocators.GOOGLE_BTN)
    with allure.step('Step 2 - Wait Popup Google Login'):
      login_page.wait_new_window_open(10)
    with allure.step('Step 3 - Test Google Login Popup'):
      login_page.switch_window(1)
      assert 'Google' in login_page.get_title()
    with allure.step('Step 4 - Return Main Window'):
      login_page.driver.close()
      login_page.switch_window(0)

  @allure.story('Test Recover Account Page Link')
  def test_link_recover_account_page(self):
    login_page = LoginPage(self.driver)
    login_page.open_login_page()
    
    with allure.step('Step 1 - Click Recover Account BTN'):
      login_page.click(LoginLocators.RECOVER_ACC)
    with allure.step('Step 2 - Test Move to Recover Account Page'):
      assert 'Recover Account Information' in login_page.get_text(RecoverLocators.TITLE)

