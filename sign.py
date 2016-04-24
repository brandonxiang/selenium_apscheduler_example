# -*- coding:utf-8 -*-
from selenium import webdriver
from apscheduler.schedulers.background import BackgroundScheduler
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import time

# 登陆


def login():
    browser = webdriver.Firefox()
    browser.get("http://XX.XX.com/")
    browser.find_element_by_id("InputName").send_keys('XXX'.decode('utf8'))
    browser.find_element_by_id("InputPassword").send_keys("XXX")
    browser.find_element_by_tag_name("button").click()
    return browser


def click_event(browser, btnName):
    WebDriverWait(browser, 10).until(EC.title_contains("系统".decode('utf8')))
    browser.switch_to_frame("ifm")
    browser.find_element_by_id(btnName).click()
    print '[' + time.strftime('%Y-%m-%d %X', time.localtime(time.time())) + '] : ' + btnName + ' has been done!!!'

schedular = BackgroundScheduler()

# 上午8：58


@schedular.scheduled_job('cron', day_of_week='mon-fri', hour=8, minute=58)
def MorningOn():
    logging.basicConfig()
    driver = login()
    click_event(driver, "btnMOn")


# 上午12：02
@schedular.scheduled_job('cron', day_of_week='mon-fri', hour=12, minute=2)
def MorningOff():
    logging.basicConfig()
    driver = login()
    click_event(driver, "btnMOff")

# 下午13：58


@schedular.scheduled_job('cron', day_of_week='mon-fri', hour=13, minute=58)
def AfternoonOn():
    logging.basicConfig()
    driver = login()
    click_event(driver, "btnNOn")

# 下午18：02


@schedular.scheduled_job('cron', day_of_week='mon-fri', hour=18, minute=2)
def AfternoonOff():
    logging.basicConfig()
    driver = login()
    click_event(driver, "btnNOff")

schedular.start()
os.system('pause')
