from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from android_behave_google_maps.pageobjects.google_maps import GoogleMapsPageObject


# @given('the Google Maps app is launched on the device')
# def step_launch_google_maps(context):
#     global driver
#     # Crear una instancia de AppiumOptions
#     options = AppiumOptions()
#
#     # Configurar las capacidades para Android
#     options.set_capability('platformName', 'Android')
#     options.set_capability('platformVersion', '15')  # La versión del emulador
#     options.set_capability('deviceName', 'emulator-5554')
#     options.set_capability('automationName', 'UiAutomator2')
#     options.set_capability('appPackage', 'com.google.android.apps.maps')
#     options.set_capability('appActivity', 'com.google.android.maps.MapsActivity')
#
#     # Inicializar el WebDriver con las opciones configuradas
#     driver = webdriver.Remote(
#         command_executor='http://127.0.0.1:4723',
#         options=options
#     )
#
#     print("Google Maps se abre en el dispositivo.")

@given('The Google maps app is open')
def step_impl(context):
    context.current_page = GoogleMapsPageObject()


@when('The user skips the initial popup')
def step_skip_initial_popup(context):
    context.current_page.skip_popup()


@then('The search bar is visible')
def step_verify_search_bar(context):
    context.current_page.verify_search_bar()


@when('The user navigates through the menu items')
def step_navigate_menu_items(context):
    context.current_page.navigate_buttons()


@then('The user closes the Google Maps app')
def step_close_google_maps(context):
    context.current_page.close_app()
