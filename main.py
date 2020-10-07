#read the 'read me' file to set up. 

from selenium import webdriver
import pyautogui as pg

driver = webdriver.Chrome()
driver.get('Enter website landing page you want chrome to open')

searchBoxUsername = driver.find_element_by_xpath('')
searchBoxUsername.send_keys('')

searchBoxPassword = driver.find_element_by_xpath('//*[@id="password"]')
searchBoxPassword.send_keys('')

searchButton = driver.find_element_by_xpath('//*[@id="skipToContent"]/form/div/div[4]/input[1]')
searchButton.click()

pg.moveTo(564, 371, 1) #these are the coordinates for your mouse to move to you.
pg.click(564, 371) #mouse will click once it gets there
