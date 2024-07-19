import pytest
from data.data import Urls
from selenium import webdriver
from data.helpers import Generators
import requests


@pytest.fixture(scope='function', params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=firefox_options)
    elif request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def create_and_delete_user():
    payload = Generators.generate_registration_user_data()
    response = requests.post(f'{Urls.BASE_URL}api/auth/register', data=payload)
    yield response, payload
    access_token = response.json()['accessToken']
    requests.delete(f'{Urls.BASE_URL}api/auth/user', headers={'Authorization': access_token})
