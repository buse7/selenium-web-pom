from selenium.webdriver.common.by import By

class FooterLocators:
  FOOTER = (By.XPATH, "//footer")
  ABOUT = (By.XPATH, "//p[@class='footer-menu']/a[contains(text(), 'About WEBZEN')]")
  KR_PORTAL = (By.XPATH, "//p[@class='footer-menu']/a[contains(text(), 'Korean Game Portal')]")
  IP_LIST = (By.XPATH, "//p[@class='footer-menu']/a[contains(text(), 'IP Franchising List')]")
  PARTNERSHIP = (By.XPATH, "//p[@class='footer-menu']/a[contains(text(), 'Business Partnership')]")
  PRIVACY_POLICY = (By.XPATH, "//p[@class='footer-menu']/a[contains(text(), 'Privacy Policy')]")
  TERMS = (By.XPATH, "//p[@class='footer-menu']/a[contains(text(), 'Terms of Service')]") 
  EULA = (By.XPATH, "//p[@class='footer-menu']/a[contains(text(), 'EULA')]")
  LANGUAGE = (By.XPATH, "//a[@class='language']")
  TIME_SERVER = (By.XPATH, "//aside[@class='time']/p/strong[contains(text(), 'Server')]")
  TIME_LOCAL = (By.XPATH, "//aside[@class='time']/p/strong[contains(text(), 'Local')]")
  COPYRIGHT = (By.XPATH, "//address[@class='copyright']")
  CI = (By.XPATH, "//h1/a[@class='nav-caller']")