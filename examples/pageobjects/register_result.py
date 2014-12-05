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
from seleniumtid.pageelements import Text
from selenium.webdriver.common.by import By


class RegisterResultPageObject(PageObject):
    def init_page_elements(self):
        self.message = Text(By.XPATH, "//div[@id='content']/div/div/div/b[2]")