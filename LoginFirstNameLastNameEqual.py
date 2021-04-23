from selenium import webdriver
import re
import random
import string
from string import printable
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.phptravels.net/register')
driver.maximize_window()

# first name
FirstName = driver.find_element_by_name('firstname') #get first name element by name
randFN = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 7)) #genereate random string of upper and lower letters
FirstName.send_keys(randFN) #enter the random string in first name
FirstName.get_attribute('value')

# last name
LastName = driver.find_element_by_name('lastname') #get last name element by name
LastName.send_keys(randFN) #enter same string of first name in last name
LastName.get_attribute('value')

# phone number
phone = driver.find_element_by_name('phone') #get phone element by name
randNo = str(random.randint(1000000, 9999999)) #generate random phone number
phone.send_keys(randNo)
phone.get_attribute('value')


# email
email = driver.find_element_by_name('email') #get email element by name
randmail = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)) #generate random string of 7 digits
email.send_keys(randmail+''+'@gmail.com') #concatenate the string with @gmail.com
email.get_attribute('value')

# password
password = driver.find_element_by_name('password') #get password element by name
randPass = ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k = 7)) #generate random string of 7 digits
password.send_keys(randPass) #enter password in text field
passvalue = password.get_attribute('value')

# confirm password
confirmpassword = driver.find_element_by_name('confirmpassword')
confirmpassword.send_keys(randPass) #enter the same password entered before in password text field

time.sleep(5) #sleep before submit

#submit
submit = driver.find_element_by_xpath('/html/body/div[2]/div[1]/section/div/div/div[2]/div/form/div[8]/button')
submit.click()

time.sleep(15)

#if the image in the page appears after submit successfully appears, take screenshot
if driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[1]/div/div[1]/img'):
    driver.save_screenshot('failed_first_name_and_last_name_are_equal.png')

# write in execution report, that this test case failed
f = open('LoginFirstNameLastNameEqual.txt' , 'w')
f.write('LoginFirstNameLastNameEqual' +'\n')
f.write('Failed Test Case.')