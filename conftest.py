import pytest
import parser
import allure
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# get console parameter
def pytest_addoption(parser):
	parser.addoption("--browser", action="store", dest="browsers", default="chrome", help="Browser Type")
	parser.addoption("--id", action="store", default="", help="id")
	parser.addoption("--password", action="store", default="", help="password")

# multi browser parsing
def pytest_generate_tests(metafunc):
	if 'browser' in metafunc.fixturenames:
		metafunc.parametrize(
			"browser", metafunc.config.option.browsers.split(','), scope='session')


@pytest.fixture(scope='class')
def init_driver(request):
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.implicitly_wait(5)
  request.cls.driver = driver

  driver.maximize_window()

  yield
  driver.close()

# screenshot method
@pytest.fixture(scope="session")
def captureScreenshot(self, e):
	tb = sys.exc_info()[2]
	allure.attach(self.driver.get_screenshot_as_png(
	), name=e.__class__.__name__+", line : "+str(tb.tb_lineno), attachment_type=allure.attachment_type.PNG)













