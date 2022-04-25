import pytest
import allure
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# get config 
with open('config.json', 'r') as cf:
  config = json.load(cf)
account = config['ACCOUNT']

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
def selenium_driver(request):
  chrome_options = webdriver.ChromeOptions()
  #chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
  driver.implicitly_wait(5)
  request.cls.driver = driver

  driver.maximize_window()

  yield driver
  driver.quit()

# id args
@pytest.fixture(scope='session')
def id(request):
	return request.config.getoption("--id") if request.config.getoption("--id") else config["ACCOUNT"]["Default"]["id"]

# password args
@pytest.fixture(scope='session')
def password(request):
	return request.config.getoption("--password") if request.config.getoption("--password") else config["ACCOUNT"]["Default"]["pwd"]


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['selenium_driver']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)

# attach screenshot to allure
def take_screenshot(driver, nodeid):
  test_case_name = re.sub(pattern=r'::|\[', repl='_', string=re.sub(pattern=r'/', repl='_', string=re.sub(pattern=r'https?://|\]', repl='', string=nodeid)))
  allure.attach(driver.get_screenshot_as_png(), name=f'{test_case_name}', attachment_type=allure.attachment_type.PNG)  