from locators.gp.gnb_locators import GNBLocators
from pages.BasePage import BasePage
from locators.gp.home_locators import HomePageLocators
from locators.gp.maintenance_locators import MaintenanceLocators
from selenium.webdriver.common.by import By


class HomePage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def open_home_page(self):
    self.open_url(HomePageLocators.PATH)

  def get_ci_screenshot(self):
    self.get_element_screenshot(HomePageLocators.MAIN_CI)

  def is_maintenance(self):
    return self.is_displayed(MaintenanceLocators.MAINTENANCE)
  
  def test(self):
    print(self.find_element(HomePageLocators.MAIN_CI))
    return self.find_element(HomePageLocators.MAIN_CI)
