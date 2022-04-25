from pages.BasePage import BasePage
from locators.gp.login_locators import LoginLocators
from locators.gp.maintenance_locators import MaintenanceLocators

class LoginPage(BasePage):

  def __init__(self, driver):
      super().__init__(driver)

  # login page open

  def open_login_page(self):
    self.open_url(LoginLocators.PATH)

  # ui check

  def is_visible_id_field(self):
    return self.is_displayed(LoginLocators.ID_FIELD)

  def is_visible_id_err_msg(self):
    return self.is_displayed(LoginLocators.ID_ERR_MSG)
  
  def is_visible_password_field(self):
    return self.is_displayed(LoginLocators.PASSWORD_FIELD)

  def is_visible_password_err_msg(self):
    return self.is_displayed(LoginLocators.PASSWORD_ERR_MSG) 

  def is_visible_news_letter_btn(self):
    return self.is_displayed(LoginLocators.NEWS_CHK_BTN)
    
  def is_visible_login_btn(self):
    return self.is_displayed(LoginLocators.LOGIN_BTN)

  def is_visible_facebook_btn(self):
    return self.is_displayed(LoginLocators.FACEBOOK_BTN)
    
  def is_visible_google_btn(self):
    return self.is_displayed(LoginLocators.GOOGLE_BTN)

  def is_visible_recover_account(self):
    return self.is_displayed(LoginLocators.RECOVER_ACC)
    
  def is_visible_create_account(self):  
    return self.is_displayed(LoginLocators.CREATE_ACC)
  
  def is_visible_update_account(self):  
    return self.is_displayed(LoginLocators.UPDATE_ACC)

  # get err msg
  def get_password_err_msg(self):
    return self.get_text(LoginLocators.PASSWORD_ERR_MSG)
  
  def get_id_err_msg(self):
    return self.get_text(LoginLocators.ID_ERR_MSG)

  # maintenance check

  def is_maintenance(self):
    return self.is_displayed(MaintenanceLocators.MAINTENANCE)

  # set id

  def set_id(self, id):
    self.find_element(LoginLocators.ID_FIELD).clear()
    self.find_element(LoginLocators.ID_FIELD).send_keys(id)

  # set password
  
  def set_password(self, password):
    self.find_element(LoginLocators.PASSWORD_FIELD).clear()
    self.find_element(LoginLocators.PASSWORD_FIELD).send_keys(password)

  # login btn click
  def click_login_btn(self):
    self.find_element(LoginLocators.LOGIN_BTN).click()

  # login method

  def login(self, id, password):
    self.set_id(id)
    self.set_password(password)
    self.find_element(LoginLocators.LOGIN_BTN).click()
