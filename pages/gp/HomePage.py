from locators.gp.gnb_locators import GNBLocators
from pages.BasePage import BasePage
from locators.gp.home_locators import HomePageLocators
from locators.gp.maintenance_locators import MaintenanceLocators

class HomePage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def open_home_page(self):
    self.open_url(HomePageLocators.PATH)

  def is_maintenance(self):
    return self.is_displayed(MaintenanceLocators.MAINTENANCE)
  
  def is_visible_line_up(self):
    return self.is_displayed(HomePageLocators.LINEUP)

  def is_visible_main_banner(self):
    return self.is_displayed(HomePageLocators.MAIN_BANNER)

# method

