#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
import random
from time import sleep


def sendText():
    for name in contact_names:
        user = driver.find_element_by_xpath(
            '//span[@title = "{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_class_name('_3FeAD')
        msg_box.send_keys(random.choice(msg))
        btn = driver.find_element_by_class_name('_3M-N-')
        btn.click()


def sendMedia():
    filepath = r'\path\to\your\media.jpg'
    for name in contact_names:
        user = driver.find_element_by_xpath(
            '//span[@title = "{}"]'.format(name))
        user.click()
        attach_btn = driver.find_element_by_xpath('//div[@title="Attach"]')
        attach_btn.click()

        photos_btn = driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        photos_btn.send_keys(filepath)

        sleep(2)

        send_btn = driver.find_element_by_xpath(
            '//span[@data-icon="send-light"]')
        send_btn.click()


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

# Extract all contacts names
contact_names = []
webElements = driver.find_elements_by_xpath("//span[@class='_19RFN']")
for name in webElements:
    contact_names.append(name.text)

msg = ["Hope you are doing well.",
       "I hope you have a good day.", "Greetings for the day."]

sleep(5)

sendText()
# sendMedia()
