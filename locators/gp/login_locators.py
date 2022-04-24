from selenium.webdriver.common.by import By

class LoginLocators:
  PATH = "https://login.webzen.com/"
  TITLE = (By.XPATH, "//div[@class='title inTit']//h2")
  ID_FIELD = (By.XPATH, "//input[@id='UserID']")
  ID_ERR_MSG = (By.XPATH, "//span[@data-valmsg-for='UserID']")
  ID_BTN_RESET = (By.XPATH, "//button[@class='frm-reset']")
  PASSWORD_FIELD = (By.XPATH, "//input[@id='Password']")
  PASSWORD_BTN_VISIBLE = (By.XPATH, "//button[@class='frm-pw']")
  PASSWORD_ERR_MSG = (By.XPATH, "//span[@data-valmsg-for='Password'")
