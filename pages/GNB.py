from pages.BasePage import BasePage
from locators.gnb_locators import GNBLocators

class GNB(BasePage):

  def __init__(self, driver):
      super().__init__(driver)

  # gnb container

  def is_visible_gnb(self):
    return self.is_displayed(GNBLocators.GNB)

  def get_gnb_container(self):
    if self.is_displayed(GNBLocators.GNB, 10):
      return self.find_element(GNBLocators.GNB) 

  # bi 

  def get_bi(self):
    if self.is_displayed(GNBLocators.BI, 10):
      return self.find_element(GNBLocators.BI)

  def get_bi_screenshot(self):
    if self.is_displayed(GNBLocators.BI, 10):
      self.get_element_screenshot(GNBLocators.BI)

  def click_bi(self):
    if self.is_displayed(GNBLocators.BI, 10):
      self.click(GNBLocators.BI)

  # navigator
  # nav - games

  def get_nav_games(self):
    if self.is_displayed(GNBLocators.GAMES, 10):
      return self.find_element(GNBLocators.GAMES)
  
  def click_nav_games(self):
    if self.is_displayed(GNBLocators.GAMES, 10):
      self.click(GNBLocators.GAMES)
  
  def get_nav_games_screenshot(self):
    if self.is_displayed(GNBLocators.GAMES, 10):
      self.get_element_screenshot(GNBLocators.GAMES)
  
  def get_nav_games_text(self):
    if self.is_displayed(GNBLocators.GAMES, 10):
      return self.get_text(GNBLocators.GAMES)

  # nav - games-layer
  
  def get_games_layer(self):
    if self.is_displayed(GNBLocators.GAMES_LAYER, 10):
      return self.find_element(GNBLocators.GAMES_LAYER)

  def get_games_layer_title(self):
    if self.is_displayed(GNBLocators.GAMES_LAYER, 10):
      return self.get_text(GNBLocators.GAMES_LAYER_TITLE)

  def get_games_layer_list(self):
    if self.is_displayed(GNBLocators.GAMES_LAYER, 10):
      return self.find_elements(*GNBLocators.GAMES_LAYER_GAMELIST)

  def click_games_layer_item(self, index):
    self.click_nav_games()
    if self.is_displayed(GNBLocators.GAMES_LAYER, 10):
      self.click(self.get_games_layer_list()[index])

  def get_games_layer_pages(self):
    if self.is_displayed(GNBLocators.GAMES_LAYER, 10):
      return self.find_elements(*GNBLocators.GAMES_LAYER_PAGE)

  def click_games_layer_page(self, index):
    self.click_nav_games()
    if self.is_displayed(GNBLocators.GAMES_LAYER, 10):
      self.click(self.get_games_layer_pages()[index])

  # nav - topup

  def get_nav_topup(self):
    if self.is_displayed(GNBLocators.TOPUP, 10):
      return self.find_element(GNBLocators.TOPUP)

  def click_nav_topup(self):
    if self.is_displayed(GNBLocators.TOPUP, 10):
      self.click(GNBLocators.TOPUP)
  
  def get_nav_topup_screenshot(self):
    if self.is_displayed(GNBLocators.TOPUP, 10):
      self.get_element_screenshot(GNBLocators.TOPUP)
  
  def get_nav_topup_text(self):
    if self.is_displayed(GNBLocators.TOPUP, 10):
      return self.get_text(GNBLocators.TOPUP)

  # nav - support

  def get_nav_support(self):
    if self.is_displayed(GNBLocators.SUPPORT, 10):
      return self.find_element(GNBLocators.SUPPORT)

  def click_nav_support(self):
    if self.is_displayed(GNBLocators.SUPPORT, 10):
      self.click(GNBLocators.SUPPORT)
  
  def get_nav_support_screenshot(self):
    if self.is_displayed(GNBLocators.SUPPORT, 10):
      self.get_element_screenshot(GNBLocators.SUPPORT)
  
  def get_nav_support_text(self):
    if self.is_displayed(GNBLocators.SUPPORT, 10):
      return self.get_text(GNBLocators.SUPPORT)

  # nav - login

  def get_nav_login(self):
    if self.is_displayed(GNBLocators.LOGIN, 10):
      return self.find_element(GNBLocators.LOGIN)

  def click_nav_login(self):
    if self.is_displayed(GNBLocators.LOGIN, 10):
      self.click(GNBLocators.LOGIN)
  
  def get_nav_login_screenshot(self):
    if self.is_displayed(GNBLocators.LOGIN, 10):
      self.get_element_screenshot(GNBLocators.LOGIN)
  
  def get_nav_login_text(self):
    if self.is_displayed(GNBLocators.LOGIN, 10):
      return self.get_text(GNBLocators.LOGIN)

  # nav - register

  def get_nav_register(self):
    if self.is_displayed(GNBLocators.REGISTER, 10):
      return self.find_element(GNBLocators.REGISTER)

  def click_nav_register(self):
    if self.is_displayed(GNBLocators.REGISTER, 10):
      self.click(GNBLocators.REGISTER)
  
  def get_nav_register_screenshot(self):
    if self.is_displayed(GNBLocators.REGISTER, 10):
      self.get_element_screenshot(GNBLocators.REGISTER)
  
  def get_nav_register_text(self):
    if self.is_displayed(GNBLocators.REGISTER, 10):
      return self.get_text(GNBLocators.REGISTER)
