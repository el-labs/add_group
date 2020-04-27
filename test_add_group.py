# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        #Open home pagew
        wd.get("http://localhost/addressbook/")
        #Login
        wd.find_element_by_name("user").send_keys(Keys.DOWN)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        #Open groupe page
        wd.find_element_by_link_text("groups").click()
        #init group creation
        wd.find_element_by_name("new").click()
        #Fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("sadasd")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("asfafasfaf")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("asfsafasfasf")
        #Submit
        wd.find_element_by_name("submit").click()
        # return groups page
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("groups").click()
        #logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
