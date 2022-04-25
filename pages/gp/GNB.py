from pages.BasePage import BasePage
from locators.gp.gnb_locators import GNBLocators

class GNB(BasePage):

  def __init__(self, driver):
      super().__init__(driver)

  # gnb container

  def is_visible_gnb(self):
    return self.is_displayed(GNBLocators.GNB)

  def get_gnb_container(self):
    if self.is_displayed(GNBLocators.GNB, 10):
      return self.find_element(GNBLocators.GNB) 

  # ci

  def get_ci(self):
    if self.is_displayed(GNBLocators.CI, 10):
      return self.find_element(GNBLocators.CI)

  def click_ci(self):
    if self.is_displayed(GNBLocators.CI, 10):
      self.click(GNBLocators.CI)

  def get_ci_link(self):
    if self.is_displayed(GNBLocators.CI, 10):
      return self.get_href(GNBLocators.CI)

  # navigator
  # nav - games

  def get_nav_games(self):
    if self.is_displayed(GNBLocators.GAMES, 10):
      return self.find_element(GNBLocators.GAMES)
  
  def click_nav_games(self):
    if self.is_displayed(GNBLocators.GAMES, 10):
      self.click(GNBLocators.GAMES)

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

  def get_nav_topup_link(self):
    if self.is_displayed(GNBLocators.SUPPORT, 10):
      return self.get_href(GNBLocators.SUPPORT)

  # nav - support

  def get_nav_support(self):
    if self.is_displayed(GNBLocators.SUPPORT, 10):
      return self.find_element(GNBLocators.SUPPORT)

  def click_nav_support(self):
    if self.is_displayed(GNBLocators.SUPPORT, 10):
      self.click(GNBLocators.SUPPORT)

  def get_nav_support_link(self):
    if self.is_displayed(GNBLocators.SUPPORT, 10):
      return self.get_href(GNBLocators.SUPPORT)

  # nav - login

  def get_nav_login(self):
    if self.is_displayed(GNBLocators.LOGIN, 10):
      return self.find_element(GNBLocators.LOGIN)

  def click_nav_login(self):
    if self.is_displayed(GNBLocators.LOGIN, 10):
      self.click(GNBLocators.LOGIN)

  def get_nav_login_link(self):
    if self.is_displayed(GNBLocators.LOGIN, 10):
      return self.get_href(GNBLocators.LOGIN)

  # nav - register

  def get_nav_register(self):
    if self.is_displayed(GNBLocators.REGISTER, 10):
      return self.find_element(GNBLocators.REGISTER)

  def click_nav_register(self):
    if self.is_displayed(GNBLocators.REGISTER, 10):
      self.click(GNBLocators.REGISTER)
  
  def get_nav_register_link(self):
    if self.is_displayed(GNBLocators.REGISTER, 10):
      return self.get_href(GNBLocators.REGISTER)
