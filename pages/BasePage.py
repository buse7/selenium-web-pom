import inspect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage():

  def __init__(self, driver):
    self.driver = driver

  def get_title(self):
    return self.driver.title

  def get_url(self):
    return self.driver.current_url

  def get_text(self, locator):
    return self.find_element(locator).text

  def get_href(self, locator):
    return self.find_element(locator).get_attribute('href')

  def open_url(self, path):
    self.driver.get(path)

  def get_cookie(self, key):
    return self.driver.get_cookie(key)

  def find_element(self, locator):
    return self.driver.find_element(locator[0], locator[1])

  def find_elements(self, *locator):
    return self.driver.find_elements(*locator)

  def get_element_screenshot(self, locator):
    el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    el.screenshot(f'./screenshots/{inspect.currentframe().f_back.f_code.co_name}.png')
  
  def click(self, locator):
    el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
    el.click()

  def double_click(self, locator):
    el = self.find_element(locator)
    action = ActionChains(self.driver)
    action.double_click(on_element=el)
    action.perform()

  def right_click(self, locator):
    el = self.find_element(locator)
    action = ActionChains(self.driver)
    action.context_click(on_element=el)
    action.perform()

  def send_keys(self, locator, input):
    self.find_element(locator).clear()
    self.find_element(locator).send_keys(input)

  def is_displayed(self, locator, timeout=0):
    if timeout > 0:
      try:
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
      except TimeoutException:
        return False
      else:
        return True
    else:
      try:
        return self.find_element(locator).is_displayed()
      except NoSuchElementException:
        return False

  def is_enable(self, locator):
    return self.find_element(locator).is_enabled()

  def is_selected(self, locator):
    return self.find_element(locator).is_selected()
