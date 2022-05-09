# Created by PyCharm
# Author: Chen
# Date: 2022.5.8
# Time: 下午 11:23
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

with open("./config.yaml", "r", encoding="utf-8") as stream:
    opt = yaml.safe_load(stream)
    opt = dict(opt)
browser = webdriver.Edge("webdrivers/msedgedriver.exe")
browser.get(opt["url"])
time.sleep(opt["login_buffer"])
element = browser.find_element(By.CLASS_NAME, "ppt_img_box")
element.click()
elements = browser.find_elements(By.CLASS_NAME, "swiper-no-swiping")
for element in elements:
    element.click()
    time.sleep(opt["watch_interval"])
browser.close()
