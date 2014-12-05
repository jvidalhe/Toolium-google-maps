# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
from seleniumtid.pageobjects.page_object import PageObject
from seleniumtid.pageelements import InputText, Select, PageElement
from selenium.webdriver.common.by import By


class RegisterPageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.NAME, 'username')
        self.password = InputText(By.ID, 'password')
        self.name = InputText(By.ID, 'name')
        self.email = InputText(By.ID, 'email')
        self.place = Select(By.ID, 'place')
        self.submit = PageElement(By.ID, 'registerButton')

    def open(self):
        self.driver.get(self.config.get('Common', 'url'))

    def register(self, user):
        self.logger.debug("Registering a new user")
        self.username.text = user['username']
        self.password.text = user['password']
        self.name.text = user['name']
        self.email.text = user['email']
        self.place.option = user['place']
        self.submit.element().click()