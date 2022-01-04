from selenium.webdriver.common.by import By

class HomePageLocators:
  PATH = "https://www.webzen.com/"
  MAIN_CI = (By.XPATH, "//article[@class='main-roll-banner']//child::em//img")
  MENU = (By.XPATH, "//menu//li")