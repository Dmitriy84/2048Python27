'''
Created on Jun 20, 2015

@author: dimon24
'''
from random import randint

from lettuce import step, world
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


criteria = ''
def is_game_over(criteria):
    try:
        world.browser.find_element_by_xpath(world.current_page["is_game_over"](criteria))
        return True
    except NoSuchElementException:
        return False

@step(r'Open "(.*)" page')
def should_open_main_page(step, page):
    world.current_page = world.mapping[page]
    world.browser.get(world.current_page['url'])

@step("Stop playing criteria is '(.*)'")
def stop_plaing_criteria(step, text):
    global criteria
    criteria = text

@step("Start random play with '(.*)' keys")
def start_random_play_with_keys(step, keys):
    keys = keys.split(",")
    while not is_game_over(criteria):
        key = keys[randint(0, len(keys) - 1)].strip()
        print "... sending key: " + key
        world.browser.find_element_by_xpath(world.current_page["body"]).send_keys(getattr(Keys, key))
        cells = [world.current_page["number_in_cell"](column, row) for row in range(1, 5) for column in range(1, 5)]
        for line in ("current state: ", cells[:4], cells[4:8], cells[8:12], cells[12:]):
            print line

@step("Show scores")
def show_scores(step):
    print "FINAL SCORES: " + world.browser.find_element_by_xpath(world.current_page["score"]).text.split()[0]