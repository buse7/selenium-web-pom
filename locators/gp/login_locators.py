from selenium.webdriver.common.by import By

class LoginLocators:
  PATH = "https://login.webzen.com/"
  TITLE = (By.XPATH, "//div[@class='title inTit']//h2")
  ID_FIELD = (By.XPATH, "//input[@id='UserID']")
  ID_ERR_MSG = (By.XPATH, "//span[@data-valmsg-for='UserID']")
  ID_BTN_RESET = (By.XPATH, "//button[@class='frm-reset']")
  PASSWORD_FIELD = (By.XPATH, "//input[@id='Password']")
  PASSWORD_BTN_VISIBLE = (By.XPATH, "//button[@class='frm-pw']")
  PASSWORD_ERR_MSG = (By.XPATH, "//span[@data-valmsg-for='Password']")
  LOGIN_BTN = (By.XPATH, "//div[@class='btn-auth']")
  NEWS_CHK_BTN = (By.XPATH, "//span[@class='chkbox']")
  FACEBOOK_BTN = (By.XPATH, "//div[@class='btn-auth double']//a[@class='btn-type btn-facebook']")
  GOOGLE_BTN = (By.XPATH, "//div[@class='btn-auth double']//a[@class='btn-type btn-google']")
  RECOVER_ACC = (By.XPATH, "//a[contains(text(), 'Recover Account')]")
  CREATE_ACC = (By.XPATH, "//a[contains(text(), 'Create Account')]")
  UPDATE_ACC = (By.XPATH, "//a[contains(text(), 'Update Your Account')]")
