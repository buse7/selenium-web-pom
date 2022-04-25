from selenium.webdriver.common.by import By

class HomePageLocators:
  PATH = "https://www.webzen.com/"
  MAIN_CI = (By.XPATH, "//article[@class='main-roll-banner']//child::em//img")
  MENU = (By.XPATH, "//menu//li")
  LINEUP = (By.XPATH, "//section[@class='line-up']")
  LINEUP_TAB = (By.XPATH, f"{LINEUP[1]}//nav[@class='tab']")
  LINEUP_LIST = (By.XPATH, f"{LINEUP[1]}//ul")
  LINEUP_ITEM = (By. XPATH, f"{LINEUP_LIST[1]}//li")
  MAIN_BANNER = (By. XPATH, "//artical[@class='main-roll-banner']")
  