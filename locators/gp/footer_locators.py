from selenium.webdriver.common.by import By

class FooterLocators:
  FOOTER = (By.XPATH, "//footer")
  ABOUT = (By.XPATH, "//p[@class='footer-menu']/a[.='About WEBZEN')]")
  KR_PORTAL = (By.XPATH, "//p[@class='footer-menu']/a[.='Korean Game Portal')]")
  IP_LIST = (By.XPATH, "//p[@class='footer-menu']/a[.='IP Franchising List')]")
  PARTNERSHIP = (By.XPATH, "//p[@class='footer-menu']/a[.='Business Partnership')]")
  PRIVACY_POLICY = (By.XPATH, "//p[@class='footer-menu']/a[.='Privacy Policy')]")
  TERMS = (By.XPATH, "//p[@class='footer-menu']/a[.='Terms of Service')]") 
  EULA = (By.XPATH, "//p[@class='footer-menu']/a[.='EULA')]")
  LANGUAGE = (By.XPATH, "//a[@class='language']")
  TIME_SERVER = (By.XPATH, "//aside[@class='time']/p/strong[.='Server')]")
  TIME_LOCAL = (By.XPATH, "//aside[@class='time']/p/strong[.='Local')]")
  COPYRIGHT = (By.XPATH, "//address[@class='copyright']")
  CI = (By.XPATH, "//h1/a[@class='nav-caller']")