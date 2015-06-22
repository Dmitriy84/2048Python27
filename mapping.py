'''
Created on Jun 20, 2015

@author: dimon24
'''
from lettuce import world
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


host_url = ""
class text_of_element_located(object):
    def __init__(self, locator):
        self.locator = locator
        self.value = ''
    def set_value(self, driver):
        try:
            self.value = driver.find_element_by_xpath(self.locator).text
        except NoSuchElementException:
            self.value = '0'
    def __call__(self, driver):
        try:
            self.set_value(driver)
        except StaleElementReferenceException:
            self.set_value(driver)
        return len(self.value) > 0

def number_in_cell(row, column):
    xpath = "//div[@class='tile-container']/div[contains(@class, 'tile-position-" + str(row) + "-" + str(column) + "')][last()]"
    try:
        el = text_of_element_located(xpath)
        WebDriverWait(world.browser, 2).until(el)
        return int(el.value)
    except TimeoutException:
        return 0

site_mapping = {
    "home": {
        "url": "http://gabrielecirulli.github.io/2048",
        "body": "//body",
        "number_in_cell": number_in_cell,
        "is_game_over": lambda text: "//div[@class='game-message game-over']/p[text()='" + str(text) + "']",
        "score":"//div[@class='score-container']"
    }
}