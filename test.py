
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox,Chrome 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import os
driver = webdriver.Firefox(executable_path='/usr/local/bin/chromedriver',service_log_path='usr/local/bin') 
