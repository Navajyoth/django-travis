from urlparse import urljoin

from django.core.urlresolvers import resolve
from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from apps.utils.tests import SeleniumTestCase


class AccountTestCase(SeleniumTestCase):

    def register(self, email='test@test2.com', password='Abcd@1234', path='/register/'):
        """
        Method to register in the site.It's called in login test.
        """
        register_page = self.selenium.get(self.get_absolute_url(path))
        self.by_id("id_first_name").send_keys('foo')
        self.by_id("id_last_name").send_keys('bar')
        self.by_id("id_email").send_keys(email)
        self.by_id("id_email_confirm").send_keys(email)
        self.by_id("id_password").send_keys(password)
        self.by_xpath('//button[@type="submit"]').click()

    def test_01_account_register(self):
        """
        Testing a successful registration.
        """
        self.register()
        self.assertEquals(
            self.selenium.current_url, self.get_absolute_url())
        print 'test_register_valid_password completed'

    def test_02_account_login(self):
        """
        Testing the login form with valid email and password
        """
        self.login(email='test@test1.com', password='Abcd@1234')
        self.assertEquals(
            self.selenium.current_url, self.get_absolute_url())
        print 'valid login test completed'