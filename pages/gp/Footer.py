from pages.BasePage import BasePage
from locators.gp.footer_locators import FooterLocators

class Footer(BasePage):

  def __init__(self, driver):
      super().__init__(driver)

  # Footer container

  def is_visible_footer(self):
    return self.is_displayed(FooterLocators.FOOTER)

  def get_footer_container(self):
    if self.is_displayed(FooterLocators.FOOTER, 10):
      return self.find_element(FooterLocators.FOOTER) 

  # ci 

  def get_ci(self):
    if self.is_displayed(FooterLocators.CI, 10):
      return self.find_element(FooterLocators.CI)

  def click_ci(self):
    if self.is_displayed(FooterLocators.CI, 10):
      self.click(FooterLocators.CI)

  # copyright

  def get_copyright(self):
    if self.is_displayed(FooterLocators.COPYRIGHT, 10):
      return self.find_element(FooterLocators.COPYRIGHT)

  def get_copyright_text(self):
    if self.is_displayed(FooterLocators.COPYRIGHT, 10):
      return self.get_text(FooterLocators.COPYRIGHT)

  # footer - menu
  # menu - about webzen

  def get_menu_about(self):
    if self.is_displayed(FooterLocators.ABOUT, 10):
      return self.find_element(FooterLocators.ABOUT)
  
  def click_menu_about(self):
    if self.is_displayed(FooterLocators.ABOUT, 10):
      self.click(FooterLocators.ABOUT)
  
  def get_menu_about_screenshot(self):
    if self.is_displayed(FooterLocators.ABOUT, 10):
      self.get_element_screenshot(FooterLocators.ABOUT)
  
  def get_menu_about_text(self):
    if self.is_displayed(FooterLocators.ABOUT, 10):
      return self.get_text(FooterLocators.ABOUT)

  # menu - korean portal
  
  def get_menu_kr_portal(self):
    if self.is_displayed(FooterLocators.KR_PORTAL, 10):
      return self.find_element(FooterLocators.KR_PORTAL)
  
  def click_menu_kr_portal(self):
    if self.is_displayed(FooterLocators.KR_PORTAL, 10):
      self.click(FooterLocators.KR_PORTAL)
  
  def get_menu_kr_portal_screenshot(self):
    if self.is_displayed(FooterLocators.KR_PORTAL, 10):
      self.get_element_screenshot(FooterLocators.KR_PORTAL)
  
  def get_menu_kr_portal_text(self):
    if self.is_displayed(FooterLocators.KR_PORTAL, 10):
      return self.get_text(FooterLocators.KR_PORTAL)


  # menu - ip list
  
  def get_menu_ip_list(self):
    if self.is_displayed(FooterLocators.IP_LIST, 10):
      return self.find_element(FooterLocators.IP_LIST)
  
  def click_menu_ip_list(self):
    if self.is_displayed(FooterLocators.IP_LIST, 10):
      self.click(FooterLocators.IP_LIST)
  
  def get_menu_ip_list_screenshot(self):
    if self.is_displayed(FooterLocators.IP_LIST, 10):
      self.get_element_screenshot(FooterLocators.IP_LIST)
  
  def get_menu_ip_list_text(self):
    if self.is_displayed(FooterLocators.IP_LIST, 10):
      return self.get_text(FooterLocators.IP_LIST)

  # menu - business partnership
  
  def get_menu_partnership(self):
    if self.is_displayed(FooterLocators.PARTNERSHIP, 10):
      return self.find_element(FooterLocators.PARTNERSHIP)
  
  def click_menu_partnership(self):
    if self.is_displayed(FooterLocators.PARTNERSHIP, 10):
      self.click(FooterLocators.PARTNERSHIP)
  
  def get_menu_partnership_screenshot(self):
    if self.is_displayed(FooterLocators.PARTNERSHIP, 10):
      self.get_element_screenshot(FooterLocators.PARTNERSHIP)
  
  def get_menu_partnership_text(self):
    if self.is_displayed(FooterLocators.PARTNERSHIP, 10):
      return self.get_text(FooterLocators.PARTNERSHIP)

  # menu - privacy policy
  
  def get_menu_privacy(self):
    if self.is_displayed(FooterLocators.PRIVACY_POLICY, 10):
      return self.find_element(FooterLocators.PRIVACY_POLICY)
  
  def click_menu_privacy(self):
    if self.is_displayed(FooterLocators.PRIVACY_POLICY, 10):
      self.click(FooterLocators.PRIVACY_POLICY)
  
  def get_menu_privacyscreenshot(self):
    if self.is_displayed(FooterLocators.PRIVACY_POLICY, 10):
      self.get_element_screenshot(FooterLocators.PRIVACY_POLICY)
  
  def get_menu_privacy_text(self):
    if self.is_displayed(FooterLocators.PRIVACY_POLICY, 10):
      return self.get_text(FooterLocators.PRIVACY_POLICY)


  # menu - terms of service
  
  def get_menu_terms(self):
    if self.is_displayed(FooterLocators.TERMS, 10):
      return self.find_element(FooterLocators.TERMS)
  
  def click_menu_terms(self):
    if self.is_displayed(FooterLocators.TERMS, 10):
      self.click(FooterLocators.TERMS)
  
  def get_menu_terms_screenshot(self):
    if self.is_displayed(FooterLocators.TERMS, 10):
      self.get_element_screenshot(FooterLocators.TERMS)
  
  def get_menu_terms_text(self):
    if self.is_displayed(FooterLocators.TERMS, 10):
      return self.get_text(FooterLocators.TERMS)

  # menu - EULA
  
  def get_menu_eula(self):
    if self.is_displayed(FooterLocators.EULA, 10):
      return self.find_element(FooterLocators.EULA)
  
  def click_menu_eula(self):
    if self.is_displayed(FooterLocators.EULA, 10):
      self.click(FooterLocators.EULA)
  
  def get_menu_eula_screenshot(self):
    if self.is_displayed(FooterLocators.EULA, 10):
      self.get_element_screenshot(FooterLocators.EULA)
  
  def get_menu_eula_text(self):
    if self.is_displayed(FooterLocators.EULA, 10):
      return self.get_text(FooterLocators.EULA)

  # time
  # time - server

  def get_time_server(self):
    if self.is_displayed(FooterLocators.TIME_SERVER, 10):
      return self.find_element(FooterLocators.TIME_SERVER)
  
  def get_time_server_screenshot(self):
    if self.is_displayed(FooterLocators.TIME_SERVER, 10):
      self.get_element_screenshot(FooterLocators.TIME_SERVER)  

# time - local

  def get_time_local(self):
    if self.is_displayed(FooterLocators.TIME_LOCAL, 10):
      return self.find_element(FooterLocators.TIME_LOCAL)
  
  def get_time_local_screenshot(self):
    if self.is_displayed(FooterLocators.TIME_LOCAL, 10):
      self.get_element_screenshot(FooterLocators.TIME_LOCAL)  

# language selector

  def get_language(self):
    if self.is_displayed(FooterLocators.LANGUAGE, 10):
      return self.find_element(FooterLocators.LANGUAGE)
  
  def get_language_screenshot(self):
    if self.is_displayed(FooterLocators.LANGUAGE, 10):
      self.get_element_screenshot(FooterLocators.LANGUAGE) 