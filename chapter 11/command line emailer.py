'''
command line emailer

take in an email address and string of text on cmd line
use selenium to log into your account and send an email 
to the provided address


'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, re, sys,time
user = "yourEmailAddress@yourMailHost.com"
password = 'CLASSIFIED_TEXT_****area51****_CLASSIFIED_TEXT'


def sendAnEmail():
    # get email addr
    to_email = sys.argv[1]
    # get text
    text = " ".join(sys.argv[2:])

    # log into your account
    url = "https://accounts.google.com/ServiceLogin"
    browser = webdriver.Firefox()
    browser.get(url)

    emailElements = browser.find_element_by_id("Email")
    emailElements.send_keys(user)
    browser.find_element_by_id("next").click()

    time.sleep(1)
    passwordElements = browser.find_element_by_id("Passwd")
    passwordElements.send_keys(password)
    browser.find_element_by_id("signIn").click()

    # send text as mail to given email id
    browser.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    time.sleep(2)
    browser.find_element_by_xpath("//textarea[@aria-label='To']").send_keys(ToEmail)
    time.sleep(2)
    browser.find_element_by_xpath("//input[@aria-label='Subject']").send_keys("Hi!")
    time.sleep(10)
    browser.find_element_by_xpath("//div[@aria-label='Message Body']").send_keys(text)
    time.sleep(5)
    browser.find_element_by_xpath("//div[contains(text(), 'Send')]").click()

sendAnEmail()