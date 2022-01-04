from selenium.webdriver.common.by import By

class GNBLocators:
  GNB = (By.XPATH, "//header[@class='global-header-container']")
  BI = (By.XPATH, "//h1/a[@class='nav-caller']")
  GAMES = (By.XPATH, "//menu//li[@class='games']")
  GAMES_LAYER = (By.XPATH, "//menu//li[@class='games']//div[@class='games-layer']")
  GAMES_LAYER_TITLE = (By.XPATH, f"{GAMES_LAYER[1]}//strong")
  GAMES_LAYER_GAMELIST = (By.XPATH, f"{GAMES_LAYER[1]}//child::div[@class='slider']//a")
  GAMES_LAYER_PAGE = (By.XPATH, f"{GAMES_LAYER[1]}//child::div[@class='bx-pager-item']")
  TOPUP = (By.XPATH, "//menu//li[@class='wcoin']")
  SUPPORT = (By.XPATH, "//menu//li[@class='support']")
  LOGIN = (By.XPATH, "//menu//li[@class='sign']")
  REGISTER = (By.XPATH, "//menu//li[@class='sign-up']")