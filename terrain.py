'''
Created on Jun 20, 2015

@author: dimon24
'''
from lettuce import before, after, world
from selenium import webdriver
from mapping import site_mapping


@before.each_feature
def setup(server):
    world.browser = webdriver.Firefox()
    world.mapping = site_mapping


@after.all
def tear_down(total):
    world.browser.close()