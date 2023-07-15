import os.path
import time
from selenium import webdriver
from selene import browser
from tests.conftest import tmp_directory_path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
def test_download_file_browser(tmp_directory):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": tmp_directory_path,
        "download.prompt_for_download": False
}
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)
    assert os.path.exists(os.path.join(tmp_directory_path, 'pytest-main.zip'))
