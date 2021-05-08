# -*- coding: utf-8 -*-
"""
Created on Sat May  8 09:41:22 2021

@author: laria
"""

from selenium import webdriver

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
browser = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")

browser.get("http://localhost:8000")

assert 'Django' in browser.title