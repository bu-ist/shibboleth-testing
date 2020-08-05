#!/usr/bin/env python3
#
# Use the following environment variables to determine what this will do
#
# SHIB_HOST
# SHIB_USER
# SHIB_PASSWORD
#
import os

# ####
# Determine our landscape first and use that to determine the appropriate defaults
landscape = os.environ.get('LANDSCAPE', 'prod')
default_sp_is_verify = True
if landscape == 'syst':
    #default_sp = 'http://ist-shib-verify-syst.bu.edu/shibboleth'
    default_sp = 'bostonuniversity.policytech.com'
    #default_sp = 'https://learn.bu.edu/shibboleth-sp'
    default_host = "shib-syst.bu.edu"
    default_sp_is_verify = False
elif landscape == 'test':
    default_sp = 'http://ist-shib-verify-syst.bu.edu/shibboleth'
    default_host = "shib-test.bu.edu"
elif landscape == 'prod':
    default_sp = 'http://ist-shib-verify-prod.bu.edu/shibboleth'
    default_host = 'shib.bu.edu'
else:
    default_sp = 'http://ist-shib-verify-%s.bu.edu/shibboleth' % landscape
    default_host = 'shib-%s.bu.edu' % landscape

# now we determine our other defaults
#
shib_host = os.environ.get('SHIB_HOST', default_host)
shib_path = os.environ.get('SHIB_PATH', 'idp/profile/SAML2/Unsolicited/SSO?providerId')
shib_sp = os.environ.get('SHIB_SP', default_sp)
sp_is_verify = default_sp_is_verify if shib_sp == default_sp else False 

# Get defaults from the json file
try:
    import json
    fname = os.environ.get('SHIB_PW_FILE', "~/.bupw.json")
    pwdict = json.loads(open(os.path.expanduser(fname)).read())
except:
    pwdict = { 'default': { 'user': "baduser", 'pw': 'badpw' } }

if landscape in pwdict:
    userpw = pwdict[landscape]
else:
    userpw = pwdict['default']

# The following are insecure by default and thus should be defined as secrets in docker
# fix in the future
shib_user = os.environ.get('SHIB_USER', userpw['user'])
shib_pw = os.environ.get('SHIB_PW', userpw['pw'])

import unittest
from selenium import webdriver

class InputFormsCheck(unittest.TestCase):

    #Opening browser.
    def setUp(self):
        #self.driver = webdriver.Chrome(r'C:\Users\pc\Downloads\chromedriver.exe')
        selenium_host = os.environ.get("SELENIUM_SERVER", "localhost")
        self.driver = webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.CHROME,
            command_executor="http://%s:4444/wd/hub" % selenium_host
        )
        self.driver.implicitly_wait(10)

    def get_error_text(self):
        # bunch of different ways to get error text
        # neterror - Chrome network error
        # error-box - Shibboleth IdP login error
        # content - Shibboleth low-level error
        #
        for examine in ('neterror', 'error-box', 'content'):
            try:
                return(self.driver.find_element_by_class_name(examine).text)
            except:
                pass
        
        # fall back to the page source - if this happens we should save a screenshot
        self.driver.get_screenshot_as_file('./error.png')
        return(self.driver.page_source)

    def test_shib_login(self):
        startURL = "https://%s/%s=%s" % (shib_host, shib_path, shib_sp)
        print("start_url: %s" % startURL)
        driver=self.driver
        driver.get(startURL)

        # we wrap the whole thing in a try block to get more debugging info if there's a failure
        try:

            assert driver.title == 'Boston University | Login'

            # look for the username/password prompt and fill it
            user_field = driver.find_element_by_id('j_username')
            user_field.clear()
            user_field.send_keys(shib_user)
            password_field = driver.find_element_by_id('j_password')
            password_field.clear()
            password_field.send_keys(shib_pw)
            login_button = driver.find_element_by_class_name('input-submit')
            login_button.click()


            # if the authentication worked then we shouldn't be on the login page
            assert driver.title != 'Boston University | Login'

            # the default_sp (verify nodes) put the username in the title which is a simple
            # check that authentication worked and got the correct username
            if sp_is_verify:
                assert shib_user in driver.title

        except:
            print("ERROR: title='%s' error=%s" % (driver.title, self.get_error_text()))
            #driver.get_screenshot_as_file('./images/state.png')
            #print("ERROR: title='%s' image dumped" % driver.title)
            raise

        #print("**** cookies ****")
        #print(driver.get_cookies())

        #driver.get_screenshot_as_file("./images/state.png")

        #for ltype in ( 'browser', 'driver', 'client', 'server'):
        #    print("**** %s ****" % ltype)
        #    try:
        #        print(driver.get_log(ltype))
        #    except: 
        #        print("<No logs found>")

    #Testing Single Input Field.    
    # def test_singleInputField(self):
    #     pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
    #     driver=self.driver
    #     driver.get(pageUrl)

        # #Finding "Single input form" input text field by id. And sending keys(entering data) in it.
        # eleUserMessage = driver.find_element_by_id("user-message")
        # eleUserMessage.clear()
        # eleUserMessage.send_keys("Test Python")

        # #Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
        # eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
        # eleShowMsgBtn.click()

        # #Checking whether the input text and output text are same using assertion.
        # eleYourMsg=driver.find_element_by_id("display")
        # assert "Test Python" in eleYourMsg.text
 
    # Closing the browser.
    def tearDown(self):
        self.driver.close()

# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main(warnings='ignore')
