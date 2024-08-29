# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from appium.webdriver.common.appiumby import AppiumBy

from toolium.pageobjects.page_object import PageObject


class GoogleMapsPageObject(PageObject):
    skip_button = '//android.widget.Button[@text="SKIP"]'
    search_bar = 'com.google.android.apps.maps:id/search_omnibox_text_box'
    navigation_items = [
        '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/navigation_bar_item_icon_view"])[1]',
        '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/navigation_bar_item_icon_view"])[2]',
        '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/navigation_bar_item_icon_view"])[3]',
        '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/navigation_bar_item_icon_view"])[4]',
        '(//android.widget.ImageView[@resource-id="com.google.android.apps.maps:id/navigation_bar_item_icon_view"])[5]'
    ]


    def skip_popup(self):
        """Search a skip button and click on it

        :returns: this page object instance
        """
        self.driver.find_element(AppiumBy.XPATH, self.skip_button).click()
        return self

    def verify_search_bar(self):
        """Verify the search bar is visible

        :returns: this page object instance
        """
        self.driver.find_element(AppiumBy.ID, self.search_bar).is_displayed()
        return self

    def navigate_buttons(self):
        """Navigate through bottom Google Maps buttons

        :returns: this page object instance
        """
        for index, xpath in enumerate(self.navigation_items):
            self.driver.find_element(AppiumBy.XPATH, xpath).click()
        return self

    def close_app(self):
        """Navigate through bottom Google Maps buttons

        :returns: this page object instance
        """
        self.driver.terminate_app('com.google.android.apps.maps')

        self.driver.quit()


