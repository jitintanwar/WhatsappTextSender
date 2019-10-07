#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
import random

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

contact_names = ["contact1", "contact2", "contact3"]
msg = ["Hope you are doing well.",
       "I hope you have a good day.", "Greetings for the day."]


for name in contact_names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_3FeAD')
    msg_box.send_keys(random.choice(msg))
    btn = driver.find_element_by_class_name('_3M-N-')
    btn.click()
